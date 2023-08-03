from rest_framework import serializers
from myCaseStudy.models import  User, Book
class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    bookTitle = serializers.CharField(max_length=180)
    bookAuthor = serializers.CharField(max_length=180)
    bookDescription = serializers.CharField(max_length=180)
    bookCover = serializers.ImageField()
    class Meta:
        model = Book
        fields = "__all__"