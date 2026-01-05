# analytics.py
# Modul algoritma & analisis data

from data import billings

URUTAN_BULAN = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "Mei": 5,
    "Jun": 6,
    "Jul": 7,
    "Agu": 8,
    "Sep": 9,
    "Okt": 10,
    "Nov": 11,
    "Des": 12
}
def histori_urut_bulan(resident_id):
   
    data = [b for b in billings if b.resident_id == resident_id]

    data.sort(key=lambda x: URUTAN_BULAN[x.bulan])

    return data

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
    
    data = billings.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j].jumlah < data[j + 1].jumlah:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def prediksi_bulan_depan(resident_id):
    histori = histori_urut_bulan(resident_id)

    if len(histori) < 3:
        return 0

    tiga_bulan_terakhir = histori[-3:]

    return sum(b.jumlah for b in tiga_bulan_terakhir) / 3
