# Resident-Hub---Smart-Analytics-Module
Course 12 - Machine Learning Fundamental

Anggota
1.	Muhamad Faisal Ramadhan
2.	Deni Ahmad Fauzi
3.	Muhamad Lutfi Adli Setiawan
4.	Sayid Rama Aheta
5.	Fauzan Azhima Zakaria

Resident Hub - Smart Analytics Module adalah mini aplikasi berbasis CLI yang berfungsi untuk menganalisis data tagihan (billing resident) melalui menu interaktif. Mini aplikasi ini dirancang dengan sederhana dan mudah digunakan sehingga focus pada logika pemograman dan pengolahan data.
Fitur pada Aplikasi
1.	Tampilkan Data Billing
Menampilkan semua data tagihan resident yang sudah tersimpan sebelumnya, sehingga admin/user dapat melihat billing secara lengkap yaitu:
-	Resident ID
-	Bulan
-	Jumlah (Rp) Tagihan
2.	Total Tagihan Resident
Menampilkan total biaya yang harus dibayar oleh satu resident dalam keseluruhan data.
3.	Rata-rata Tagihan Resident
Menampilkan hasil perhitungan rata-rata tagihan dari satu resident yang di dalam sistem.
4.	Urutkan Tagihan Terbesar
Menampilkan data billing resident dari tagihan terbesar sampai ke terkecil secara berurutan.
5.	Prediksi Tagihan Bulan Depan
Menampilkan perkiraan/prediksi tagihan bulan berikutnya berdasarkan data billing sebelumnya (data 3 bulan terakhir).
6.	Keluar
Mengakhiri program dan keluar dari aplikasi.

- main.py
Berfungsi sebagai program utama dari mini aplikasi Resident Hub  dan menjadi antarmuka admin/pengguna berbasis Command Line Interface (CLI). File ini menampilkan menu, menerima input, mengontrol alur program dan memanggil fungsi fungsi analisis pada file analytics.py sesuai pilihan menu.

- analytics.py
Berfungsi sebagai tempat pengolahan dan analisis data. Didalamnya terdapat beberapa fungsi untuk menghitung total tagihan, rata-rata tagihan, mengurutkan data berdasarkan jumlah tagihan, mengelola history billing berdasarkan bulan untuk melakukan prediksi tagihan  bulan berikutnya. 

- data.py
Berfungsi sebagai file penyedia data serta menyimpan kumpulan data billing. Seluruh proses analisis dalam aplikasi menggunakan data dari file data.py.

Output :

<img width="496" height="239" alt="image" src="https://github.com/user-attachments/assets/abbaabc9-b8b2-4d03-8923-13b2a269045e" />

 
1.	Tampilkan Data Billing

<img width="420" height="417" alt="image" src="https://github.com/user-attachments/assets/f23d7b84-c7f4-4940-88e1-7b0dd6bfe212" />

 
2.	Total Tagihan Resident

 <img width="524" height="332" alt="image" src="https://github.com/user-attachments/assets/7111af5a-0431-42e1-9c23-81d53da1c2da" />


3.	Rata-rata Tagihan Resident

 <img width="521" height="327" alt="image" src="https://github.com/user-attachments/assets/58033eea-9a28-46a3-9530-e818c5ec37e6" />


4.	Urutkan Tagihan Terbesar

<img width="522" height="518" alt="image" src="https://github.com/user-attachments/assets/8a3d9d5f-449d-431e-b62c-f513d198e350" />

 
5.	Prediksi Tagihan Bulan Depan

<img width="605" height="345" alt="image" src="https://github.com/user-attachments/assets/c4883e45-80a7-4896-b01a-0d8ad9f38d7b" />
 

0.	Keluar

 <img width="608" height="336" alt="image" src="https://github.com/user-attachments/assets/ae6c1298-e920-4cdf-995f-e3981acfce3d" />




