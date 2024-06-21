from tabulate import tabulate

daftarBuku = {
    'Dilan 1927' : [1, 'N001', 'Dilan 1927', 'Susanto', 'Novel', 15],
    'Boruto' : [2, 'K001', 'Boruto', 'Masashi Kisimoto', 'Komik', 2],
    'FIFA Rules and Regulations' : [3, 'S001', 'FIFA Rules and Regulations', 'FIFA', 'Olahraga', 1]
}

def validasiStr(title):
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silahkan inputkan hanya teks')
    return teks.capitalize()

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
        2. Tampilkan Beberapa Buku
        3. Kembali Ke Menu Awal
              ''')

        pilMenu = validasiInt(title="Masukkan angka sesuai menu: ")

        if pilMenu == 1:
            tampilkanBuku(daftarBuku)
        elif pilMenu == 2:
            pencarianBuku(daftarBuku)
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
        Tambahkan Buku

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

def tampilkanBuku(database ,header=['No', 'ID Buku', 'Judul', 'Author', 'Kategori', 'Jumlah']):
    print(tabulate(database.values(), headers=header, tablefmt='grid'))

def pencarianBuku(idBuku):
    idBuku = input('Masukkan ID Buku Yang Ingin Dicari: ').upper()
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
    id = input('Masukkan ID Buku: ').upper()
    judul = input('Masukkan Judul Buku: ')
    author = input('Masukkan Pengarang Buku: ')
    kategori = input('Masukkan Kategori Buku: ')
    jumlah = validasiInt(title='Masukkan Jumlah Buku: ', minval=0)

    # Check if ID already exists
    if id in buku in daftarBuku.values():
        print(f'Buku dengan ID {id} sudah ada. Silakan periksa kembali.')
        return

    # Menambahkan data ke database
    for key, buku in daftarBuku.items():
        if id in buku:
            buku[2] = judul  # Update title
            buku[3] = author  # Update author
            buku[4] = kategori  # Update category
            buku[5] = jumlah  # Update quantity
            print('Buku Berhasil Diupdate!')
            break
    else:
        noBaru = len(daftarBuku) + 1
        daftarBuku[judul] = [noBaru, id, judul, author, kategori, jumlah]
        print('Buku Berhasil Ditambahkan!')

    # Menampilkan database
    tampilkanBuku(daftarBuku)

def tambahBuku():
    id = input('Masukkan ID Buku: ').upper()
    judul = input('Masukkan Judul Buku: ')
    author = input('Masukkan Pengarang Buku: ')
    kategori = input('Masukkan Kategori Buku: ')
    jumlah = validasiInt(title='Masukkan Jumlah Buku: ', minval=0)

    # Menambahkan data ke database
    for buku in daftarBuku.items():
        if id in buku:
            buku[2] = judul  # Update title
            buku[3] = author  # Update author
            buku[4] = kategori  # Update category
            buku[5] = jumlah  # Update quantity
            print('Buku Berhasil Diupdate!')
            break
    else:
        noBaru = len(daftarBuku) + 1
        daftarBuku[judul] = [noBaru, id, judul, author, kategori, jumlah]
        print('Buku Berhasil Ditambahkan!')

    # Menampilkan database
    tampilkanBuku(daftarBuku)

    # # Menambahkan data ke database
    # for key, buku in daftarBuku.items():
    #     if id in buku:
    #         daftarBuku[key] = [id, judul, author, kategori, jumlah]
    #         print('Buku Berhasil Diupdate!')
    #         break
    # else:
    #     noBaru = len(daftarBuku) +1
    #     daftarBuku[judul] = [noBaru, id, judul, author, kategori, jumlah]
    #     print('Buku Berhasil Ditambahkan!')

    # # Menampilkan database
    # tampilkanBuku(daftarBuku)

def hapusBuku():
    tampilkanBuku(daftarBuku)

    idBuku = input('Masukkan ID Buku Yang Ingin Dihapus: ').upper()

    # Hapus Buku
    for key, val in daftarBuku.items():
        if idBuku == val[1]:
            del daftarBuku[key]
            print(f'Buku dengan ID {idBuku} berhasil dihapus.')
            break
        else:
            print(f'Buku dengan ID {idBuku} tidak ditemukan.')
   
    # Update urutan buku
    for index, (key, val) in enumerate(daftarBuku.items(), start=1):
        val[0] = index

    # Display the updated book list
    tampilkanBuku(daftarBuku)

# def hapusBuku():
#     tampilkanBuku(daftarBuku)

#     idBuku = input('Masukkan ID Buku Yang Ingin Dihapus: ').upper()

#     for key, val in daftarBuku.copy().items():
#         if idBuku == val[0]:
#             del daftarBuku[key]
#             break
#     else:
#         print('Buku Yang Anda Cari Tidak Ada')

#     #Memperbarui urutan buku
#     for key, val in enumerate(daftarBuku.values()):
#         if key != val[0]:
#             val[0]= key + 1
#             print('Buku Berhasil Di Hapus')
#             break

#     # Menampilkan database
#     tampilkanBuku(daftarBuku)