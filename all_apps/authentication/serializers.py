from rest_framework import serializers
from .models import CustomUser, Farmer

# Think of Serializer as a smart assistant that:
# ✅ Receives form/API data
# ✅ Checks if data is valid
# ✅ Converts data into Python format
# ✅ Creates database objects
# ✅ Updates database objects
# ✅ Generates JSON responses from model objects

class registerAPI_Serializer(serializers.ModelSerializer): # is a bridge b/w model & JSON

    class Meta:                                       # Meta is configuration for serializer
        model = CustomUser                            # This serialzer work with CustomUser
        fields = ['username', 'email', 'password', 'role']  # and these fields
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):         # its a method in DRF validate_<field_name>()
        if CustomUser.objects.filter(username=value).exists():        # we can use it for validations
            raise serializers.ValidationError("Username Already Exists!") # for email, username, etc
        return value                                                # value is value of dict that 
                                                                    # user submitted

    def create(self, validated_data):                     # is a DRF special method, it execute
        user = CustomUser.objects.create_user(            # when we call serializer.save()
            username=validated_data['username'], email=validated_data['email'],
            password=validated_data['password'], role=validated_data['role']
        )

        if user.role == 'farmer':
             Farmer.objects.create(user=user)

        return user

    # validated_data is a secure Python dictionary containing cleaned, verified input that has been 
    # converted into native Python datatypes and is ready to be safely saved to your database.


class UpdateUserAPI_Serializer(serializers.ModelSerializer):

    # Include farmer fields explicitly
    age = serializers.IntegerField(required=False)
    profile_image = serializers.ImageField(required=False)
    aadhaar = serializers.CharField(required=False)
    district = serializers.CharField(required=False)
    region = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    panchayath = serializers.CharField(required=False)
    farm_size = serializers.DecimalField(max_digits=7, decimal_places=2, required=False)
    farm_type = serializers.CharField(required=False)
    soil_type = serializers.CharField(required=False)
    soil_card = serializers.ImageField(required=False)

    username = serializers.CharField(required=False,allow_blank=True)
    password = serializers.CharField(required=False,allow_blank=True,write_only=True)
    email = serializers.EmailField(required=False,allow_blank=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number',
                  'age', 'profile_image', 'aadhaar', 'district', 'region',
                  'address', 'panchayath', 'farm_size', 'farm_type',
                  'soil_type', 'soil_card']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):   # If the user not upadte 'username' | DRF raise 
                                        # multiple user with same 'username'
        user = self.instance            # To prevent use validate_username

        if CustomUser.objects.exclude(id=user.id).filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        
        return value

    def update(self, instance, validated_data):
    
                # updating details of CustomUser model
                if 'username' in validated_data:
                    instance.username = validated_data['username']
                if 'email' in validated_data:
                    instance.email = validated_data['email']
                if 'password' in validated_data and validated_data['password']:
                    instance.set_password(validated_data['password'])
                if 'phone_number' in validated_data:
                    instance.phone_number = validated_data['phone_number']
                instance.save()
    
                # updating details of Farmer model
                farmer = Farmer.objects.get(user=instance)
                farmer.age = validated_data.get('age', farmer.age)
                farmer.profile_image = validated_data.get('profile_image', farmer.profile_image)
                farmer.aadhaar = validated_data.get('aadhaar', farmer.aadhaar)
                farmer.district = validated_data.get('district', farmer.district)
                farmer.region = validated_data.get('region', farmer.region)
                farmer.address = validated_data.get('address', farmer.address)
                farmer.panchayath = validated_data.get('panchayath', farmer.panchayath)
                farmer.farm_size = validated_data.get('farm_size', farmer.farm_size)
                farmer.farm_type = validated_data.get('farm_type', farmer.farm_type)
                farmer.soil_type = validated_data.get('soil_type', farmer.soil_type)
                farmer.soil_card = validated_data.get('soil_card', farmer.soil_card)
                farmer.save()
    
                return instance