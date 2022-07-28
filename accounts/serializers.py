from rest_framework import fields, serializers
# from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email']#,
            # username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    def update(self, instance, validated_data):
        pass


    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            # raise exceptions.ValidationError(msg)
            raise ValueError('Must include "email" and "password".')

        return user


    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _(
                'Must include "username or "email" or "phone number" and "password".'
            )
            # raise exceptions.ValidationError(msg)
            
            raise ValueError('Must include "username or "email" or "phone number" and "password".')

        return user


    """

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except AuthUser.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
        
    """

"""
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
            'email',
            'role'
        )

"""
