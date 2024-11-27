from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", auto_now=True, editable=False
    )

    class Meta:
        abstract = True
