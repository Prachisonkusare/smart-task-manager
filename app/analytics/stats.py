import pandas as pd
import numpy as np

from app.models.task import Task


def task_analytics():

    tasks = Task.query.all()

    task_data = []

    for task in tasks:

        task_data.append({
            "title": task.title,
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    if total_tasks == 0:

        return {
            "total": 0,
            "completed": 0,
            "pending": 0,
            "percentage": 0
        }

    completed_tasks = len(
        df[df["status"] == "Completed"]
    )

    pending_tasks = total_tasks - completed_tasks

    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {
        "total": total_tasks,
        "completed": completed_tasks,
        "pending": pending_tasks,
        "percentage": completion_percentage
    }