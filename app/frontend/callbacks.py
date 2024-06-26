from app.models.control import ControlModel

import os
import requests

class CallbackHandler:
    def __init__(self, control_model: ControlModel, api_url: str = None):
        self.control_model = control_model
        self.api_url = os.getenv("HYPGNOSIS_API_URL")

    def update_state(self):
        print(self.control_model.model_dump())

        try:
            response = requests.post(
                f"{self.api_url}/users/{self.control_model.user_id}",
                json=self.control_model.model_dump()
            )
        except Exception as e:
            print(f"Unable to connect to API server: {e}")

