from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Borrow
from .forms import BookForm, MemberForm, BorrowForm
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    BookSerializer,
    MemberSerializer,
    BorrowSerializer
)


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})

@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'library/delete_book.html', {'book': book})


@login_required
def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(
        request,
        'library/book_list.html',
        {'books': books}
    )

@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm()

    return render(request, 'library/add_member.html', {'form': form})


@login_required
def edit_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm(instance=member)

    return render(request, 'library/edit_member.html', {
        'form': form,
        'member': member
    })


@login_required
def delete_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('member_list')

    return render(request, 'library/delete_member.html', {
        'member': member
    })


@login_required
def issue_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)

        if form.is_valid():
            borrow = form.save()

            borrow.book.available = False
            borrow.book.save()

            return redirect('borrow_list')

    else:
        form = BorrowForm()

    return render(request, 'library/issue_book.html', {'form': form})


@login_required
def borrow_list(request):
    borrows = Borrow.objects.all()

    total_borrows = Borrow.objects.count()

    returned_books = Borrow.objects.filter(
        returned_date__isnull=False
    ).count()

    return render(
        request,
        'library/borrow_list.html',
        {
            'borrows': borrows,
            'total_borrows': total_borrows,
            'returned_books': returned_books,
        }
    )


@login_required
def return_book(request, id):
    borrow = get_object_or_404(Borrow, id=id)

    if request.method == 'POST':
        borrow.returned_date = timezone.now().date()
        borrow.book.available = True

        borrow.book.save()
        borrow.save()

        return redirect('borrow_list')

    return render(request, 'library/return_book.html', {
        'borrow': borrow
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'library/login.html', {'form': form})

@login_required
def dashboard(request):
    total_books = Book.objects.count()
    available_books = Book.objects.filter(available=True).count()
    borrowed_books = Book.objects.filter(available=False).count()
    total_members = Member.objects.count()

    return render(request, 'library/dashboard.html', {
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'total_members': total_members,
    })

def logout_view(request):
    logout(request)
    return redirect('login')

class BookAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BookDetailAPI(APIView):

    def get_object(self, id):
        return get_object_or_404(Book, id=id)

    def get(self, request, id):
        book = self.get_object(id)

        serializer = BookSerializer(book)

        return Response(serializer.data)

    def put(self, request, id):
        book = self.get_object(id)

        serializer = BookSerializer(
            book,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id):
        book = self.get_object(id)

        serializer = BookSerializer(
            book,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        book = self.get_object(id)

        book.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class MemberAPI(APIView):

    def get(self, request):
        members = Member.objects.all()

        serializer = MemberSerializer(
            members,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = MemberSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class MemberDetailAPI(APIView):

    def get_object(self, id):
        return get_object_or_404(Member, id=id)

    def get(self, request, id):
        member = self.get_object(id)

        serializer = MemberSerializer(member)

        return Response(serializer.data)

    def put(self, request, id):
        member = self.get_object(id)

        serializer = MemberSerializer(
            member,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id):
        member = self.get_object(id)

        serializer = MemberSerializer(
            member,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        member = self.get_object(id)

        member.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class BorrowAPI(APIView):

    def get(self, request):
        borrows = Borrow.objects.all()

        serializer = BorrowSerializer(
            borrows,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = BorrowSerializer(
            data=request.data
        )

        if serializer.is_valid():
            borrow = serializer.save()

            borrow.book.available = False
            borrow.book.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BorrowDetailAPI(APIView):

    def get_object(self, id):
        return get_object_or_404(Borrow, id=id)

    def get(self, request, id):
        borrow = self.get_object(id)

        serializer = BorrowSerializer(borrow)

        return Response(serializer.data)

    def put(self, request, id):
        borrow = self.get_object(id)

        serializer = BorrowSerializer(
            borrow,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id):
        borrow = self.get_object(id)

        serializer = BorrowSerializer(
            borrow,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        borrow = self.get_object(id)

        borrow.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class ReturnBookAPI(APIView):

    def post(self, request, id):
        borrow = get_object_or_404(Borrow, id=id)

        if borrow.returned_date:
            return Response(
                {"error": "This book has already been returned."},
                status=status.HTTP_400_BAD_REQUEST
            )

        borrow.returned_date = timezone.now().date()
        borrow.save()

        borrow.book.available = True
        borrow.book.save()

        serializer = BorrowSerializer(borrow)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )