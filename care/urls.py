
from django.urls import path
from django.urls.conf import include
from . import views


app_name = "care"
urlpatterns = [
    path('', views.login_page, name='login'),
    path('/payment', views.payment, name='payment'),
    path('routines/', views.routines, name='routines'),
    path('details/', views.details, name='details'),

]
