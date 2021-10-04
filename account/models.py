from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='images/default.jpg',upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.photo.path)

        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.photo.path)
