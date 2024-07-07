from django.db import models

# Create your models here.

class userInfo(models.Model):
    name = models.CharField(max_length=300)
    image =  models.ImageField(upload_to='user_info_image/')


class Experience(models.Model):
    p_year = models.CharField(max_length=300)
    sc = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    det = models.TextField()

    class Meta:
       verbose_name_plural = 'Experience' 

    def __str__(self):
        return self.p_year

class ContactInfo(models.Model):
    Name = models.CharField(max_length=300)
    Email = models.EmailField()
    Phone = models.CharField(max_length=400)
    Message = models.TextField()

    class Meta:
       verbose_name_plural = ("Contact-Infos") 

    def __str__(self):
        return self.Name





