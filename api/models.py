from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Tanlov(models.Model):
    title = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.title

class QA(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question[:50]


class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.fullname


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question



