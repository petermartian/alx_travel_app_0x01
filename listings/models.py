from django.db import models
from django.conf import settings  



class Listing(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location    = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    available   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Meta:
    ordering = ['-created_at']



class Booking(models.Model):
    listing     = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='bookings')
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    start_date  = models.DateField()
    end_date    = models.DateField()
    guests      = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'start_date', 'end_date')
        ordering = ['-created_at']

    def __str__(self):
        return f'Booking by {self.user} for {self.listing}'

class Review(models.Model):
    listing     = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='reviews')
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating      = models.PositiveSmallIntegerField()  # e.g. 1–5
    comment     = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.user} – {self.rating}/5'


