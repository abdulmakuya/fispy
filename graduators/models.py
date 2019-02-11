from django.db import models

# Create your models here.
class graduator(models.Model):
    #memberid==pk
    FullName = models.CharField(max_length=20,null=True)
    PersonalDescription = models.TextField(max_length=200,null=True)
    age = models.CharField(max_length=20,null=True)
    image = models.FileField(max_length=200,null=True)
    email = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    adress = models.CharField(max_length=30,null=True)
    HighestEducation=models.CharField(max_length=30,null=True)
    graduationYear = models.CharField(max_length=30,null=True)
    Employed = models.BooleanField(default=False)
    #skills in form of tags
    #

    #string representation of the models
    def  __str__(self):
        return self.FullName
        #return self.FirstName + ' - ' + self.LastName

class portfolio(models.Model):
    #'Memberid==fk
    graduator = models.ForeignKey(graduator, on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length=100,null=True)
    projectDescription = models.TextField(max_length=200,null=True)
    projectScreenshot = models.CharField(max_length=200,null=True)
    projectlink = models.CharField(max_length=200,null=True)
    certificationImage = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.projectTitle

class internshipExperience(models.Model):
    graduator = models.ForeignKey(graduator, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    roles = models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.institution
