from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BookResource

def export_xls(request):
    buku = BookResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xls"'
    return response

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,"user berhasil dibuat")
            return redirect('signup')
        else :
            messages.error(request,"Terjadi Kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form
        }
    return render(request,'signup.html',konteks)



def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST,request.FILES,instance = buku)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diupdate")
            return redirect('ubah-buku',id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku
        }
        return render(request,template,konteks)

def hapus_buku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request,"dihapus")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def buku(request) :
    # variable

    # select * from buku
    books = Buku.objects.all()

    # select * from buku where
    # books = Buku.objects.filter(jumlah=30)

    # penulisan limit pada sql (limit 3) sedangkan pada django [:3]

    # menampilkan filter dengan relasi table atau join
    # books = Buku.objects.filter(kelompok_id__nama='Novel')[:1]

    # mengumpulkan apa yang mau di kirimkan ke template
    konteks = {
        'books':books
    }

    return render(request,'buku.html',konteks)

def penerbit(request) :
    return render(request,'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data Berhasil disimpan"
            konteks = {
                'form':form,
                'pesan':pesan
            }
            return render(request,'tambah-buku.html',konteks)
    else:
        form = FormBuku()

        konteks = {
            'form':form
        }

    return render(request,'tambah-buku.html',konteks)