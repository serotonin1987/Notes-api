from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from .models import Note,Product,Task
from rest_framework.generics import ListCreateAPIView,viewsets
from .serializers import NoteSerializer,TaskSerializer


# def note_list(request):
#     if request.method != "GET":
#         return JsonResponse({"detail": "Method not allowed"}, status=405)

#     notes = list(Note.objects.values("id", "title", "text"))
#     return JsonResponse({"items": notes})


# def note_detail(request, pk):
#     if request.method != "GET":
#         return JsonResponse({"detail": "Method not allowed"}, status=405)

#     # .first() вернет либо dict: {"id": 1, "title": "..."}, либо None
#     note = Note.objects.filter(pk=pk).values("id", "title", "text").first()

#     if note is None:
#         return JsonResponse({"detail": "Not found"}, status=404)
#     # Теперь в note ГАРАНТИРОВАННО лежит dict
#     return JsonResponse(note)

def product_list(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    # Получаем список словарей с полями id, name, description
    products = list(Product.objects.values("id", "name", "description"))
    
    # Передаем переменную products без кавычек
    return JsonResponse({"items": products})

class NoteListView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer