from django.urls import path, include
from . import views
from .views import HomePageView, UrlCreateView, CertainPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('search', UrlCreateView.as_view(), name='url_create'),
    path('<int:link_id>', CertainPage.as_view()),
]