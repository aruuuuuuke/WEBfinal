from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.word} - {self.translation}"


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    worlds = models.ManyToManyField(Word, related_name='lessons')

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    teacher = models.TextField(max_length=200)
    lessons = models.ManyToManyField(Lesson, related_name='groups')

    def __str__(self):
        return self.name
