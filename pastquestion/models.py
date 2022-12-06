from django.db import models

semesterChoices = (
    ('Alpha', 'Alpha'),
    ('Omega', 'Omega'),
)

levelChoices = (
    ('100','100'),
    ('200','200'),
    ('300','300'),
    ('400','400'),
    ('500','500'),
)

# Create your models here.
class PastQuestion(models.Model):
    courseCode = models.CharField(max_length=6, primary_key=True)
    semester = models.CharField(choices=semesterChoices, max_length=5)
    session = models.CharField(max_length=10)
    level = models.CharField(max_length=3, choices=levelChoices)
    questionFile = models.FileField(upload_to='')

    REQUIRED_FIELDS=['courseCode','semester','session','level','questionFile']

    def __str__(self):
        return self.courseCode