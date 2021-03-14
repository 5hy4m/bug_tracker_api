from django.contrib.auth.models import User
from rest_framework import serializers
from bug_tracker.models import User_Activity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','password']
        extra_kwargs={"password":{"write_only":True}}

        def validate(self,data):
            username = data['username']
            users_names = User.objects.filter(username = username)
            if users_names.exists():
                raise ValidationError("This User is already Registerd")
            return data

        def create(self,validated_data):
            user_obj = User(
                username = validated_data['username'],
            )
            user_obj.set_password(validated_data['password'])
            user_obj.save()
            return validated_data

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Activity
        fields = '__all__'




