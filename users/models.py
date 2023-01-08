from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username.capitalize()} Profile'

    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) #Profile.save() got multiple values for argument 'force_insert'
        img = Image.open(self.image.path) #grabs the image that was saved

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) #sends the resized image back to the path