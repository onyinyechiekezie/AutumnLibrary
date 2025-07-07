from rest_framework import serializers

from .models import Book, Author, BookImage, BookInstance


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
        many=True,
    )
    class Meta:
        model = Book
        fields = ['id','title', 'summary','images','author']


class AddBookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['id','title','isbn', 'summary']

class BookImageSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     book_id = self.context['book_id']
    #     return BookImage.objects.create(book_id=book_id, **validated_data)

    class Meta:
        model = BookImage
        fields = ['id','image']


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['return_date', '']