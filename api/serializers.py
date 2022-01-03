from rest_framework.serializers import ModelSerializer
from api.models import Stay


class StaySerializer(ModelSerializer):
    class Meta:
        model = Stay
        fields = '__all__'
