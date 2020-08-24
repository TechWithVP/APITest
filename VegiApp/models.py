from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userFName = models.CharField(max_length = 25, default = "")
    userMName = models.CharField(max_length = 25, default = "")
    userLName = models.CharField(max_length = 25, default = "")
    userHeight = models.CharField(max_length = 5, default = "")
    userWeight = models.CharField(max_length = 5, default = "")
    userPasswordSecret = models.CharField(max_length = 16, default = "")
    userAadhar = models.CharField(max_length = 16, default = "0000 0000 0000 0000")
    userState = models.CharField(max_length = 25, default = "")
    userCity = models.CharField(max_length = 25, default = "")
    userArea = models.CharField(max_length = 25, default = "")
    userAddress = models.CharField(max_length = 300, default = "")
    userMobileNumber = models.CharField(max_length = 10, default = "0123456789")
    userEmail = models.EmailField(max_length = 50, default = "example@gmail.com")
    userPassword = models.CharField(max_length = 300, default = "")
    userRole = models.CharField(max_length = 10, default = "ROLE_ADMIN")
    userImage = models.CharField(max_length = 300, default = "")
    userDeletionStatus = models.IntegerField(default = 0)
    whoAdded = models.IntegerField(default = 0)

class VFCategory(models.Model):
    catId = models.AutoField(primary_key=True)
    catName = models.CharField(max_length = 25, default = "")
    catDescription = models.CharField(max_length = 200, default = "")
    catStatus = models.IntegerField(default = 0)

class VegiFruits(models.Model):
    vegifruitId = models.AutoField(primary_key=True)
    vegifruitName = models.CharField(max_length = 25, default = "")
    vegifruitDescription = models.CharField(max_length = 200, default = "")
    vegifruitImage = models.CharField(max_length = 200, default = "")
    vegifruitSKU = models.CharField(max_length = 20, default = "SKU-1")
    vegifruitMarketPrice = models.FloatField(default = 0.0)
    vegifruitOurPrice = models.FloatField(default = 0.0)
    vegifruitPricePerWeight = models.FloatField(default = 0.0)
    catId = models.IntegerField(default = 1)
    vegifruitTotalStock = models.FloatField(default = 1)
    vegifruitStatus = models.IntegerField(default = 0)

class AuthTokens(models.Model):
    tokenId = models.AutoField(primary_key = True)
    tokenAuth = models.CharField(max_length = 128, default = "kdkfjdkkfjkjdfkjfk")
    userId = models.IntegerField()