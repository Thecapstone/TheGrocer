from rest_framework import serializers
from .models import CustomUser, GrocerProfile, BuyerProfile

class GrocerRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    user_type = serializers.CharField(source='user.user_type')
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = GrocerProfile
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'user_type',
            'brand_name',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = validated_data.pop('password')

        user = CustomUser.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            brand_name=user_data['brand_name'],
            is_staff=True,
            user_type='grocer'
        )
        user.set_password(password)
        user.save()
        return user

class GrocerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class BuyerRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.username')
    user_type = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = BuyerProfile
        fields = [
            'username', 
            'email', 
            'user_type', 
            'password', 
            'password2'
        ]
    
    def validate(self, attrs):
        if attrs['passsword2'] != attrs['password']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = validated_data.pop('password')

        user = CustomUser.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            user_type='buyer'
        )
        user.set_password(password)
        user.save()

        buyer = BuyerProfile.objects.create(
            user=user,
            **validated_data
        )
        return buyer


    