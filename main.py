# main.py
# Program utama (CLI)

from analytics import (
    tampilkan_data,
    total_tagihan,
    rata_rata_tagihan,
    urutkan_tagihan_desc,
    prediksi_bulan_depan
)


def menu():
    print("\n=== RESIDENT HUB - SMART ANALYTICS ===")
    print("1. Tampilkan Data Billing")
    print("2. Total Tagihan Resident")
    print("3. Rata-rata Tagihan Resident")
    print("4. Urutkan Tagihan Terbesar")
    print("5. Prediksi Tagihan Bulan Depan")
    print("0. Keluar")


while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        rid = input("Masukkan Resident ID: ")
        print("Total Tagihan: Rp", total_tagihan(rid))

    elif pilihan == "3":
        rid = input("Masukkan Resident ID: ")
        print("Rata-rata Tagihan: Rp", rata_rata_tagihan(rid))

    elif pilihan == "4":
        hasil = urutkan_tagihan_desc()
        print("\nTAGIHAN TERBESAR")
        for b in hasil:
            print(f"{b.resident_id} | {b.bulan} | Rp {b.jumlah}")

    elif pilihan == "5":
        rid = input("Masukkan Resident ID: ")
        prediksi = prediksi_bulan_depan(rid)
        if prediksi == 0:
            print("Data tidak cukup untuk prediksi.")
        else:
            print("Estimasi tagihan bulan depan: Rp", int(prediksi))

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
