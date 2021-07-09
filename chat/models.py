from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=50, blank=False)
    is_logged_in = models.BooleanField(default=False)


class Message(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="to_user")
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="from_user")
    text = models.CharField(max_length=500, blank=False)
    time = models.DateTimeField(blank=False, auto_now_add=True)