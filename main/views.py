from django.shortcuts import render, get_object_or_404
from .models import Article
import openai
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'main/article_detail.html', {'article': article})



openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return render(request, 'main/chatbot.html', {'answer': answer})
    
    return render(request, 'main/chatbot.html')