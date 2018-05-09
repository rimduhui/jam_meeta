from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Quiz(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    number = models.IntegerField(default=1, primary_key=True)
    title = models.CharField(max_length=100)
    question = models.TextField()

    first_exam = models.CharField(default=None, max_length=100)
    second_exam = models.CharField(default=None, max_length=100)
    third_exam = models.CharField(default=None, max_length=100)

    answer = models.IntegerField(default=1, validators=[MaxValueValidator(3), MinValueValidator(1)])

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title