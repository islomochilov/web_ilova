from rest_framework import serializers
from .models import Yangiliklar, Kitob


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'



class KitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob
        fields = '__all__'
