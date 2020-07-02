from pprint import pprint

from django.shortcuts import render
from .utility import *
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
    context = {'article':get_article_by_uuid(uuid)}

    return render(request,'article.html',context)