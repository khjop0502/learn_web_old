from rest_framework import serializers
from .models import User

#임시임 수정해야됨
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'