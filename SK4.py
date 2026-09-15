Data_buku = {
            "judul": "I Have NO Mouth and I Must Scream",
            "penulis": "Harlan Ellison",
            "tahun": 1967
    }

#Looping Menu
while True:
    print("Menu Data Buku")
    print("1. Lihat Data Buku")
    print("2. Tambah Data Penerbit Buku")
    print("3. Edit Data Penulis Buku")
    print("4. Hapus Data Penerbit Buku")
    print("5. Keluar")
    #Input user
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        if not Data_buku:
            print("Nampaknya Tida' Ada Data Buku")
        else:
            print("Judul:", Data_buku.get("judul"))
            print("Penulis:", Data_buku.get("penulis"))
            print("Tahun:", Data_buku.get("tahun"))

            if "penerbit" in Data_buku:
                print("Penerbit:", Data_buku.get("penerbit"))

    elif pilihan == "2":
        if not Data_buku:
            print("Nampaknya Tida' Ada Data Buku")
        else:
            penerbit = input("Masukkan Nama Penerbit: ")
            Data_buku["penerbit"] = penerbit
            print(" Data penerbit berhasil ditambahkan!")

    elif pilihan == "3":
        if not Data_buku:
            print("Nampaknya Tida' Ada Data Buku")
        else:
            penulis_baru = input("Masukkan Nama Penulis Baru: ")
            Data_buku["penulis"] = penulis_baru
            print(" Data penulis berhasil diubah!")

    elif pilihan == "4":
        if not Data_buku:
            print("Nampaknya Tida' Ada Yang Bisa dihapus")
        else:
            del Data_buku["penerbit"]
            print(" Data penerbit berhasil dihapus!")

#OPSI KELUAR
    elif pilihan == "5":
        print("Anda KELUAR")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


