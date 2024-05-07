from django.shortcuts import render
from .models import Document
from .utils import query

def search_view(request):
    # Example view for handling a search request
    query_text = request.GET.get('query', '')
    documents = query.searching(query_text)
    prompt = query.create_prompt(query_text, documents)
    better_query = query.get_expanded_query(prompt)
    
    return render(request, 'search/results.html', {
        'query': query_text,
        'better_query': better_query,
        'documents': documents
    })
