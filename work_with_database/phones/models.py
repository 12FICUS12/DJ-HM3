from django.db import models
from django.utils.text import slugify

class Phone(models.Model):

    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id};' \
               f'{self.name};' \
               f'{self.price};' \
               f'{self.image};' \
               f'{self.release_date};' \
               f'{self.lte_exists};' \
               f'{self.slug}'


