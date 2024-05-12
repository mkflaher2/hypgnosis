from app.models.control import ControlModel

import uvicorn
from fastapi import FastAPI

app = FastAPI()
PORT: int = 8081

masterlist = {}

class ControlState:
    def __init__(self):
        self.state = ControlModel()

#@app.post("/state")
#async def update_state(state: ControlModel):
#    control_state.state = state
#    return control_state.state
#
#@app.get("/state")
#async def get_state():
#    return control_state.state

@app.post("/users/{user_id}")
async def update_user_state(user_id: str, control_model: ControlModel):
    masterlist[user_id] = control_model
    return control_model

@app.get("/users/{user_id}")
async def get_user_state(user_id):
    return masterlist[user_id]

if __name__ == "__main__":
    control_state = ControlState()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
