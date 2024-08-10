from django.http import JsonResponse, HttpResponse
# Create your views here.
from rest_framework.decorators import api_view

from .models import Book


@api_view(['GET'])
def get_all_books(request):
    return JsonResponse({'books': list(Book.objects.all().values())})
