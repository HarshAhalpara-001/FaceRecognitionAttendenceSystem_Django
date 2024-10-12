from django.db import models

class StudentImage(models.Model):
    class_name = models.CharField(max_length=10)
    division = models.CharField(max_length=1)
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.class_name} {self.division} - {self.roll_no}: {self.name}"
