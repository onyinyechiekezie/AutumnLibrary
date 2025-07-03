from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author, BookImage
from .serializers import BookSerializer, AddBookSerializer, BookImageSerializer
from .serializers import AuthorSerializer

# Create your views here.
@api_view()
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(["POST"])
def add_author(request):
    author = AuthorSerializer(data=request.data)
    author.is_valid(raise_exception=True)
    author.save()
    return Response(author.data, status=status.HTTP_201_CREATED)

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}.")
@api_view(["GET"])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class AddAuthorView(ListCreateAPIView):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
@api_view()
def get_author(request):
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT", "PATCH"])
def update_author(request, pk):
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

def delete_author(request, pk):
    author = Author.objects.get(pk=pk)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



def greet(request, name):
    return render(request, 'index.html', {'name': name})

@api_view(["GET"])
def image_detail(request, pk):
    book_image = Book.objects.get(pk=pk)
    serializer = BookImageSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBookSerializer
        elif self.request.method == 'PUT':
            return AddBookSerializer

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return{"book_id": self.kwargs["book_pk"]}
