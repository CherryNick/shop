from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit_profile'),
    path('verify/<email>/<activation_key>/', views.verify, name='verify')
]
