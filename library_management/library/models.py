# library/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    outstanding_debt = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def can_borrow(self):
        return self.outstanding_debt <= 500

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def clean(self):
        if self.book.quantity <= 0:
            raise ValidationError("This book is out of stock.")
        if not self.member.can_borrow():
            raise ValidationError("Member has outstanding debt exceeding KES 500.")

    def save(self, *args, **kwargs):
        if not self.pk:  # New transaction
            self.clean()
            self.book.quantity -= 1
            self.book.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"