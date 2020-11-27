from perpustakaan.models import Kelompok
from perpustakaan.serializers import KelompokSerializer
from rest_framework import viewsets
# from rest_framework import permissions

class KelompokViewSet(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializer
    # permission_classes = [permissions.IsAuthenticated]
