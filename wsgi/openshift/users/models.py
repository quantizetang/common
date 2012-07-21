from django.db import models

class users(models.Model):
    user_name  = models.CharField('username', max_length=200)
    user_description  = models.CharField('userdesc', max_length=100)
    
    def __str__(self):
        return '%s' % (self.username)