from django.db import models
from django.contrib.auth.models import AbstractUser



class UserAccount(AbstractUser):
    """
        | Field        | Details    |
        | :---------   | :--------  |
        | username     | unique     |
        | first_name   | 150 chars  |
        | last_name    | 150 chars  |
        | email        | email      |
        | picture      | image      |
        | bio          | text       |
        | password     | 128 chars  |
        | isNew        | bool       |
        | school       | 150 chars  |
        | occupation   | 150 chars  |
    """

    CHOICES = [(1, 'True'), (2, 'False')]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='images/', max_length=100)
    bio = models.TextField(null=True, blank=True)
    isNew = models.BooleanField(choices=CHOICES, default=1)
    school = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)

    def __str__(self):
        return self.username
