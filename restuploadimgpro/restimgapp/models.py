from django.db import models


class Student(models.Model):
    sname =models.CharField(max_length=20)
    image=models.ImageField(upload_to='images',default='images/None/No-img.jpg')
    profile=models.FileField(upload_to='files',default='fies/None/No-file.pdf')
    task=models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.sname
