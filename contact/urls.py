from django.urls import path
from contact import views

urlpatterns = [
    path('', view=views.index, name='index'),
]
