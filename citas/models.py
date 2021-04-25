from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

alpha_spaces = RegexValidator(r'^[a-zA-Z ]*$', 'Solo letras y espacios.')
num_only = RegexValidator(r'^[0-9 ]*$', 'Solo números permitidos.')

class Post(models.Model):
    email = models.EmailField(max_length=70, blank=False)
    name = models.CharField(max_length=50, blank=False, null=False, validators=[alpha_spaces])
    tel = models.CharField(max_length=50, blank=False, validators=[num_only])
    date = models.DateField(auto_now=False, auto_now_add=False)
    # convert time into charfield.
    time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
