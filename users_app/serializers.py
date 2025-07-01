from rest_framework import serializers
from .models import User
from .models import BikerApplication, SupportIssue

class UserRegisterSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'confirmPassword', 'joined_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user

from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'




class BikerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikerApplication
        fields = '__all__'
        read_only_fields = ['status', 'submitted_at', 'reviewed_at']


class SupportIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportIssue
        fields = '__all__'
       
