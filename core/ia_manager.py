import json
import urllib.request
import urllib.error
from data_structures.queue import Queue


class IARequest:
    #Solicitud de analisis encolada
    def __init__(self, filename, code_content):
        self.filename = filename
        self.code_content = code_content


class IAManager:
    #Buffer FIFO para administrar y despachar solicitudes de analisis a una API real
    def __init__(self, api_endpoint="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent", api_key=""):
        self.request_queue = Queue()
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def enqueue_request(self, filename, code_content):
        # Encola una nueva solicitud en el buffer FIFO
        if not code_content:
            return False, "El archivo esta vacio, no hay codigo para analizar."

        request = IARequest(filename, code_content)
        self.request_queue.enqueue(request)
        return True, f"Solicitud de analisis para '{filename}' agregada a la cola FIFO."

    def get_queue_status(self):
        # Devuelve el numero de peticiones pendientes en el buffer
        return self.request_queue.size

    def process_next_request(self):
        # Despacha la siguiente solicitud y realiza la llamada HTTP real a la API
        if self.request_queue.is_empty():
            return False, "La cola de peticiones esta vacia.", None

        if not self.api_key:
            return False, "Error: No se ha configurado una API Key valida en config.json.", None

        request = self.request_queue.dequeue()

        # Construccion de la peticion HTTP a la API real
        url = f"{self.api_endpoint}?key={self.api_key}"
        
        prompt_text = (
            f"Analiza el siguiente codigo Python del archivo '{request.filename}'. "
            f"Indica brevemente su complejidad algoritmica O-grande y dame una sugerencia corta de refactorizacion:\n\n"
            f"{request.code_content}"
        )

        payload = {
            "contents": [{
                "parts": [{"text": prompt_text}]
            }]
        }

        data = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json"}

        try:
            req = urllib.request.Request(url, data=data, headers=headers, method="POST")
            
            with urllib.request.urlopen(req, timeout=15) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                
                # Extraccion del texto generado por el modelo de IA
                ia_response_text = response_data["candidates"][0]["content"]["parts"][0]["text"]

                analysis_result = {
                    "filename": request.filename,
                    "complexity": "Analizado por IA",
                    "refactoring_suggestion": ia_response_text.strip(),
                    "endpoint_used": self.api_endpoint,
                    "key_configured": True
                }
                
                return True, f"Analisis real de '{request.filename}' completado con exito.", analysis_result

        except urllib.error.HTTPError as e:
            return False, f"Error HTTP de la API ({e.code}): {e.reason}", None
        except urllib.error.URLError as e:
            return False, f"Error de conexion a la API: {e.reason}", None
        except Exception as e:
            return False, f"Error inesperado procesando la peticion: {str(e)}", None
