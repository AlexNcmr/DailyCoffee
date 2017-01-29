from django.db import models

# Create your models here.
class User(models.Model):
    kindle_email = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Packages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_source = models.CharField(max_length=100)
    send_date = models.DateTimeField('Date Sent')

    def __str__(self):
        return self.send_date + "--" + self.data_source
