from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

#------------HOME PAGE---------------
class Service(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    icon=models.ImageField(upload_to="products/",blank=True,null=True)

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='team/')

    def __str__(self):
        return f"{self.name}({self.duration})"
    
class About(models.Model):
    duration=models.CharField(max_length=100)
    name=models.CharField(max_length=200)
    description=models.TextField()
    photo=models.ImageField(upload_to="about/")

    
class Achievement(models.Model):
    image=models.ImageField(upload_to="achievements/",blank=True,null=True)

    def __str__(self):
        return f"Achievement{self.id}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
#----------------CAREERS----------------
class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE, related_name="applications")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application: {self.name} for {self.job.title}"
    
#----------------NOTICES----------------
class Notice(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
#---------------CERTIFICATIONS-----------
class Certification(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="certificates/")

    def __str__(self):
        return self.name
    
#---------------PATENTS-----------------
class Patent(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    document=models.FileField(upload_to="patents/",blank=True,null=True)

    def __str__(self):
        return self.name
    
#-------------ABOUT US-----------------
class Founder(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    bio=models.TextField(max_length=200)
    photo=models.ImageField(upload_to="founders/")

    def __str__(self):
        return self.name
    
class CoreTeam(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    bio=models.TextField(max_length=200)
    photo=models.ImageField(upload_to="core_team/")

    def __str__(self):
        return self.name
    
class TechTeam(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    bio=models.TextField(max_length=200)
    photo=models.ImageField(upload_to="tech_team/")

    def __str__(self):
        return self.name
    
