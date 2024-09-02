from django.http import HttpResponse

from .task import task_func


def test_api(self):
    task_func.delay()
    return HttpResponse("Done")
