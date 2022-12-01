from rest_framework import serializers
from .models import Client, Tag, MobileCode


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
        
        
class MobileCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCode
        fields = ['code']


class ClientSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    mobile_code = MobileCodeSerializer()
    
    class Meta:
        model = Client
        fields = ['phone_number', 'mobile_code', 'tag', 'time_zone']
        
    def update(self, instance, validated_data):
        instance.email = validated_data.get('phone_number', instance.email)
        instance.content = validated_data.get('mobile_code', instance.content)
        instance.created = validated_data.get('tag', instance.created)
        instance.email = validated_data.get('time_zone', instance.email)
        return instance