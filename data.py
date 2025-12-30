# data.py
# Struktur data & data dummy billing resident

class Billing:
    def __init__(self, resident_id, bulan, jumlah):
        self.resident_id = resident_id
        self.bulan = bulan
        self.jumlah = jumlah


billings = [
    Billing("R001", "Jan", 1200000),
    Billing("R001", "Feb", 1250000),
    Billing("R001", "Mar", 1300000),
    Billing("R001", "Apr", 1280000),
    Billing("R002", "Jan", 1000000),
    Billing("R002", "Feb", 1050000),
]
