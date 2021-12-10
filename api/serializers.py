from rest_framework.serializers import ModelSerializer
from api.models import SampleCategory, SampleStoreList


class DataSerializer(ModelSerializer):
    class Meta:
        model = SampleCategory
        fields = '__all__'

class StoreSerializer(ModelSerializer):
    class Meta:
        model = SampleStoreList
        fields = '__all__'

