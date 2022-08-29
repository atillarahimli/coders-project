from blog.models import News,Category
from django.shortcuts import render,get_object_or_404


# Create your views here.


def news_view(request):
    all_items=[]
    news=News.objects.filter(draft=True)
    categories=Category.objects.all()
    for category in categories:
        blog = category.category_blog.filter(draft=True)
        all_items.append((category,blog))
    context={
        "news":news,
        "all_items":all_items,
        "categories":categories
    }
    

    return render(request,"main/index.html",context)


def details_view(request,slug):
    post = get_object_or_404(News,slug=slug)
    context= {
        "objects":post
    }

    return render(request,'details/single.html',context)


def category_views(request,slug):
    category = get_object_or_404(Category,slug=slug)
    blog = category.category_blog.all()

    context = {
        "blogs":blog
    }

    return render(request,'category/category.html',context)


