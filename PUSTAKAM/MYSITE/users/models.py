from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile, self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


class feedback(models.Model):
	First_Name = models.CharField(max_length=30)
	Last_Name = models.CharField(max_length=30)
	Age = models.IntegerField(default='0')
	Email = models.EmailField(max_length=50)
	Feedback = models.CharField(max_length=70)
	

