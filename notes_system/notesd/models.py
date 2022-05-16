from django.db import models

# Create your models here.
'''
class notes_table(models.Model):
    coursecode= models.CharField(max_length=100)
    coursename= models.CharField(max_length=100)
    topicname= models.CharField(max_length=100)
    notesfile= models.FileField(upload_to='files')
    
   
    # this is useful in admin
    def __str__(self):
        return f'{self.coursecode} {self.coursename}'
'''
