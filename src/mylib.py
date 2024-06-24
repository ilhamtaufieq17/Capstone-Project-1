from tabulate import tabulate

daftarBuku = {
    'Dilan 1990' : [1, 101, 'Dilan 1990', 'Pidi Baiq', 'Novel', 2014, 10],
    'Boruto' : [2, 201, 'Boruto', 'Ukyo Kodachi & Masashi Kisimoto', 'Komik', 2016, 9],
    'FIFA Rules and Regulations' : [3, 301, 'FIFA Rules and Regulations', 'FIFA', 'Olahraga', 2023, 8],
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
            print('Input anda salah. Silahkan input ulang!')

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
            print('Input anda salah. Silahkan input ulang!')

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
            print('Input anda salah. Silahkan input ulang!')

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
            print('Input anda salah. Silahkan input ulang!')

def tampilkanBuku(database ,header=['No', 'ID Buku', 'Judul', 'Pengarang', 'Kategori', 'Tahun Terbit', 'Jumlah']):
    if len(daftarBuku) == 0:
        print('Tidak Ada Data Yang Ditampilkan')
    else:
        print(tabulate(database.values(), headers=header, tablefmt='grid', stralign='center', numalign='center'))

def pencarianBukuId(idBuku):
    if len(daftarBuku) == 0:
        print('Tidak Ada Data Yang Ditampilkan')
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
            print('Buku Yang Anda Cari Tidak ada')

def tambahBuku():
    idBuku = validasiInt(title='Masukkan ID Buku: ')
    status = False
    for buku in daftarBuku.values():
        if buku[1] == idBuku:
            status = True
            break
    if status:
        print(f"Buku dengan ID {idBuku} sudah ada. Silakan periksa kembali.")
        return

    judul = input('Masukkan Judul Buku: ').capitalize()
    pengarang = input('Masukkan Pengarang Buku: ').capitalize()
    kategori = input('Masukkan Kategori Buku: ').capitalize()
    tahunTerbit = validasiInt(title='Masukkan Tahun Terbit Buku: ', minval=0)
    jumlah = validasiInt(title='Masukkan Jumlah Buku: ', minval=0)

    status = False
    for buku in daftarBuku.values():
        if buku[2] == judul:
            status = True
            break
    if status:
        print(f"Buku dengan judul {judul} sudah ada. Silakan periksa kembali.")
        return

    while True:
        validasi = input('Apakah Anda Setuju Akan Menambahkan Buku? (Y/N): ').lower()
        if validasi in ['yes', 'y', 'ya']:
            noBaru = len(daftarBuku) + 1
            daftarBuku[noBaru] = [noBaru, idBuku, judul, pengarang, kategori, tahunTerbit, jumlah]
            print('Buku Berhasil Ditambahkan!')
            tampilkanBuku(daftarBuku)
            break
        elif validasi in ['no', 'n', 'tidak']:
            print('Buku Batal Ditambahkan!')
            break
        else:
            print('Inputan Anda Tidak Sesuai')

def updateBuku():
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
                        judulBaru = input('Masukkan Judul Buku baru: ').capitalize()
                        status = False
                        for buku in daftarBuku.values():
                            if buku[2] == judulBaru:
                                status = True
                                break
                        if status:
                            print(f"Buku berjudul {judulBaru} sudah ada. Silakan periksa kembali.")
                            break
                        else:
                            validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                            if validasi in ['yes', 'y', 'ya']:
                                buku[2] = judulBaru
                                print('Perubahan Data Berhasil Disimpan')
                                tampilkanBuku(daftarBuku)
                                break
                            elif validasi in ['no', 'n', 'tidak']:
                                print('Perubahan Data Batal Disimpan')
                            else:
                                print('Input Tidak Sesuai')

                    elif pilihan == 2:
                        pengarangBaru = input('Masukkan Pengarang Buku baru: ').capitalize()
                        validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                        if validasi in ['yes', 'y', 'ya']:
                            buku[3] = pengarangBaru
                            print('Perubahan Data Berhasil Disimpan')
                            tampilkanBuku(daftarBuku)
                            break
                        elif validasi in ['no', 'n', 'tidak']:
                            print('Perubahan Data Batal Disimpan')
                        else:
                            print('Input Tidak Sesuai')

                    elif pilihan == 3:
                        kategoriBaru = input('Masukkan Kategori Buku baru: ').capitalize()
                        validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                        if validasi in ['yes', 'y', 'ya']:
                            buku[4] = kategoriBaru
                            print('Perubahan Data Berhasil Disimpan')
                            tampilkanBuku(daftarBuku)
                            break
                        elif validasi in ['no', 'n', 'tidak']:
                            print('Perubahan Data Batal Disimpan')
                        else:
                            print('Input Tidak Sesuai')

                    elif pilihan == 4:
                        tahunBaru = validasiInt('Masukkan Tahun Terbit Buku baru: ', minval=0)
                        validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                        if validasi in ['yes', 'y', 'ya']:
                            buku[5] = tahunBaru
                            print('Perubahan Data Berhasil Disimpan')
                            tampilkanBuku(daftarBuku)
                            break
                        elif validasi in ['no', 'n', 'tidak']:
                            print('Perubahan Data Batal Disimpan')
                        else:
                            print('Input Tidak Sesuai')

                    elif pilihan == 5:
                        jumlahBaru = validasiInt('Masukkan Jumlah Buku baru: ', minval=0)
                        validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                        if validasi in ['yes', 'y', 'ya']:
                            buku[6] = jumlahBaru
                            print('Perubahan Data Berhasil Disimpan')
                            tampilkanBuku(daftarBuku)
                            break
                        elif validasi in ['no', 'n', 'tidak']:
                            print('Perubahan Data Dibatalkan')
                        else:
                            print('Input Tidak Sesuai')    
                    elif pilihan == 6:
                        judulBaru = input('Masukkan Judul Buku baru: ').capitalize()
                        if any(buku[2].lower() == judulBaru.lower() for buku in daftarBuku.values()):
                            print(f"Buku berjudul {judulBaru} sudah ada. Silakan periksa kembali.")
                            return
                        pengarangBaru = input('Masukkan Pengarang Buku baru: ').capitalize()
                        kategoriBaru = input('Masukkan Kategori Buku baru: ').capitalize()
                        tahunBaru = validasiInt('Masukkan Tahun Terbit Buku baru: ', minval=0)
                        jumlahBaru = validasiInt('Masukkan Jumlah Buku baru: ', minval=0)

                        validasi = input('Apakah Yakin Untuk Menyimpan Data Baru? (Y/N): ').lower()
                        if validasi in ['yes', 'y', 'ya']:
                            buku[2], buku[3], buku[4], buku[5], buku[6] = judulBaru, pengarangBaru, kategoriBaru, tahunBaru, jumlahBaru
                            print('Perubahan Data Berhasil Disimpan')
                            tampilkanBuku(daftarBuku)
                            break
                        elif validasi in ['no', 'n', 'tidak']:
                            print('Perubahan Data Dibatalkan')
                        else:
                            print('Input Tidak Sesuai')
                    elif pilihan == 7:
                        break
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

                elif validasi in ['no', 'n', 'tidak']:
                    print('Data Batal Diupdate')
                    break
                else: 
                    print('Inputan Anda Tidak Sesuai')
            return
    print(f"Buku dengan ID {idBuku} tidak ditemukan.")

def hapusBuku():
    tampilkanBuku(daftarBuku)
    idBuku = validasiInt(title='Masukkan ID Buku: ')

    for key, val in list(daftarBuku.items()):
        if idBuku == val[1]:
            validasi = input('Apakah Anda Setuju Menghapus Buku? (Y/N): ').lower()
            if validasi in ['yes', 'y', 'ya']:
                del daftarBuku[key]
                print(f'Buku dengan ID {idBuku} berhasil dihapus.')
                break
            elif validasi in ['no', 'n', 'tidak']:
                print('Penghapusan Buku Dibatalkan.')
                break
            else:
                print('Inputan Anda Tidak Sesuai.')
                break
    else:
        print(f'Buku dengan ID {idBuku} tidak ditemukan.')

    for index, (key, val) in enumerate(daftarBuku.items(), start=1):
        val[0] = index

    tampilkanBuku(daftarBuku)