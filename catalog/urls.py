from django.urls import path
from django.urls import path, include
from rest_framework_nested import routers

from . import views
from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, 'books')
router.register("images", BookImageViewSet, "book-images")

book_image_router = routers.NestedSimpleRouter(router, 'books', lookup='book')
book_image_router.register('images', BookImageViewSet, 'book-images')

urlpatterns = [
    path('', include(router.urls)),

    path('', include(book_image_router.urls)),
    # path("", views.get_books),
    path("authors/", views.AddAuthorView.as_view(), name="add_author"),
    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view()),
    path("images/<int:pk>/", views.image_detail, name="image_detail"),
    path("borrow-books/<int:pk>/", views.borrow_book, name="borrow-book"),
    # path("authors/<int:pk>/", views.update_author, name="update_author"),
    # path("authors/<int:pk>/delete/", views.delete_author, name="delete_author"),
    # path("get/authors/", views.get_authors, name="get_authors"),
    # path("greet/<name>", views.greet),
]
