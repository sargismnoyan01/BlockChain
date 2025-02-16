from rest_framework import serializers
from .models import *


class BlockModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['index','data']