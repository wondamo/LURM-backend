from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token

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

def format_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f'{instance.courseId}.{ext}'


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def tokens(self):
        token = Token.objects.get_or_create(user=self)
        return token[0].key

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

class PastQuestion(models.Model):
    courseId = models.CharField(max_length=25, primary_key=True)
    courseCode = models.CharField(max_length=6)
    semester = models.CharField(choices=semesterChoices, max_length=5)
    session = models.CharField(max_length=10)
    level = models.CharField(max_length=3, choices=levelChoices)
    questionFile = models.FileField(upload_to=format_filename)

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