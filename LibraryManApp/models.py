from django.db import models

class reader(models.Model):
    reader_name = models.CharField(max_length = 200)
    reader_contact = models.CharField(max_length = 200)
    reader_id = models.CharField(max_length = 200)
    reader_address = models.CharField(max_length = 200)
    reader_name = models.TextField()
    active = models.BooleanField(default=True)



    