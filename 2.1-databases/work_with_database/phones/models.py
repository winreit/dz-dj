from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, unique=True)
    # TODO: Добавьте требуемые поля

