import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=True)
