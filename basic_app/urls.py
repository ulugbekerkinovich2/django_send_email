from django.urls import path

from basic_app import views

urlpatterns = [
    path('email/', views.send_email, name='index')
]
