from django.shortcuts import render
from .models import Topic, Politic,New, Metro, Entertainment, latest

# Create your views here.

def home (request):
    '''render home page'''
    my_topic =Topic.objects.all()
    politic=Politic.objects.all()
    new=New.objects.all()
    metro=Metro.objects.all()
    entertain=Entertainment.objects.all()
    latest_news=latest.objects.all()
    return render(request,'index.html', {'topics': my_topic ,'politic': politic, 'News':new, 'metro':metro, 'entertain':entertain, 'latest':latest_news})



def politics(request):
    '''render politics content'''
    politic1=Politic.objects.all()
    return render(request, 'politics.html', {'politic': politic1})

def metro(request):
    '''render politics content'''
    metro=Metro.objects.all()
    return render(request, 'metro.html', {'metro': metro})

def news(request):
    '''render politics content'''
    new=New.objects.all()
    return render(request, 'news.html', {'new': new})

# def sport(request):
#     '''render politics content'''
#     sport=Spo.objects.all()
#     return render(request, 'news.html', {'new': new})
def entertain(request):
    '''render entertain content'''
    entertain=Entertainment.objects.all()
    return render(request, 'entertainment.html', {'entertain': entertain})

def article(request, post_id):
    '''render article page'''
    print(post_id)
    article=Topic.objects.get(id=post_id)
    
    return render (request, 'article.html',{'article':article, })

def article2(request, post_id):
    '''render article page'''
    print(post_id)
    article2=Politic.objects.get(id=post_id)
    return render (request, 'article2.html',{'article2':article2, })

def article3(request, post_id):
    '''render article page'''
    print(post_id)
    article3=New.objects.get(id=post_id)
    return render (request, 'article3.html',{'article3':article3, })
def article4(request, post_id):
    '''render article page'''
    print(post_id)
    article4=Metro.objects.get(id=post_id)
    return render (request, 'article4.html',{'article4':article4, })
def article5(request, post_id):
    '''render article page'''
    print(post_id)
    article5=Entertainment.objects.get(id=post_id)
    return render (request, 'article5.html',{'article5':article5, })

def article6(request, post_id):
    '''render article page'''
    print(post_id)
    article6=latest.objects.get(id=post_id)
    return render (request, 'article6.html',{'article6':article6, })
