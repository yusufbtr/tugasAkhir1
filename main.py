import sys

totalHarga = 0
pilihObat = []
harga = []
while True:
    print()
    print('Selamat Datang di Toko Obat Stutle\n'
          'Ketik perintah untuk membuka menu\n'
          '1. List Obat\n'
          '-perintah: list-obat\n'
          '2. Beli Obat\n'
          '-perintah: beli-<namaobat>\n'
          '3. Hapus Obat\n'
          '-perintah: hapus-<namaobat>\n'
          '4. Melihat Daftar Keranjang\n'
          '-perintah: keranjang\n'
          '5. Transaksi Pembelian\n'
          '-perintah: checkout\n'
          '6. Exit\n'
          '-perintah: exit\n'
          )

    choice = input("Silahkan ketik perintah yang anda inginkan: ")

    if choice == "list-obat":
        namaObat = ["paramex \t Rp1000", "panadol \t Rp2000", "bodrexin \t Rp3000", "procold \t Rp4000"]
        print("List Obat - Obat yang tersedia: ")
        for i in namaObat:
            print(i)
    elif choice == "beli-paramex":
        pilihObat.append('paramex')
        harga.append(1000)
        totalHarga += 1000
    elif choice == "beli-panadol":
        pilihObat.append('panadol')
        harga.append(2000)
        totalHarga += 2000
    elif choice == "beli-bodrexin":
        pilihObat.append('bodrexin')
        harga.append(3000)
        totalHarga += 3000
    elif choice == "beli-procold":
        pilihObat.append('procold')
        harga.append(4000)
        totalHarga += 4000
    elif choice == "hapus-paramex":
        pilihObat.remove('paramex')
        harga.remove(1000)
        totalHarga -= 1000
    elif choice == "hapus-panadol":
        pilihObat.remove('panadol')
        harga.remove(2000)
        totalHarga -= 2000
    elif choice == "hapus-bodrexin":
        pilihObat.remove('bodrexin')
        harga.remove(3000)
        totalHarga -= 3000
    elif choice == "hapus-procold":
        pilihObat.remove('procold')
        harga.remove(4000)
        totalHarga -= 4000
    elif choice == "keranjang":
        # print('Obat yang dibeli: ', pilihObat)
        print('Obat yang dibeli: ')
        # print("List Obat - Obat yang tersedia: ")
        for j in pilihObat:
            print(j)
        # print('harga obatnya: ', harga, '(dalam Rupiah)')
        print('harga obatnya: (dalam Rupiah)')
        for k in harga:
            print(k)
    elif choice == "checkout":
        print('total yang harus dibayar: Rp', totalHarga, '\n')
        bayar = int(input("Nominal uang pembayaran: Rp"))
        if bayar > totalHarga:
            print('Uang kembaliannya sebesar: Rp', bayar - totalHarga)
        elif bayar == totalHarga:
            print('Uang pembayarannya pas')
        else:
            print('Uang pembayaran kurang')
    elif choice == "exit":
        sys.exit()
    else:
        print("perintah yang kamu masukkan salah.")
