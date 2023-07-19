from django.urls import path
from .views import example

urlpatterns = [
    path("ex/", example),
    path("example/", example)
]
