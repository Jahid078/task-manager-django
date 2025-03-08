# tasks.py
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from .models import Task
from simple_setup import settings

def send_task_reminders():
    today = datetime.now().date()
    
    high_priority_tasks = Task.objects.filter(due_date=today + timedelta(days=1), priority="High")
    medium_priority_tasks = Task.objects.filter(due_date=today + timedelta(days=2), priority="Medium")
    low_priority_tasks = Task.objects.filter(due_date=today + timedelta(days=3), priority="Low")

    all_tasks = list(high_priority_tasks) + list(medium_priority_tasks) + list(low_priority_tasks)

    for task in all_tasks:
        send_mail (
            subject=f'Reminder: {task.title} ({task.priority} Priority) is due soon!',
            message=f'Hello,\n\nYour {task.priority} priority task "{task.title}" is due on {task.due_date}. Please complete it on time.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[task.user.email],
            fail_silently=False,
        )

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_task_reminders, 'interval', hours=24) 
    scheduler.start()
