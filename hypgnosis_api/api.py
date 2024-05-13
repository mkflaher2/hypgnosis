from app.models.control import ControlModel

from datetime import datetime
from fastapi import FastAPI
import time
import uvicorn
app = FastAPI()
PORT: int = 8081

masterlist = {}

@app.post("/users/{user_id}")
async def update_user_state(user_id: str, control_model: ControlModel):
    masterlist[user_id] = control_model
    timestamp_now = time.mktime(datetime.now().timetuple())
    masterlist[user_id].last_updated = timestamp_now

    return control_model

@app.get("/users/{user_id}")
async def get_user_state(user_id):
    timestamp_now = time.mktime(datetime.now().timetuple())
    masterlist[user_id].last_updated = timestamp_now

    return masterlist[user_id]

# If a session has been inactive for long enough, remove it from memory.
# NOTE: on prod, this will be called by curl in a cron job
@app.post("/clear_dead_sessions")
async def clear_dead_sessions():
    dead_sessions = {}
    dead_session_ids = []
    for user_id in masterlist:
        timestamp_now = time.mktime(datetime.now().timetuple())
        instance_age = timestamp_now - masterlist[user_id].last_updated

        # Kill sessions older than 5 minutes.
        if instance_age > 300:
            dead_session_ids.append(user_id)

    for user_id in dead_session_ids:
        dead_sessions[user_id] = masterlist.pop(user_id)

    return dead_sessions

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
