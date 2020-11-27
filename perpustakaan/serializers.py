from perpustakaan.models import Kelompok
from rest_framework import serializers

class KelompokSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kelompok
        fields = ['id','nama','keterangan']