Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## PRAKTIKUM 6 KEGIATAN 4
>>> Nama = 'Viola Lovitasari'
>>> NIM = 173
>>> Tinggi = 1.58
>>> Berat = 53
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama) # Sebuah tuple
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama] # Sebuah list
>>> type (Aku) # Untuk menampilkan tipe data dari variabel Aku
<type 'tuple'>
>>> Aku [0] # Menampilkan elemen tuple indeks 0
1999
>>> a = NIM % 4 ; Aku [a] # NIM, 173 dibagi dengan 4 sisanya adalah 1. Lalu indeks 1 dimasukkan kedalam variabel Aku
53
>>> type (Aku [a]) # Menampilkan tipe data dari elemen tuple indeks a
<type 'int'>
>>> Aku [a:4] # Slicing dimulai indeks ke 3 dan akhirnya indeks ke 4
(53, 1.58, 173)
>>> type (Aku [4]) # Menampilkan tipe data dari elemen tuple indeks 4
<type 'str'>
>>> Aku [0] = 'ok' # ERROR, karena elemen sebuah tuple tidak dapat diubah

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Aku [0] = 'ok' # ERROR, karena elemen sebuah tuple tidak dapat diubah
TypeError: 'tuple' object does not support item assignment
>>> type (Data) # Menampilkan tipe data dari variabel Data
<type 'list'>
>>> type (Data [4]) # Menampilkan tipe data dari elemen list indeks 4
<type 'str'>
>>> Data [4] [5] # Menampilkan list indeks 5 pada list 4
' '
>>> Data [4] [a:6] # Menampilkan list indeks 3 sampai 5 dari list 4
'iola '
>>> Data [0] = 'ok' ; Data # Mengubah elemen list pada indeks 0 menjadi ok
['ok', 53, 1.58, 173, 'Viola Lovitasari']
>>> Data [-a] # Menampilkan huruf/angka terakhir pada indeks ke 3 dari list
'Viola Lovitasari'
>>> range (a) # Menghasilkan semacam daftar atau koleksi dari indeks 3
[0]
>>> 
