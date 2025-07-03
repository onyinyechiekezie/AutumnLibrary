from rest_framework import serializers

from .models import Book, Author, BookImage


# from user.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='image-detail',
        queryset=BookImage.objects.all(),
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary']


class AddBookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['id','title', 'summary','images','author']