from django.conf import settings

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#we defing obects called models
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(default='Your default content value here')
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def _str_(self):
         return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    


# class POST(models.Model):

#     title=models.CharField(max_length=200)
#     comment=models.TextField(default='Your default content value here')
#     date_posted=models.DateTimeField(default=timezone.now)
#     author=models.ForeignKey(User,on_delete=models.CASCADE)
    
#     def _str_(self):
#          return self.title







    # def publish(self):
    #     self.published_date=timezone.now()
    #     self.save()

    # def _str_(self):
    #     return self.title
    


#     from django.conf import settings

# from django.db import models
# from django.utils import timezone
# # Create your models here.


# #we defing obects called models
# class Post(models.Model):
#     author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     title=models.CharField(max_length=200)
#     title=models.TextField()
#     created_date=models.DateTimeField(default=timezone.now)
#     published_date=models.DateTimeField(blank=True,null=True)

#     def publish(self):
#         self.published_date=timezone.now()
#         self.save()

#     def _str_(self):
#         return self.title