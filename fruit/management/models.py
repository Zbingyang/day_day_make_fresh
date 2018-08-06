from django.db import models

class User_admin(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table = 'user_admin'
