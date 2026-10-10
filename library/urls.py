from django.urls import path
from .views import (
    book_list, add_book, edit_book, delete_book,
    member_list, add_member, edit_member, delete_member,
    issue_book, borrow_list, return_book,
    dashboard, login_view, logout_view,
    BookAPI, BookDetailAPI,MemberAPI,MemberDetailAPI, BorrowAPI,BorrowDetailAPI,ReturnBookAPI
)
urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:id>/', edit_book, name='edit_book'),
    path('books/delete/<int:id>/', delete_book, name='delete_book'),

    path('members/', member_list, name='member_list'),
    path('members/add/', add_member, name='add_member'),
    path('members/edit/<int:id>/', edit_member, name='edit_member'),
    path('members/delete/<int:id>/', delete_member, name='delete_member'),

    path('borrow/', borrow_list, name='borrow_list'),
    path('borrow/issue/', issue_book, name='issue_book'),
    path('borrow/return/<int:id>/', return_book, name='return_book'),

    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api/books/', BookAPI.as_view(), name='book_api'),
    path('api/books/<int:id>/', BookDetailAPI.as_view(), name='book_detail_api'),
    path(
    'api/members/', MemberAPI.as_view(), name='member_api'),
    path('api/members/<int:id>/',MemberDetailAPI.as_view(), name='member_detail_api'),
    path('api/borrows/',BorrowAPI.as_view(),name='borrow_api'),
    path('api/borrows/<int:id>/',BorrowDetailAPI.as_view(),name='borrow_detail_api'),
    path('api/borrows/<int:id>/return/',ReturnBookAPI.as_view(),name='return_book_api'),
]