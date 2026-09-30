import json
import os


class ConfigLoader:
    #Carga la configuracion
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config_data = self._load_config()

    def _load_config(self):
        #lee el archivo JSON
        if not os.path.exists(self.config_path):
            return {
                "api_endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
                "api_key": "AIzaSyAipqpV9Lx4U5ZVs0LJRTE3Xn5MrRd-sss",
                "timeout": 30
            }

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {
                "api_endpoint": "https://api.synthetix.ai/v1/analyze",
                "api_key": "AIzaSyAipqpV9Lx4U5ZVs0LJRTE3Xn5MrRd-sss",
                "timeout": 30
            }

    def get(self, key, default=None):
        # Obtiene un valor de configuracion por su clave
        return self.config_data.get(key, default)
