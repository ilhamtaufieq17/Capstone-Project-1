from tabulate import tabulate

daftarBuku = {
    'Dilan 1990' : [1, 101, 'Dilan 1990', 'Pidi Baiq', 'Novel', 2014, 10],
    'Boruto' : [2, 201, 'Boruto', 'Ukyo Kodachi & Masashi Kisimoto', 'Komik', 2016, 9],
    'The Game Rules' : [3, 301, 'The Game Rules', 'FIFA', 'Olahraga', 2023, 8],
    'Jujutsu Kaisen' : [4, 202, 'Jujutsu Kaisen', 'Gege Akutami', 'Komik', 2023, 7],
}

def validasiInt(title, minval=0, maxval=10000):
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print('Angka yang anda masukkan di luar rentang')
        except:
            print('Yang anda inputkan bukan bilangan')
    return num

def subMenuTampilkan():
    while True:
        print('''
        Tampilkan Data Buku

        1. Tampilkan Seluruh Buku
        2. Cari Buku Berdasarkan ID
        3. Kembali Ke Menu Awal
              ''')

        pilMenu = validasiInt(title="Masukkan angka sesuai menu: ")

        if pilMenu == 1:
            tampilkanBuku(daftarBuku)
        elif pilMenu == 2:
            pencarianBukuId(daftarBuku)
        elif pilMenu == 3:
            break
        else:
            print('\nInput anda salah. Silahkan input ulang!\n')

def subMenuTambahkan():
    while True:
        print('''
        Tambahkan Buku

        1. Tambahkan Data Buku Baru
        2. Kembali Ke Menu Awal
              ''')

        pilMenu = validasiInt(title="Masukkan Angka Sesuai Menu: ")

        if pilMenu == 1:
            tambahBuku()
        elif pilMenu == 2:
            break
        else:
            print('\nInput anda salah. Silahkan input ulang!\n')

def subMenuHapus():
    while True:
        print('''
        Hapus Buku

        1. Hapus Data Buku
        2. Kembali Ke Menu Awal
              ''')

        pilMenu = validasiInt(title="Masukkan Angka Sesuai Menu: ")

        if pilMenu == 1:
            hapusBuku()
        elif pilMenu == 2:
            break
        else:
            print('\nInput anda salah. Silahkan input ulang!\n')

def subMenuUpdate():
    while True:
        print('''
        Update Data Buku

        1. Update Data Buku
        2. Kembali Ke Menu Awal
              ''')

        pilMenu = validasiInt(title="Masukkan Angka Sesuai Menu: ")

        if pilMenu == 1:
            updateBuku()
        elif pilMenu == 2:
            break
        else:
            print('\nInput anda salah. Silahkan input ulang!\n')

def tampilkanBuku(database ,header=['No', 'ID Buku', 'Judul', 'Pengarang', 'Kategori', 'Tahun Terbit', 'Jumlah']):
    if len(daftarBuku) == 0:
        print('\nTidak Ada Data Yang Ditampilkan\n')
    else:
        print(tabulate(database.values(), headers=header, tablefmt='grid', stralign='center', numalign='center'))

def pencarianBukuId(idBuku):
    if len(daftarBuku) == 0:
        print('\nTidak Ada Data Yang Ditampilkan\n')
    else:
        idBuku = validasiInt(title='Masukkan ID Buku Yang Ingin Dicari: ')
        dataBuku = {}
        for key, val in daftarBuku.items():
            if idBuku == val[1]:
                valCopy = val[:]
                valCopy[0] = 1
                dataBuku.update({key: valCopy})
                tampilkanBuku(dataBuku)
                break
        else:
            print('\nBuku Yang Anda Cari Tidak ada\n')

def tambahBuku():
    idBuku = validasiInt(title='Masukkan ID Buku: ')
    status = False
    for buku in daftarBuku.values():
        if buku[1] == idBuku:
            status = True
            break
    if status:
        print(f"\nBuku dengan ID {idBuku} sudah ada. Silakan periksa kembali.\n")
        return

    judul = input('Masukkan Judul Buku: ').title()
    if any(buku[2] == judul for buku in daftarBuku.values()):
        print(f"\nBuku berjudul {judul} sudah ada. Silakan periksa kembali.\n")
        return
    pengarang = input('Masukkan Pengarang Buku: ').title()
    kategori = input('Masukkan Kategori Buku: ').title()
    tahunTerbit = validasiInt(title='Masukkan Tahun Terbit Buku: ', minval=0)
    jumlah = validasiInt(title='Masukkan Jumlah Buku: ', minval=0)

    while True:
        validasi = input('Apakah Anda Setuju Akan Menambahkan Buku? (Y/N): ').lower()
        if validasi in ['yes', 'y', 'ya']:
            noBaru = len(daftarBuku) + 1
            daftarBuku[noBaru] = [noBaru, idBuku, judul, pengarang, kategori, tahunTerbit, jumlah]
            print('\nBuku Berhasil Ditambahkan!\n')
            tampilkanBuku(daftarBuku)
            break
        elif validasi in ['no', 'n', 'tidak']:
            print('\nBuku Batal Ditambahkan!\n')
            break
        else:
            print('\nInputan Anda Tidak Sesuai\n')

def updateBuku():
    if len(daftarBuku) == 0:
        print('\nTidak Ada Data Yang Ditampilkan\n')
    else:
        idBuku = validasiInt(title='Masukkan ID Buku: ')
        for key, buku in daftarBuku.items():
            if buku[1] == idBuku:
                while True:
                    dataBuku = {}
                    for key, val in daftarBuku.items():
                        if idBuku == val[1]:
                            valCopy = val[:]
                            valCopy[0] = 1
                            dataBuku.update({key: valCopy})
                            tampilkanBuku(dataBuku)
                            break
                        
                    validasi = input('Apakah Anda Setuju Akan Mengubah Data Buku? (Y/N): ').lower()
                    if validasi in ['yes', 'y', 'ya']:
                        print('''
                        Pilih kolom yang ingin diupdate:
                        1. Judul Buku
                        2. Pengarang Buku
                        3. Kategori Buku
                        4. Tahun Terbit Buku
                        5. Jumlah Buku
                        6. Update Keseluruhan
                        7. Kembali      
                        ''')
                        pilihan = validasiInt("Masukkan pilihan (1-6): ")
                        
                        if pilihan == 1:
                            judulBaru = input('Masukkan Judul Buku baru: ').title()
                            if any(buku[2] == judulBaru for buku in daftarBuku.values()):
                                print(f"\nBuku berjudul {judulBaru} sudah ada. Silakan periksa kembali.\n")
                                break
                            else:
                                validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                                if validasi in ['yes', 'y', 'ya']:
                                    buku[2] = judulBaru
                                    print('\nPerubahan Judul Buku Berhasil Disimpan\n')
                                    tampilkanBuku(daftarBuku)
                                    break
                                elif validasi in ['no', 'n', 'tidak']:
                                    print('\nPerubahan Judul Buku Batal Disimpan\n')
                                    break
                                else:
                                    print('\nInput Tidak Sesuai\n')

                        elif pilihan == 2:
                            pengarangBaru = input('Masukkan Pengarang Buku baru: ').title()
                            validasi = input('\nApakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[3] = pengarangBaru
                                print('\nPerubahan Data Berhasil Disimpan\n')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('\nPerubahan Data Batal Disimpan\n')
                                break
                            else:
                                print('\nInput Tidak Sesuai\n')

                        elif pilihan == 3:
                            kategoriBaru = input('Masukkan Kategori Buku baru: ').title()
                            validasi = input('\nApakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[4] = kategoriBaru
                                print('\nPerubahan Data Berhasil Disimpan\n')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('\nPerubahan Data Batal Disimpan\n')
                                break
                            else:
                                print('\nInput Tidak Sesuai\n')

                        elif pilihan == 4:
                            tahunBaru = validasiInt('Masukkan Tahun Terbit Buku baru: ', minval=0)
                            validasi = input('\nApakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[5] = tahunBaru
                                print('\nPerubahan Data Berhasil Disimpan\n')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('\nPerubahan Data Batal Disimpann\n')
                                break
                            else:
                                print('\nInput Tidak Sesuai\n')

                        elif pilihan == 5:
                            jumlahBaru = validasiInt('Masukkan Jumlah Buku baru: ', minval=0)
                            validasi = input('\nApakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[6] = jumlahBaru
                                print('\nPerubahan Data Berhasil Disimpan\n')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('\nPerubahan Data Dibatalkan\n')
                                break
                            else:
                                print('\nInput Tidak Sesuai\n')

                        elif pilihan == 6:
                            judulBaru = input('Masukkan Judul Buku baru: ').title()
                            if any(buku[2] == judulBaru for buku in daftarBuku.values()):
                                print(f"\nBuku berjudul {judulBaru} sudah ada. Silakan periksa kembali.\n")
                                return
                            pengarangBaru = input('Masukkan Pengarang Buku baru: ').title()
                            kategoriBaru = input('Masukkan Kategori Buku baru: ').title()
                            tahunBaru = validasiInt('Masukkan Tahun Terbit Buku baru: ', minval=0)
                            jumlahBaru = validasiInt('Masukkan Jumlah Buku baru: ', minval=0)

                            validasi = input('\nApakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[2], buku[3], buku[4], buku[5], buku[6] = judulBaru, pengarangBaru, kategoriBaru, tahunBaru, jumlahBaru
                                print('\nPerubahan Data Berhasil Disimpan\n')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('\nPerubahan Data Dibatalkan\n')
                                break
                            else:
                                print('\nInput Tidak Sesuai\n')
                        elif pilihan == 7:
                            break
                        else:
                            print("\nPilihan tidak valid. Silakan coba lagi.\n")

                    elif validasi in ['no', 'n', 'tidak']:
                        print('\nData Batal Diupdate\n')
                        break
                    else: 
                        print('\nInputan Anda Tidak Sesuai\n')
                return
        print(f"\nBuku dengan ID {idBuku} tidak ditemukan.\n")

def hapusBuku():
    tampilkanBuku(daftarBuku)
    if len(daftarBuku) == 0:
        print('\nTidak Ada Data Yang Ditampilkan\n')
    else:
        idBuku = validasiInt(title='Masukkan ID Buku: ')

        for key, val in list(daftarBuku.items()):
            if idBuku == val[1]:
                validasi = input('\nApakah Anda Setuju Menghapus Buku? (Y/N): ').lower()
                if validasi in ['yes', 'y', 'ya']:
                    del daftarBuku[key]
                    print(f'\nBuku dengan ID {idBuku} berhasil dihapus.\n')
                    break
                elif validasi in ['no', 'n', 'tidak']:
                    print('\nPenghapusan Buku Dibatalkan.\n')
                    break
                else:
                    print('\nInputan Anda Tidak Sesuai.\n')
                    break
        else:
            print(f'\nBuku dengan ID {idBuku} tidak ditemukan.\n')

        for index, (key, val) in enumerate(daftarBuku.items(), start=1):
            val[0] = index

        if len(daftarBuku) == 0:
            print('\nTidak Ada Data Yang Ditampilkan\n')
        else:
            tampilkanBuku(daftarBuku)