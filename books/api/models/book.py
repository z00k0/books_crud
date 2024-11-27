from django.db import models

from .common import TimeStampMixin


class Book(TimeStampMixin):
    title = models.CharField("Название", max_length=255)
    author = models.CharField("Автор", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
