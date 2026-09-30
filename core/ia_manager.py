from data_structures.queue import Queue


class IARequest:
    # Representa una solicitud de analisis encolada
    def __init__(self, filename, code_content):
        self.filename = filename
        self.code_content = code_content


class IAManager:
    # Buffer FIFO para administrar y despachar solicitudes de analisis a la IA
    def __init__(self, api_endpoint="https://api.synthetix.ai/v1/analyze", api_key=""):
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
        # Despacha y procesa la siguiente solicitud en el frente de la cola FIFO
        if self.request_queue.is_empty():
            return False, "La cola de peticiones esta vacia.", None

        request = self.request_queue.dequeue()

        # Simulacion del analisis de complejidad y refactorizacion recibido de la API
        lines_count = len(request.code_content.splitlines())
        complexity = "O(n)" if lines_count > 10 else "O(1)"

        analysis_result = {
            "filename": request.filename,
            "complexity": complexity,
            "refactoring_suggestion": f"Estructura optima. Considera modularizar las funciones de mas de {lines_count} lineas.",
            "endpoint_used": self.api_endpoint,
            "key_configured": bool(self.api_key)
        }

        return True, f"Analisis de '{request.filename}' completado con exito.", analysis_result
