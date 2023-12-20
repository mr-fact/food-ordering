from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'email',
            'password',
            'first_name',
            'last_name',
        ]
        extra_kwargs = {
            'phone': {'required': False},
            'password': {'write_only': True, 'required': False},
        }

    def validate(self, attrs):
        request = self.context.get('request')
        if request.method == 'POST':
            errors = {}
            if not attrs.get('phone', False):
                errors['phone'] = 'This field is required.'
            if not attrs.get('password', False):
                errors['password'] = 'This field is required.'
            if len(errors) != 0:
                raise serializers.ValidationError(errors)
        return super().validate(attrs)

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError('set minimum 8 charactors')
        return password

    def save(self, **kwargs):
        if self.validated_data.get('password', False):
            self.validated_data['password'] = make_password(self.validated_data['password'])
        return super().save(**kwargs)
