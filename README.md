# README

Program menggunakan bahasa python dengan library pyopengl dan pygame untuk menampilkan mobil dengan animasi roda yang berotasi.

Pada program ini menggunakan shader dan immediate untuk menghasilkan grafis mobil. 

### Shader
Shader menggunakan VBO dan VAO untuk binding titik-titik yang digunakan dalam menggambarkan mobil. Sehingga tiap satuan waktu, program tidak perlu menggambarkan ulang masing-masing titik karena sudah diabstraksikan di dalam VBO.

### Immediate
Immediate menggunakan glBegin() dan glEnd() untuk menggambarkan sebuah objek per satuan waktu sehingga tiap menampilkan objek ke layar, titik-titik digambarkan ulang lagi.

### Perbandingan Shader dan Immediate
Jika dilihat dari keefisiensian dalam menggambar, maka shader lebih efisien karena tidak perlu menggambarkan ulang objek tiap satuan waktu

by : Twin Group
