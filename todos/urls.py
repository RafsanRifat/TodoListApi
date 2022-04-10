from django.urls import path
from .views import TodoCreateApiView, TodoAllView


urlpatterns = [
    path('create/', TodoCreateApiView.as_view(), name='create'),
    path('all/<int:id>', TodoAllView.as_view(), name='all')
]