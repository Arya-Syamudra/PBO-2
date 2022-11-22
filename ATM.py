nama = "Arya Syamudra"
norek = 1234567890
pin = 12345
saldo = 1900000000

while True:
    print("=" * 50)
    print("=" + "ATM Sederhana".center(48) + "=")
    print("=" * 50)
    print("Selamat Datang".center(50))
    print("Menu Transaksi : " + "\n 1. Informasi Saldo" + "\n 2. Tarik Tunai" + "\n 3. Keluar \n")
    pilihan = input("Masukkan Pilihan Anda : ")
    if pilihan == '1':
        print("Saldo Rekening Anda : RP")
        print(saldo)
        konfirmasi = input("Tekan tombol apapun untuk lanjut")
    elif pilihan == '2':
        while True:
            if saldo >= 50000:
                tunai = int(input("Masukkan Jumlah Penarikan : "))
                if tunai % 50000 == 0:
                    saldo1 = saldo - tunai
                    print("Saldo Ditarik : RP", tunai)
                    print("Sisa Saldo Anda : ", saldo1)
                    saldo = saldo1
                    konfirmasi = input("Tekan tombol apapun untuk lanjut")
                    break
                  
                else:
                    print("Nominal tidak diketahui,\nSilahkan Masukkan Jumlah penarikan kelipatan 50000")
                    konfirmasi = input("Tekan tombol apapun untuk lanjut")
            else:
                print("Transaksi Gagal".center(50) + "\nSaldo Tidak Mencukupi".center(50))
                while True:
                    konfirmasi = input("Ingin Melakukan Transaksi Lain? (y/n) : ")
                    if konfirmasi == 'y':
                        print("")
                    elif konfirmasi == 'n':
                        break
                    else:
                        print("") 
    elif pilihan == '3':
      break
    else:
      print("Perintah tidak ditemukan")
      konfirmasi = input("Tekan tombol apapun untuk lanjut")
