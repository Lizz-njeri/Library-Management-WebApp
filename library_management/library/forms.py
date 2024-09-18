# library/forms.py
from django import forms
from .models import Book, Member, Transaction

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'quantity']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone_number', 'membership_date', 'outstanding_debt']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'member', 'issue_date', 'rent_fee']