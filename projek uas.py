menu = {
    1: {"item": "Nasi Goreng", "harga": 14000},
    2: {"item": "Mie Goreng", "harga": 13500},
    3: {"item": "Ayam Goreng", "harga": 8500},
    4: {"item": "Es Teh", "harga": 5000},
    5: {"item": "Es Jeruk", "harga": 5000},
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("========== Daftar Menu ==========")
    for num, value in menu.items():
        print(f"{num}. {value['item']} \t: Rp {value['harga']}\t|")
    print("=================================")

# Fungsi untuk menghitung total pembelian
def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total

# Fungsi utama
def main():
    print("============ Warung Muiz ============")
    nama_kasir = input("Nama Kasir: ")

    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-5), 0 untuk mengakhiri pesanan\t: "))
            if pilihan == 0:
                break
            elif pilihan not in menu:
                print("Pilihan tidak valid. Silakan masukkan nomor yang benar -_-")
            else:
                jumlah = int(input(f"Masukkan jumlah yang ingin dibeli\t\t: "))
                if pilihan in pesanan:
                    pesanan[pilihan] += jumlah
                else:
                    pesanan[pilihan] = jumlah
        except ValueError:
            print("Masukkan nomor atau jumlah yang valid.")

    if not pesanan:
        print("Anda belum memesan apapun.")
    else:
        total_harga = hitung_total(pesanan)
        print("Tagihan: Rp ",total_harga)

        # Meminta input jumlah uang yang diberikan oleh pelanggan
        Bayar = input("Bayar\t: Rp ")
        if Bayar.isdigit():
            Tunai = int(Bayar)
        else:
            print("Masukkan jumlah uang yang valid.")

        # Menghitung kembalian
        kembalian = Tunai - total_harga

        # Menampilkan struk pembelian
        print("\n============ Struk Pembelian ============")
        print(f"Nama Kasir \t\t= {nama_kasir}\t\t|")
        print("=========================================")
        for pilihan, jumlah in pesanan.items():
            print(f"{menu[pilihan]['item']} Sejumlah {jumlah} \t= Rp {menu[pilihan]['harga'] * jumlah}\t|")
        print("=========================================")
        print(f"Total Harga \t\t= Rp {total_harga}\t|")
        print(f"Tunai \t\t\t= Rp {Tunai}\t|")
        print(f"Kembalian \t\t= Rp {kembalian}\t|")
        print("=========================================")

        return total_harga, Tunai, kembalian

if __name__ == "__main__":
    total_harga, tunai, kembalian = main()
    # Selanjutnya, Anda dapat menggunakan nilai yang dikembalikan sesuai kebutuhan.
