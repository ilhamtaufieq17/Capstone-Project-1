import mylib 

def main():
    listMenu = '''
Selamat Datang di Perpustakaan!

List Menu:
1. Tampilkan Data Buku
2. Tambahkan Buku
3. Update Buku
4. Hapus Buku
5. Exit
'''
    while True:
        print(listMenu)
        option =mylib.validasiInt(title='\nMasukkan Menu Yang Akan Dipilih (1-5): ')
        if option == 1:
            mylib.subMenuTampilkan()
        elif option == 2:
            mylib.subMenuTambahkan()
        elif option == 3:
            mylib.subMenuUpdate()
        elif option == 4:
            mylib.subMenuHapus()
        elif option == 5:
            break
        else:
            print('\nNomor Yang Anda Inputkan Tidak Tersedia. Silahkan Input Kembali!\n')

main()