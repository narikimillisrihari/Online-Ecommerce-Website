from django.urls import path
from website import views
urlpatterns = [
    path('homepage/',views.homepage , name='homepage'),
]

