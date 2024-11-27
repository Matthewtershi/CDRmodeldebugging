from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    """ since django uses ORM format, we can define 
        the Postgre SQL DB fields with python first 
        and let django take care of the conversion """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    """ one to many for user to notes
        foreign key linked user to a single key
        ondelete param just means when the user is deleted, all associated objects are also deleted """

    def __str__(self):
        return self.title
    
class Graph(models.Model):

    number = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="graph")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

