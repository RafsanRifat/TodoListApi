from django.urls import path
from .views import RegisterApiView

urlpatterns = [
    path('registration/', RegisterApiView.as_view(), name='registration')
]
