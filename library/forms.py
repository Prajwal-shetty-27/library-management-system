from django import forms
from .models import Book, Member, Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return phone

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['member', 'book']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['book'].queryset = Book.objects.filter(available=True)

    def clean_book(self):
        book = self.cleaned_data['book']

        if not book.available:
            raise forms.ValidationError(
                'This book is currently unavailable.'
            )

        return book