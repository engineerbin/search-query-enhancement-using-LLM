from django.shortcuts import render
from .models import Document

def search_view(request):
    # Example view for handling a search request
    query_text = request.GET.get('query', '')
    documents = Document.objects.filter(content__icontains=query_text)
    return render(request, 'search/results.html', {'documents': documents})
