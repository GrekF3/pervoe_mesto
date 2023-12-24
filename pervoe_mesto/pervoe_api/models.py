from django.db import models

class Apartment(models.Model):
    room_type = models.CharField(max_length=50)
    area = models.FloatField()
    image = models.ImageField(upload_to='apartment_images/')

    def __str__(self):
        return f"{self.room_type} - {self.area} м²"

