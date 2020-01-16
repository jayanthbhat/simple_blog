from django.db import models
import uuid
import os
# Create your models here.

# Getting Unique Image Path
def get_images_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/blog_image', filename)

class Posts(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to=get_images_path,blank=True,null=True)
    

    def __str__(self):
        return self.title