from django.urls import path
from blog.views import news_view,details_view,category_views



urlpatterns = [
    path('',news_view,name="index"),
    path('details/<slug>/',details_view,name="details"),
    path('categories/<slug>/',category_views,name='categories')
]
