from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class TestModel(models.Model):
    class Meta(object):
        db_table = 'testmodel'

    name = models.CharField(
        'Name', max_length=200
    )

    image = CloudinaryField(
        'image', default=""
    )

    def __str__(self):
        return self.name
