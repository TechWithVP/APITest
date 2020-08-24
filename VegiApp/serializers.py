from rest_framework import serializers
from VegiApp.models import VegiFruits, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('catName', 'catDescription')
        fields = ('userId', 'userFName', 'userMName', 'userLName', 'userEmail')
        # fields = '__all__'

class VegiFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VegiFruits
        # fields = '__all__'
        # fields = ('vegifruitName', 'vegifruitDescription', 'vegifruitImage', 'vegifruitMarketPrice', 'vegifruitOurPrice', 'vegifruitPricePerWeight', 'vegifruitTotalStock', 'catId')
        fields = ('vegifruitId', 'vegifruitName', 'vegifruitDescription', 'vegifruitImage', 'vegifruitMarketPrice', 'vegifruitOurPrice', 'vegifruitPricePerWeight', 'vegifruitTotalStock', 'catId')

class APILoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'userEmail', 'userPassword', 'userDeletionStatus', 'userRole')