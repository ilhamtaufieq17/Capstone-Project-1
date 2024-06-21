import mylib 

def main():
    listMenu = '''
Selamat Datang di Perpustakaan!

List Menu:
1. Tampilkan Data Buku
2. Tambahkan Buku
3. Hapus Buku
4. Pinjam Buku
5. Kembalikan Buku
6. Exit
'''
    while True:
        print(listMenu)
        option =mylib.validasiInt(title='Masukkan Menu Yang Akan Dipilih (1-6): ')
        if option == 1:
            mylib.subMenuTampilkan()
        elif option == 2:
            mylib.subMenuTambahkan()
        elif option == 3:
            mylib.subMenuHapus()
        elif option == 4:
            mylib.borrow()
        elif option == 5:
            mylib.back()
        elif option == 6:
            break
        else:
            print('Nomor Yang Anda Inputkan Tidak Tersedia. Silahkan Input Kembali!')

main()