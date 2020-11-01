from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('translator/<str:translatorCh>/',
         views.TranslateView.as_view(), name="translator")
]
