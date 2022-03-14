from django.db import models

# Create your models here.

class User(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)
    UserName = models.CharField(db_column='UserName', max_length=225)
    Email = models.CharField(db_column='Email', max_length=225)
    Password = models.CharField(db_column='Password', max_length=20)
    AuthentiationCode = models.CharField(db_column='AuthentiationCode', max_length=52)    
    RegisterDate = models.DateTimeField(db_column='RegisterDate',auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'User'


class SubscriptionPlan(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)
    SubscriptionName = models.CharField(db_column='AppName', max_length=225)
    Description = models.TextField(db_column='Description', default=None)       
    RegisterDate = models.DateTimeField(db_column='RegisterDate')

    class Meta:
        managed = True
        db_table = 'SubscriptionPlan'


class APP(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)
    UserId = models.ForeignKey('User', on_delete=models.CASCADE, db_column='UserId')    
    AppName = models.CharField(db_column='AppName', max_length=225)
    Description = models.TextField(db_column='Description', default=None)  
    SubscriptionName = models.CharField(db_column='SubscriptionName', max_length=225,default='Free')
    SubscriptionPrice = models.FloatField(db_column='SubscriptionPrice', default=0)
    active = models.CharField(db_column='active', max_length=225,default=True)    
    CreatedDate = models.DateTimeField(db_column='CreatedDate')
    EndDate = models.DateTimeField(db_column='EndDate')

    class Meta:
        managed = True
        db_table = 'APP'


