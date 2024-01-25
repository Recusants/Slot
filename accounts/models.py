from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
	ROLES = {
		('Cashier','Cashier'),
		('Pharmacist','Pharmacist'),
		('Data Analist','Data Analist'),

		('Pharmacist, Cashier','Pharmacist, Cashier'),
		('Data Analist, Cashier','Data Analist, Cashier'),

		('Data Analist, Pharmacist','Data Analist, Pharmacist'),

		('Data Analist, Pharmacist, Cashier','Data Analist, Pharmacist, Cashier'),
	}
	phone_number = models.CharField(max_length=30)
	address = models.TextField(max_length=255)
	roles = models.CharField(max_length=1000)
	#profile_picture = models.ImageField(blank=True, upload_to='images/staff')
	created_by = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	deleted = models.BooleanField(default=False)


class MedicalScheme(models.Model):
	company_name = models.CharField(max_length=30)
	registration_number = models.CharField(max_length=100, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)
	address = models.TextField(max_length=255, blank=True, null=True)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)
	deleted = models.BooleanField(default=False)
