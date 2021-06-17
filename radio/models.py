from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date


class Show(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    show_name = models.CharField(max_length=250)
    show_logo = models.FileField()
    category = models.CharField(max_length=50, default='Education')
    favorite = models.ManyToManyField(User, related_name='show_favorite')

    def __str__(self):
        return self.show_name + ' - ' + self.artist.username
    
    def total_favorite(self):
        return self.favorite.count()
    
    def get_absolute_url(self):
        return reverse('radio:detail', kwargs={'pk': self.pk})


class Audio(models.Model):
    show = models.ForeignKey(Show, related_name='audios', on_delete=models.CASCADE)
    file_title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)
    post_date = models.DateField(auto_now_add=True)
    favorite = models.ManyToManyField(User, related_name='audio_favorite')

    def __str__(self):
        return self.file_title
    
    def total_favorite(self):
        return self.favorite.count()

    def get_absolute_url(self):
        return reverse('radio:detail', kwargs={'pk' : self.show.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('radio:index')









