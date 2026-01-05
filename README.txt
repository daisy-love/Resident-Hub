Project Title : Resident Hub - Smart Analytics Module
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

main.py
Berfungsi sebagai program utama dari mini aplikasi Resident Hub  dan menjadi antarmuka admin/pengguna berbasis Command Line Interface (CLI). File ini menampilkan menu, menerima input, mengontrol alur program dan memanggil fungsi fungsi analisis pada file analytics.py sesuai pilihan menu.

analytics.py
Berfungsi sebagai tempat pengolahan dan analisis data. Didalamnya terdapat beberapa fungsi untuk menghitung total tagihan, rata-rata tagihan, mengurutkan data berdasarkan jumlah tagihan, mengelola history billing berdasarkan bulan untuk melakukan prediksi tagihan  bulan berikutnya. 

data.py
Berfungsi sebagai file penyedia data serta menyimpan kumpulan data billing. Seluruh proses analisis dalam aplikasi menggunakan data dari file data.py.

