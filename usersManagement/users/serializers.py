from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    full_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)
    
class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)
    

