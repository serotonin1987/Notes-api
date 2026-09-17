from rest_framework.test import APIClient
from rest_framework import status
from notes.models import Note
from tasks.models import Task
from datetime import datetime
import pytest


@pytest.mark.django_db
def test_get_notes():
    client = APIClient()
    Note.objects.create(title=
                        "Первая заметка",
                        text="Текст")
    
    response = client.get("/api/notes/")
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == "Первая заметка"


@pytest.mark.django_db
def test_create_note():
    client = APIClient()
    payload = {
        "title": "Новая заметка",
        "text": "Описание"
    }
    
    response = client.post("/api/notes/", data=payload, format="json")
    
    assert response.status_code == status.HTTP_201_CREATED
    assert Note.objects.count() == 1
    assert response.data["title"] == "Новая заметка"

@pytest.mark.django_db
def test_create_at():
    client = APIClient()
    this_time = datetime.now().strftime("%H:%M:%S")
    payload = {
        "title":"Новая заметка",
        "text":"текст заметки",
        "description":f"Создан в {this_time}",
    }

    responce =client.post("/api/notes/", data=payload, format="json")

    assert responce.status_code == status.HTTP_201_CREATED
    assert responce.data["description"] == f"Создан в {this_time}"

@pytest.mark.django_db
def test_completed_tasks():
    client = APIClient()
    that_time = datetime.now().strftime("%H:%M:%S")
    payload = {
        "title":"Новая заметка",
        "text":"текст заметки",
        "description":f"Создан в {that_time}",
        "completed":True,
    }

    responce =client.post("/api/tasks/", data=payload, format="json")
    
    assert responce.status_code == status.HTTP_201_CREATED
    assert responce.data["description"] == f"Создан в {that_time}"
    assert responce.data["completed"] is True