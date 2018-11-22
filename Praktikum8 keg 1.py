V = {'NIM':'L200180173','Nama':'Viola Lovitasari','Alamat':'Boyolali','Panggilan':'Viola', 'Prodi':'Informatika','Fak':'FKI','Umur':'19'}

print "Pilihan yang tersedia:"
print "N menampilkan Nama"
print "n menampilkan NIM"
print "l menampilkan Alamat"
print "p menampilkan Panggilan"
print "r menampilkan Prodi"
print "f menampilkan Fakultas"
print "u menampilkan Umur"


def Nama():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Nama:' + V['Nama']

def NIM():
        "menampilkan data diri masing masing 1 setiap data"
        print 'NIM:' + V['NIM']

def Alamat():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Alamat:' + V['Alamat']

def Panggilan():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Paggilan:' + V['Panggilan']

def Prodi():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Prodi:' + V['Prodi']

def Fak():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Fakultas:' + V['Fak']

def Umur():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Umur:' + V['Umur']

repeat = True

while repeat :
    x = raw_input("Pilihan Saudara:")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM ()
    elif x == "l" :
        Alamat ()
    elif x == "p" :
        Panggilan ()
    elif x == "r" :
        Prodi ()
    elif x == "f" :
        Fak ()
    elif x == "u" :
        Umur ()
    elif x == "k" :
        print "Terimakasih."
        repeat = False
        
