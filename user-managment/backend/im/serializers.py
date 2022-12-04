from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'





class UserSerializer(serializers.ModelSerializer):
    profile = UserProfile(many=False)

    #
    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        user_profile_data = data.pop('profile')
        for key, value in user_profile_data.items():
            data.update({key:value})
        return data

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_active", "is_staff", "password", "profile"]

        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            validated_data['is_active'] = True
            validated_data['is_staff'] = True
            user = User.objects.create(**validated_data)
            return user

