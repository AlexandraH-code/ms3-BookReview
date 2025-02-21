from django.contrib import admin
from .models import Book, Review, AboutPage  # Import the models


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'approved')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Book)
admin.site.register(Review, ReviewAdmin)
admin.site.register(AboutPage)




