from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router_book = DefaultRouter()
router_book.register(r"books", views.BookViewSet, basename="book")
