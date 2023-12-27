# account/serializers.py

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Define the serializer's metadata, including the model and fields to include.
        model = User
        fields = [
            'phone',
            'email',
            'password',
            'first_name',
            'last_name',
        ]
        # Additional options for customizing field behavior.
        extra_kwargs = {
            'phone': {'required': False},
            'password': {'write_only': True, 'required': False},
        }

    def validate(self, attrs):
        # Validate the incoming data before it is processed.
        request = self.context.get('request')
        if request.method == 'POST':
            errors = {}
            # Check if phone and password are present during a POST request.
            if not attrs.get('phone', False):
                errors['phone'] = 'This field is required.'
            if not attrs.get('password', False):
                errors['password'] = 'This field is required.'
            if len(errors) != 0:
                raise serializers.ValidationError(errors)
        return super().validate(attrs)

    def validate_password(self, password):
        # Validate the password length.
        if len(password) < 8:
            raise serializers.ValidationError('set minimum 8 charactors')
        return password

    def save(self, **kwargs):
        # Save method to handle any additional processing before saving.
        if self.validated_data.get('password', False):
            self.validated_data['password'] = make_password(self.validated_data['password'])
        return super().save(**kwargs)
