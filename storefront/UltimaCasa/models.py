from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.conf import settings
from .managers import CustomUserManager
from django.utils import timezone




class Role(models.Model):
    naam = models.CharField(max_length=50)
    waarde = models.IntegerField()
    landingspagina = models.CharField(max_length=50)
    

    def __str__(self):
        return self.naam
    

class Gebruiker(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, default=1)
        
    USERNAME_FIELD = "email"

    objects = CustomUserManager()
# class CustomUser(AbstractUser):
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Home(models.Model):
    datum = models.DateField(null=True)
    user = models.ForeignKey(Gebruiker, on_delete=models.CASCADE, null=True)
    straat = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    plaats = models.CharField(max_length=50)
    gewijzigd = models.DateTimeField(null=True)

    def __str__(self):
        return self.straat

class status(models.Model):
    statuscode = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status
    
class Bieding(models.Model):
    datum = models.DateField()
    user = models.ForeignKey(Gebruiker, on_delete=models.CASCADE, null=True)
    house = models.ForeignKey(Home, on_delete=models.CASCADE, null=True)
    bod = models.IntegerField(null=True)
    status = models.ForeignKey(status, on_delete=models.CASCADE, null=True)
    statusdatum = models.DateField(null=True)

    def __str__(self):
        return self.house.straat
    
    