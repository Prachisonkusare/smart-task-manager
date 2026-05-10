from app.analytics.stats import task_analytics
from app.socket_events.events import send_task_notification
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app import db

from app.models.task import Task

task = Blueprint("task", __name__)


@task.route("/dashboard")
def dashboard():

    tasks = Task.query.all()
    analytics = task_analytics()

    return render_template(
    "dashboard.html",
    tasks=tasks,
    analytics=analytics
)
    


@task.route("/add-task", methods=["POST"])
def add_task():

    title = request.form.get("title")

    description = request.form.get("description")

    priority = request.form.get("priority")

    status = request.form.get("status")

    new_task = Task(
        title=title,
        description=description,
        priority=priority,
        status=status
    )

    db.session.add(new_task)

    db.session.commit()

    send_task_notification()

    return redirect(url_for("task.dashboard"))

@task.route("/delete-task/<int:id>")
def delete_task(id):

    task_to_delete = Task.query.get(id)

    db.session.delete(task_to_delete)

    db.session.commit()

    return redirect(url_for("task.dashboard"))

@task.route("/update-task/<int:id>", methods=["GET", "POST"])
def update_task(id):

    task_to_update = Task.query.get(id)

    if request.method == "POST":

        task_to_update.title = request.form.get("title")

        task_to_update.description = request.form.get("description")

        task_to_update.priority = request.form.get("priority")

        task_to_update.status = request.form.get("status")

        db.session.commit()

        return redirect(url_for("task.dashboard"))

    return render_template(
        "update_task.html",
        task=task_to_update
    )