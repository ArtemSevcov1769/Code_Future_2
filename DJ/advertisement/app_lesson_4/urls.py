from django.urls import path
from .views import example

urlpatterns = [
    path("lesson_4/", example),
]
