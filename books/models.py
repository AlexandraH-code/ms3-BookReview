from django.db import models
from django.contrib.auth.models import User

# STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) # Connection to the user
    is_draft = models.BooleanField(default=True) # For admin draft
    # is_draft = models.IntegerField(choices=STATUS, default=0) - uncomment this line + STATUS and comment out the line above

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    
    def __str__(self):
        return self.title  


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) # Only admin can approve

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating}/5)"
    

class AboutPage(models.Model):
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About the website"

