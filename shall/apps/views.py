from django.shortcuts import render
from .models import Wiki

def greetings(request):
    return render(request, 'greetings.html')

def main_page(request):
    wiki_list = Wiki.objects.order_by('-updated_at')
    context = {
        "wiki_list": wiki_list,
    }
    return render(request, 'main_page.html', context)