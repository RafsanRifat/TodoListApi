from django.urls import path
from .views import TodoCreateApiView


urlpatterns = [
    path('create/', TodoCreateApiView.as_view(), name='create')
]