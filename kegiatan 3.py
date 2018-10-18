Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Viola Lovitasari'
>>> NIM = 'L200180173'
>>> x =  '1' + NIM [7:] # Didalam string, digabungkan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print (x) # Menampilkan variabel x
1173
>>> a = int (x) # Konversi string ke integer (bilangan bulat)
>>> print (a) # Menampilkan variabel a
1173
>>> b = len (Nama) # Konversi string dalam variabel Nama ke dalam angka
>>> print (b) # Menampilkan variabel b
16
>>> type (a) # Menampilkan type data dari variabel a
<type 'int'>
>>> type (b) # Menampilkan type data dari variabel b
<type 'int'>
>>> a / b # Operasi pembagian antara bilangan dari variabel a dengan b. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/flo
73
>>> a // b # Operasi pembagian antara bilangan dengan pembulatan ke bawah. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/
73
>>> 10 * (a - 999) # Operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer dengan integer, floating point dengan floating point, integer deng
1740
>>> b ** 2 # Operasi ini digunakan untuk perpangkatan, type data yang dapat diolah menggunakan operasi ini diantaranya integer dan floating point. Namun, pada operasi
256
>>> a % b # Operasi ini digunakan untuk memunculkan sisa hasil bagi
5
>>> c = 12.5 # Variabel c menggunakan angka dengan koma yang berarti type data yang terdapat pada variabel c adalah type floating point
>>> type (c) # Menampilkan type data dari variabel c
<type 'float'>
>>> a / c # operasi pembagian antara bilangan dari variabel a dengan b. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/flo
93.84
>>> a // c # Operasi pembagian antara bilangan dengan pembulatan ke bawah. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/
93.0
>>> a % c # Operasi ini digunakan untuk memunculkan sisa hasil bagi
10.5
>>> c > b # Operasi ini digunakan untuk menampilkan perbandingan lebih besar dari. Type dari data adalah boolean
False
>>> type (c > b) # Menampilkan type data dari (c > b)
<type 'bool'>
>>> a > b and b > c # Pada data terdapat dua pernyataan yaitu 1173 > 16 dan 16 > 12.5. Karena, kedua pernyataan tersebut dihubungkan dengan operasi logika "and" maka
True
>>> a > 1100 or b < 10 # Logika yang digunakan pada data adalah "or". Dari pernyataan disamping diartikan 1173 > 1100 atau 16 < 10. Dengan 1173 > 1100 adalah data pert
True
>>> 
