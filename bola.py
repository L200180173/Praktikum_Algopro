#!/usr/bin/python

def hitung_luas(jarijari):
    "fungsi menghitung luas dari bola"
    r=jarijari
    phi=3.14
    hasil=4*phi*r*r
    return hasil

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Selamat Datang</title></head>
<body>
<table>
    <tr>
        <td width='100' align='center' rowspan='6'> GAMBAR </td>
        <td colspan='3'><b><font size='5'>Bangun Geometri</font></b></td>
    </tr>
    <tr>
        <td>Nama Bangun </td>
        <td>:</td>
        <td> bola </td>
    </tr>
    <tr>
        <td> Dimensi (2D/3D) </td>
        <td>:</td>
        <td>3D</td>
    </tr>
    <tr>
        <td> Rumus luas</td>
        <td>:</td>
        <td> 4 x phi x r x r</td>
    </tr>"""
jarijari=21
print"""
    <tr>
        <td>jari-jari</td>
        <td>:</td>
        <td>{0}</td>
    </tr>""".format(jarijari)
luas=hitung_luas(jarijari)
print"""
    <tr>
        <td> Luas</td>
        <td>:</td>
        <td>{0}</td>
    </tr>""".format (luas)
print"""
</table>
</body>
</html>"""    
