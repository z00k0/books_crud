import csv

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api.models import Book
from api.serializers import BookSerializer


@extend_schema(tags=["Книги"])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="books.csv"'
        writer = csv.writer(response, delimiter=";")
        writer.writerow(
            ["id", "title", "author", "description", "isbn", "created_at", "updated_at"]
        )
        for book in queryset:
            writer.writerow(
                [
                    book.id,
                    book.title,
                    book.author,
                    book.description,
                    book.isbn,
                    book.created_at,
                    book.updated_at,
                ]
            )

        return response
