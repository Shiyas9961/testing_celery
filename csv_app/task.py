from celery import shared_task


@shared_task(bind=True)
def parse_csv(self, num) :
    for i in range(num) :
        print(i)
    return None