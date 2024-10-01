from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
class Contact(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('contact', 'Contact'),
        ('bug_report', 'Remontée de bug'),
    ]
    email = models.EmailField(validators=[EmailValidator()])
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.request_type}'
