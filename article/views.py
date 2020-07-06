from pprint import pprint

from article.models import Comment
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .utility import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    homepage_article = get_homepage_article()
    #pprint(homepage_article)
    random_articles = get_random_articles(count=3)
    context = {'homepage_article':homepage_article,
                'random_articles':random_articles
                }

    #print(homepage_article[0]['images'])

    return render(request,'home.html',context)

def article(request,uuid):
    comments = [comment for comment in Comment.objects.all().filter(article_uuid=uuid).order_by('-comment_date')]
    context = {'article':get_article_by_uuid(uuid),
                'stocks':get_random_stocks(count=3),
                'comments':comments
                }

    return render(request,'article.html',context)

@csrf_exempt
def add_comment(request,uuid):
    comment_text = request.POST.get('data')
    if comment_text:
        q = Comment(comment_text=comment_text, article_uuid=uuid)
        q.save()
        return HttpResponse(comment_text)
