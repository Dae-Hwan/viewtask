from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    age = models.IntegerField(default = 0)
	
    def __str__(self):
        return self.owner

    class Meta():	
        db_table = 'owner'

class Dog(models.Model):
    owner = models.ForeignKey('owner', on_delete = models.CASCADE)
    name = models.CharField(max_length = 45)
    age = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.dog

    class Meta():
        db_table = 'dog'
    
        
	
