## kegiatan 1 praktikum 9
berkas = open("L200180173","w")
berkas.write("L200180173 \n")
berkas.write("13-07-1999 \n")
berkas.write("Viola Lovitasari \n")
berkas.close()

## kegiatan 2 praktikum 9
berkas = open("L200180173","w")
berkas.write("L200180173 \n")
berkas.write("Viola Lovitasari \n")
berkas.write("Boyolali \n")
berkas.write("13-07-1999 \n")
berkas.close()

import shelve
f = open("L200180173","r")
NIM = f.readline()
Nama = f.readline()
Kota = f.readline()
TL = f.readline()
f.close()

f = shelve.open("Viola")
f['v'] = [Nama, Kota, TL, NIM]
f.close()

f = shelve.open("Viola")

print f['v'][0]
print f['v'][1]
print f['v'][2]
print f['v'][3]

## kegiatan 3 praktikum 9
import shelve
f = open("L200180173","r")
Nim = f.readline()
Nama = f.readline()
Kota = f.readline()
TL = f.readline()
f.close()

f = shelve.open("Viola")
f['v'] = [Nama, Kota, TL, NIM]
f.close()

## kegiatan 4 praktikum 9
import shelve
f = shelve.open("Viola")
print 'Nama :' , f['v'][0]
print 'Kota :' , f['v'][1]
print 'TL   :' , f['v'][2]
print 'NIM  :' , f['v'][3]

