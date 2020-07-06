from pprint import pprint

from article.models import Comment
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .utility import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse


# Create your views here.
def index(request):
    # grab the homepage article, and random articles 
    #and pass to html via context 
    homepage_article = get_homepage_article()
    random_articles = get_random_articles(count=3)
    context = {'homepage_article':homepage_article,
                'random_articles':random_articles
                }


    return render(request,'home.html',context)

def article(request,uuid):
    # get all comments from latest to earlist
    comments = [comment for comment in Comment.objects.all().filter(article_uuid=uuid).order_by('-comment_date')]
    context = {'article':get_article_by_uuid(uuid),
                'stocks':get_random_stocks(count=3),
                'comments':comments
                }

    return render(request,'article.html',context)

def add_comment(request,uuid):
    # grab the reader comment and save it
    comment_input = request.POST.get('comment_input')
    
    if comment_input:
        comment = Comment(article_uuid=uuid,comment_text=comment_input)
        comment.save()
    # after saving redirect back to the article itself, so that comment can be displayed
    return HttpResponseRedirect(reverse('article', args=(uuid,)))

