from rest_framework import serializers
from .models import User

'''  authentication serializer  '''


class AuthSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=15, min_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, min_length=8, write_only=True)

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


def validate(self, attrs):

    """
    create serializer  validation  for messages
    :para args : return get dictionary attributes to be set on the rendered
    return : serializer validation
    """

    email = attrs.get('email', '')
    username = attrs.get('username', '')
    first_name = attrs.get('first_name', '')
    last_name = attrs.get('last_name', '')

    if not first_name.ischar():
        raise serializers.ValidationError('first_name must contain characters')
    if not last_name.ischar():
        raise serializers.ValidationError('last_name also have characters only ')
    if not username.isalnum():
        raise serializers.ValidationError('Username should contain only alphanumeric characters')
    return attrs


def create(self, validated_data, *args, **kwargs):

    """
    :param self:
    :param validated_data:
    :param args: null
    :param kwargs: null
    :return: save data after convert is json  create user using return instance,
             given the validated data
    """
    return User.objects.create(**validated_data)
        



