from rest_framework import serializers
from .models import registrationmodel
from django.contrib.auth.models import User

class livepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrationmodel
        fields =  [
                   'memberSponserId',
                   'firstName',
                   'email',
                   'gender',
                   'fatherName',
                   'dob',
                   'adharCardNumber',
                   'penCardNumber',
                   'phoneNumber',
                   'address',
                   'city',
                   'state',
                   'zipCode',
                   'nomineName',
                   'nominegender',
                   'nominedob',
                   'nominePhoneNumber',
                   'bankAccountNumber',
                   'bankAccountHolder',
                   'bankName',
                   'ifscCode',
                   'branchName',
                   'dateTimeCreated',
                   'password',
                   'sponserId',
                   ]
        # fields = '_all_'



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# # Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
