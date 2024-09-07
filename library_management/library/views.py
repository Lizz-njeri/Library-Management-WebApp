from django.shortcuts import render, redirect
from .models import Book, Member, Transaction
from datetime import datetime

def index(request):
    return render(request, 'library/index.html')

def manage_books(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        stock = request.POST['stock']
        Book.objects.create(title=title, author=author, stock=stock)
        return redirect('manage_books')
    
    books = Book.objects.all()
    return render(request, 'library/books.html', {'books': books})

def manage_members(request):
    if request.method == 'POST':
        name = request.POST['name']
        Member.objects.create(name=name)
        return redirect('manage_members')

    members = Member.objects.all()
    return render(request, 'library/members.html', {'members': members})

def manage_transactions(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        member_id = request.POST['member_id']
        action = request.POST['action']

        book = Book.objects.get(id=book_id)
        member = Member.objects.get(id=member_id)

        if action == 'issue':
            if book.stock > 0:
                Transaction.objects.create(book=book, member=member)
                book.stock -= 1
                book.save()
            else:
                return render(request, 'library/transactions.html', {'error': 'Book out of stock'})

        elif action == 'return':
            transaction = Transaction.objects.filter(book=book, member=member, is_returned=False).first()
            if transaction:
                transaction.return_date = datetime.now()
                transaction.is_returned = True
                rent_fee = 100.00  # Example rent fee
                transaction.fee = rent_fee
                transaction.save()
                member.outstanding_debt += rent_fee
                member.save()
                book.stock += 1
                book.save()

        return redirect('manage_transactions')

    transactions = Transaction.objects.all()
    books = Book.objects.all()
    members = Member.objects.all()
    return render(request, 'library/transactions.html', {'transactions': transactions, 'books': books, 'members': members})

def search_books(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        results = Book.objects.filter(title__icontains=search_term) | Book.objects.filter(author__icontains=search_term)
        return render(request, 'library/search.html', {'results': results})

    return render(request, 'library/search.html')
