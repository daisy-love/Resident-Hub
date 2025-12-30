# analytics.py
# Modul algoritma & analisis data

from data import billings


def tampilkan_data():
    print("\nDATA BILLING RESIDENT")
    for b in billings:
        print(f"{b.resident_id} | {b.bulan} | Rp {b.jumlah}")


def total_tagihan(resident_id):
    total = 0
    for b in billings:
        if b.resident_id == resident_id:
            total += b.jumlah
    return total


def rata_rata_tagihan(resident_id):
    total = 0
    count = 0
    for b in billings:
        if b.resident_id == resident_id:
            total += b.jumlah
            count += 1

    if count == 0:
        return 0

    return total / count


def urutkan_tagihan_desc():
    # Bubble Sort (mudah dijelaskan di laporan)
    data = billings.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j].jumlah < data[j + 1].jumlah:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def prediksi_bulan_depan(resident_id):
    histori = []

    for b in billings:
        if b.resident_id == resident_id:
            histori.append(b.jumlah)

    if len(histori) < 3:
        return 0

    return sum(histori[-3:]) / 3
