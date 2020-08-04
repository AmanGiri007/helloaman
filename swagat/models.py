from django.db import models

# Create your models here.
class List(models.Model):
    list_item=models.CharField(max_length=200,null=True)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.list_item}"
    