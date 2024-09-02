from celery import shared_task


@shared_task(bind=True)
def task_func(self):
    # Operatins you need
    for i in range(1, 6):
        print(f"{i} Task")
    return "Done"
