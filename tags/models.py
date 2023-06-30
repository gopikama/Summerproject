from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tags(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag=models.ForeignKey(Tags,on_delete=models.CASCADE)
    #type and ID requied for creating a generic item to which this tag is applied to
    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()

