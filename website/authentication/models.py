from django.db import models

# Create your models here.
#class Login(models.Model):
#    username = models.CharField(max_length=50)
#    pswrd = models.CharField(max_length=30)

class Register(models.Model):
    Username = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)

class contact1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    Messages = models.CharField(max_length=500)

class User_Detail(models.Model):
    Patient_ID = models.CharField(max_length=200)
    Abnormal_short_term_variability = models.CharField(max_length=500)
    Percentage_of_time_with_ALTV = models.CharField(max_length=500)
    Mean_value_short_term = models.CharField(max_length=500)
    Histogram_mean = models.CharField(max_length=500)
    Prolongued_decelerations = models.CharField(max_length=500)
    Histogram_median = models.CharField(max_length=500)
    Accelerations = models.CharField(max_length=500)
    Histogram_mode = models.CharField(max_length=500)
    Mean_value_of_LTV = models.CharField(max_length=500)
    Histogram_min =models.CharField(max_length=500)
    
