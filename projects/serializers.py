from rest_framework import serializers
from .models import ProjectImg

class ProjectImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImg
        fields = 'id','order'