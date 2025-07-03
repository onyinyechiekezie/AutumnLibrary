from rest_framework import serializers

from .models import Book, Author


# from user.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary']

    # author = serializers.ManyRelatedField(
    #     queryset=Author.objects.all(),
    #     read_only=True,
    # )
