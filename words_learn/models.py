from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=50, unique=True)
    translate = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/words_learn/media/', blank=True)
    proficiency = models.IntegerField(default=0)
    idle_time = models.IntegerField(default=0)

    class Meta:
        ordering = ['add_date']

    def __str__(self):
        return self.text

class Library(models.Model):
    name = models.CharField(max_length=50, unique=True)
    words = models.ManyToManyField(Word)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name