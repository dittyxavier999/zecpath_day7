from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer used to register a new user.

    Public registration always creates a CANDIDATE.
    Users cannot choose their own role.
    """

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    password2 = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        """
        Make sure both passwords match.
        """

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({
                "password": "Passwords do not match."
            })

        return attrs

    def create(self, validated_data):
        """
        Create a new public user.

        Public registration always creates a CANDIDATE.
        The client cannot choose ADMIN or EMPLOYER.
        """

        validated_data.pop("password2")

        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            role="CANDIDATE",
            **validated_data
        )

        return user