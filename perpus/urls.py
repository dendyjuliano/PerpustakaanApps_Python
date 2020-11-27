from django.contrib import admin
from django.urls import path,include
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from perpustakaan.viewset_api import KelompokViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok',KelompokViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('buku/', buku,name='buku'),
    path('penerbit/', penerbit),
    path('tambah-buku/',tambah_buku,name='tambah-buku'),
    path('buku/ubah/<int:id_buku>',ubah_buku, name='ubah-buku'),
    path('buku/hapus/<int:id_buku>',hapus_buku,name='hapus-buku'),
    path('masuk/',LoginView.as_view(),name='masuk'),
    path('keluar/',LogoutView.as_view(next_page='masuk'),name='keluar'),
    path('signup/',signup,name='signup'),
    path('export/xls/',export_xls,name='export_xls')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)