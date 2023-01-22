# list array untuk menyimpan data user
user = [["admin", "password"]]

# menu utama sebelum login
while True:
    print("Menu Utama:")
    print("1. Register")
    print("2. Login")
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user.append([username, password])
    elif pilihan == 2:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        for i in user:
            if i[0] == username and i[1] == password:
                print("Login berhasil!")
                # menu utama setelah login
                while True:
                    print("Menu Utama:")
                    print("1. Kasir")
                    print("2. Logout")
                    pilihan = int(input("Masukkan pilihan: "))
                    if pilihan == 1:
                        # fungsi kasir
                        print("Daftar Barang/Layanan:")
                        print("1. Barang A - Rp. 10.000")
                        print("2. Barang B - Rp. 15.000")
                        print("3. Layanan C - Rp. 20.000")
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
                        bayar = int(input("Masukkan jumlah pembayaran: "))
                        if bayar < total_harga:
                            print("Uang yang dibayar kurang.")
                            kembalian = bayar - total_harga
                        elif bayar == total_harga:
                            print("Uang yang dibayar pas.")
                            kembalian = bayar - total_harga
                        else:
                            kembalian = bayar - total_harga
                        print("Struk Pemesanan:")
                        print("Barang/Layanan:", pesan)
                        print("Total Harga: Rp. ", total_harga)
                        print("Pembayaran: Rp. ", bayar)
                        print("Kembalian: Rp. ", kembalian)
                    elif pilihan == 2:
                        print("Anda berhasil logout.")
                        break
                    else:
                        print("Pilihan tidak tersedia.")
                break
        else:
            print("Username atau password salah.")
    else:
        print("Pilihan tidak tersedia")
break
