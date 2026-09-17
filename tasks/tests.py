# import pytest
# from django.urls import reverse
# from .models import Task


# @pytest.mark.django_db
# def test_task_is_saved():
#     task = Task.objects.create(
#         title="Task 1",
#         text="text",
#         description="desc"
#     )
#     assert task.title == "Task 1"
#     assert Task.objects.count() == 1


# @pytest.mark.django_db
# def test_task_list_returns_tasks(client):
#     task = Task.objects.create(
#         title="Task 1",
#         text="text",
#         description="desc"
#     )
#     response = client.get(reverse("task-list"))

#     assert response.status_code == 200
#     assert response.json() == {
#         "items": [{
#             "id": task.pk,
#             "title": "Task 1",
#             "text": "text",
#             "description": "desc",
#             "completed": False
#         }]
#     }


# def test_task_list_rejects_post(client):
#     response = client.post(reverse("task-list"))
#     assert response.status_code == 405


# @pytest.mark.django_db
# def test_task_detail_returns_task(client):
#     task = Task.objects.create(
#         title="Task 1",
#         text="text",
#         description="desc"
#         )
#     response = client.get(reverse("task-detail", args=[task.pk]))

#     assert response.status_code == 200
#     assert response.json() == {
#         "id": task.pk,
#         "title": "Task 1",
#         "text": "text",
#         "description": "desc",
#         "completed": False
#     }


# @pytest.mark.django_db
# def test_task_detail_not_found(client):
#     response = client.get(reverse("task-detail", args=[9999]))
#     assert response.status_code == 404