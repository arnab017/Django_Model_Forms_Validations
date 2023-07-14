from django.db import models
from django import forms
# Create your models here.

#* Form Validations
def validate_start_with_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('Name should not start with a') 
    
def validate_length(value):
    if len(value) <= 3:
        raise forms.ValidationError('Too short')


#* Model Classes
class Topic(models.Model):
    topic_name = models.CharField(max_length=20, primary_key=True, validators=[validate_start_with_a])
    
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, primary_key=True, validators=[validate_length])
    url = models.URLField()
    
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=20)
    
    def __str__(self):
        return self.author