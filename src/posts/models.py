from re import M
from django.urls import reverse  
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

import datetime

from django.core.validators import MaxValueValidator, MinValueValidator # ajout rating stars

User = get_user_model() #liée au champ author

class BookPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre du livre")
    book_author = models.CharField(max_length=255, verbose_name="Nom de l'auteur")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name="Terminé le ")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Résumé")
    thumbnail = models.ImageField(blank=True, upload_to="book", verbose_name="Image")
    score = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)], verbose_name="Note")

    class Meta :
        ordering = ['-created_on']
        verbose_name = "Livre"

    def __str__(self):
        return (self.title)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        return ("Auteur inconnu")

    def get_absolute_url(self):
        return reverse("posts:home") #ici, "posts" a été nommé dans urls.py, dans l'app_name
