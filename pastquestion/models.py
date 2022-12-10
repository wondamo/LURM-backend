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
    courseId = models.CharField(max_length=25, primary_key=True)
    courseCode = models.CharField(max_length=6)
    semester = models.CharField(choices=semesterChoices, max_length=5)
    session = models.CharField(max_length=10)
    level = models.CharField(max_length=3, choices=levelChoices)
    questionFile = models.FileField(upload_to='lurm/')

    REQUIRED_FIELDS=['courseCode','semester','session','level','questionFile']

    def __str__(self):
        return self.courseCode

    def slugify_courseId(self):
        beg = self.courseCode
        mid = self.semester[:3]
        end = self.session
        return f"{beg}_{mid}_{end[:4]}_{end[5:]}_PQ"

    def save(self, *args, **kwargs):
        self.courseId = self.slugify_courseId()
        super(PastQuestion, self).save(*args, **kwargs)