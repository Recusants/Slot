from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True, blank=True)




# ===================
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class AbstractPerson(models.Model):
# 	first_name = models.CharField(max_length=255)
# 	last_name = models.CharField(max_length=255)
# 	email = models.EmailField(unique=True)


# 	class Meta:
# 		abstract = True

# class User(AbstractUser):
# 	phone_number = models.CharField(max_length=20, blank=True)
# 	is_barber_shop = models.BooleanField(default=True)
# 	is_admin = models.BooleanField(default=True)
# 	is_client = models.BooleanField(default=True)

# 	class Meta:
# 		abstract = True

# class Adminstrator(AbstractPerson, User):
# 	rating = models.CharField(max_length=30)
# 	class Meta:
# 		proxy = True

# class Barber(AbstractPerson, User):
# 	barber_shop = models.ForeignKey('BarberShop', on_delete=models.DO_NOTHING)
# 	availability = models.BooleanField(default=False)
# 	rating = models.CharField(max_length=30)
# 	beginning_year = models.DateField()

# 	class Meta:
# 		proxy = True

# class BarberShop(AbstractPerson, User):
# 	name = models.CharField(max_length=255)
# 	street = models.CharField(max_length=255)
# 	exact = models.CharField(max_length=255)
# 	coordinates = models.CharField(max_length=255)
# 	expiration_date = models.DateTimeField()

# 	opening_hours = models.CharField(max_length=30)
# 	clossing_hours = models.CharField(max_length=30)
# 	call = models.CharField(max_length=30)
# 	whatsapp = models.CharField(max_length=30)
# 	sms = models.CharField(max_length=30)

# 	class Meta:
# 		proxy = True


# class Client(Account):
# 	rating = models.CharField(max_length=30)


