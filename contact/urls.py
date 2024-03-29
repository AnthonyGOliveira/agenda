from django.urls import path
from contact import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:contact_id>/', view=views.contact, name='contact'),
]
