from django.contrib import admin
from .models import Book, Review, AboutPage  # Import the models

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(AboutPage)
