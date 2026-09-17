from django.urls import path
from .views import NoteListView  # Оставляем только то, что реально есть в views.py

urlpatterns = [
    # path("notes/", note_list, name="note-list"),
    # path("notes/<int:pk>/", note_detail, name="note-detail"),
    # path("products/", product_list, name="product-list"),
    # path("task/", task, name="task-list"),
    path("notes/", NoteListView.as_view(), name="note-list"),
]