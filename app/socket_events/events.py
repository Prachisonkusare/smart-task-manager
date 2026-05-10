from app import socketio


def send_task_notification():

    socketio.emit(
        "new_task",
        {
            "message": "New Task Added Successfully"
        }
    )