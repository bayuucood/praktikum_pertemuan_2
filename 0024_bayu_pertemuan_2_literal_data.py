print ("soal_1")
# membuat deklarasi program
print ("nama : Ucup Santoso")
print ("umur : 200 tahun")
print ("berat : 56.4 kg")

print ("soal_2")
# mengubah tipe data
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# konversi angka_string menjadi integer
hasil1 = int (angka_string)
print (hasil1, "type = ", type (hasil1))
# konversi angka_float menjadi integer
hasil2 = int (angka_float)
print (hasil2, "type = ", type (hasil2))
# konversi angka_integer menjadi float
hasil3 = float (angka_integer)
print (hasil3, "type = ", type (hasil3))
# konversi angka_integer menjadi string
hasil4 = str (angka_integer)
print (hasil4, "type = ", type (hasil4))

print ("soal_3")
# membuat deklarasi program
usia = int (input ("masukkan usia : "))
tinggi_badan = float (input ("masukkan tinggi badan : "))
nama = str (input ("masukkan nama : "))

print ("data usia :", usia, ", type = ", type(usia))
print ("data tinggi badan :", tinggi_badan, ", type = ", type(tinggi_badan))
print ("data nama :", nama, ", type = ", type(nama))

