# login
username = input("Masukkan username: ")
password = input("Masukkan password: ")

# cek login
if username == "admin" and password == "pass":
    print("Login berhasil!")
    # tampilkan menu
    print("Daftar Barang/Layanan:")
    print("1. Barang A - Rp. 10.000")
    print("2. Barang B - Rp. 15.000")
    print("3. Layanan C - Rp. 20.000")
    # pemesanan
    pesan = []
    total_harga = 0
    pilihan = "y"
    while pilihan == "y":
        pemesanan = int(input("Masukkan pilihan barang/layanan: "))
        if pemesanan == 1:
            pesan.append("Barang A")
            total_harga += 10000
        elif pemesanan == 2:
            pesan.append("Barang B")
            total_harga += 15000
        elif pemesanan == 3:
            pesan.append("Layanan C")
            total_harga += 20000
        else:
            print("Pilihan tidak tersedia.")
        pilihan = input("Apakah ingin memesan lagi? (y/n)")
    # pembayaran
    bayar = int(input("Masukkan jumlah pembayaran: "))
    if bayar < total_harga:
        print("Uang yang dibayar kurang.")
    else:
        kembalian = bayar - total_harga
    # struk
    print("Struk Pemesanan:")
    print("Barang/Layanan:", pesan)
    print("Total Harga: Rp. ", total_harga)
    print("Pembayaran: Rp. ", bayar)
    print("Kembalian: Rp. ", kembalian)
else:
    print("Login gagal, periksa kembali username dan password Anda.")
