from django.urls import path
from user import views
urlpatterns = [
    path('home/',views.home , name='home'),
    path('login/',views.login , name='login'),
    path('signup/',views.signup , name='signup'),
    path('logout_view/',views.logout_view,name="logout_view"),
]

