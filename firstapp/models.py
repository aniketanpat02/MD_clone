from django.db import models

# Create your models here.
class Center(models.Model):
    #code = models.IntegerField()
    code = models.IntegerField(null= False)
    short_name= models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    village =models.CharField(max_length=20)
    status_field = [
        (1, 'Active'),
        (2, 'Inactive'),
        (3, 'Deleted')
    ]
    status= models.IntegerField(max_length=1,choices=status_field,default=2)


    def __str__(self):
        return str(self.pk)

class Customer(models.Model):
    number = models.IntegerField(max_length=3)
    number_prefix = models.IntegerField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length = 10)
    Select_Gender=[
        (1,'Male'),
        (2,'Female')
    ]
    gender = models.IntegerField(choices=Select_Gender ,default=1)
    dob= models.DateTimeField()
    mobile = models.IntegerField()
    is_deleted= [
        (1,'Active'),
        (2,'Non Active'),
        (3,'deleted')
    ]
    status = models.IntegerField(choices=is_deleted,default=1)

    def __str__(self):
        return str(self.pk)


class Collection(models.Model):
    GENDER_CHOICES = [
        ('c', 'Cow'),
        ('b', 'buffalo'),
    ]
    date = models.DateTimeField()
    type = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Shift_Choice =[
        ('M','Morning'),
        ('E', 'Evening')
    ]
    shift = models.CharField(max_length=1, choices=Shift_Choice)
    quantity =  models.DecimalField(max_digits=3,decimal_places=2)
    snf = models.DecimalField(max_digits=4,decimal_places=2)
    fat = models.DecimalField(max_digits=4,decimal_places=2)
    rate = models.DecimalField(max_digits=4,decimal_places=2)
    is_deleted = [
        (1, 'Active'),
        (2, 'Non Active'),
        (3, 'deleted')
    ]
    status = models.IntegerField(choices=is_deleted, default=1)
    center = models.ForeignKey(Center,on_delete=models.CASCADE,related_name='centers',default=5)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE , related_name='customer', default =10)

    def __str__(self):
        return self.type






"""
"""






