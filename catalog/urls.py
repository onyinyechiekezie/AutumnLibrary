from django.urls import path
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, 'books')

print(router.urls)

urlpatterns = [
    path("", views.get_books),
    path("authors/", views.AddAuthorView.as_view(), name="add_author"),
    path("authors/<int:pk>/", views.update_author, name="update_author"),
    path("authors/<int:pk>/delete/", views.delete_author, name="delete_author"),
    path("get/authors/", views.get_authors, name="get_authors"),
    path("greet/<name>", views.greet),
]
