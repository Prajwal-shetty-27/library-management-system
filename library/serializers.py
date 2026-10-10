from rest_framework import serializers
from .models import Book, Member, Borrow


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'

    def validate_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return value


class BorrowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrow
        fields = '__all__'

    def validate_book(self, book):

        if not book.available:
            raise serializers.ValidationError(
                'This book is currently unavailable.'
            )

        return book