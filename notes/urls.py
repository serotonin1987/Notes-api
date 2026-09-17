from django.urls import path
from .views import NoteListView, TaskViewSet# Оставляем только то, что реально есть в views.py
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register(r"tasks",TaskViewSet,basename= "task")

urlpatterns = [
    # path("notes/", note_list, name="note-list"),
    # path("notes/<int:pk>/", note_detail, name="note-detail"),
    # path("products/", product_list, name="product-list"),
    # path("task/", task, name="task-list"),
    path("notes/", NoteListView.as_view(), name="note-list"),
]