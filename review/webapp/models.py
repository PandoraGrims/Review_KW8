from django.db import models
from django.contrib.auth.models import User

category_choices = [("Category No. 1", "CategoryNo1"), ("Category No. 2", "CategoryNo2"),
                    ("Category No. 3", "CategoryNo3")]


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, null=False, blank=False, verbose_name="категория",
                                choices=category_choices,
                                default=category_choices[0][0])
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, max_length=200, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"{self.author.username} {self.product.name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
