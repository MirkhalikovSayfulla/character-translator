from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('translator/<str:translatorType>/',
         views.TranslateView.as_view(), name="translator")
]
