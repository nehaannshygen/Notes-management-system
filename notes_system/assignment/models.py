from django.db import models

# Create your models here.
class assignment_details(models.Model):
    registration = models.CharField(max_length=100,default=False)
    class_code = models.CharField(max_length=100)
    year= models.CharField(max_length=100)
    instructions= models.CharField(max_length=100)
    upload= models.FileField(upload_to='files',default='no file')
    # this is useful in admin
    

    def __str__(self):
        return f'{self.class_code} {self.year}'
    

class assignment_answer(models.Model):
    student_registration = models.CharField(max_length=100)
    class_code = models.CharField(max_length=100)
    upload_answer=models.FileField(upload_to='files/',default='no file')

    def __str__(self):
        return f'{self.student_registration}'


