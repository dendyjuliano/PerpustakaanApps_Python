from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku

        # bila semua form akan di tampilkan
        fields = '__all__'

        # bisa memilih form yang di inginkan
        # fields = ['judul','penulis']

        # bila salah satu field tidak mau di tampilkan
        # exclude = ['judul','penerbit']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }