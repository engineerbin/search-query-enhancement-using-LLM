from django.shortcuts import render
from .models import Document
from .utils import query

def search_view(request):
    # Example view for handling a search request
    query_text = request.GET.get('query', '')
    action = request.GET.get('action', 'Search')
    documents = query.searching(query_text)
    
    # return render(request, 'search/results.html', {
    #     'query': query_text,
    #     'better_query': better_query,
    #     'documents': documents
    # })

    documents = query.searching(query_text)
    enhanced_documents = None
    enhanced_query = None

    if action == 'Enhance Query':
        # Call get_expanded_query to enhance the query
        prompt = query.create_prompt(query_text, documents)
        enhanced_query = query.get_expanded_query(prompt)
        enhanced_documents = query.searching(enhanced_query) if enhanced_query else None

    return render(request, 'search/results.html', {
        'query': query_text,
        'documents': documents,
        'enhanced_query': enhanced_query,
        'enhanced_documents': enhanced_documents
    })
