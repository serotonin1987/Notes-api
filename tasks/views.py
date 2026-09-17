from django.http import JsonResponse
from .models import Task


def task_list(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    tasks = list(Task.objects.values(
        "id",
        "title",
        "text",
        "description",
        "completed"))
    return JsonResponse({"items": tasks})


def task_detail(request, pk):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    task = Task.objects.filter(pk=pk).values(
        "id",
        "title",
        "text",
        "description",
        "completed").first()

    if task is None:
        return JsonResponse({"detail": "Not found"}, status=404)

    return JsonResponse(task)

