def main():
    print("=============================================")
    print("     Selamat datang di Aplikasi Monitoring    ")
    print("             Akademik Mahasiswa           ")
    print("           Universitas Esa Unggul      ")
    print("=============================================")
    print("                 ATTENTION                              ")

    print("         Silahkan pilih menu di bawah ini\n")
    print("                     |           ")
    print("                     |           ")
    print("                  \  |  /         ")
    print("                   \ | /          ")
    print("                    \|/           ")
    print("                     v            \n")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
ascii_art = """
  _        _   _                            _
  \ \      / /_| | __ _  _ _ __   _  | |
   \ \ /\ / / _ \ |/ _/ _ \| ' ` _ \ / _ \ | |
    \ V  V /  _/ | (| () | | | | | |  _/ |_|
     \_/\_/ \__||\__\_/|| || ||\__| ()
"""
main()
print(ascii_art)

def menu_utama():
    print("+=======================================+")
    print("|         MAIN MENU APLICATION          |")
    print("+=======================================+")
    print("1. Admin")
    print("2. Mahasiswa ")
    print("3. Keluar dari aplikasi")
    print("+====================================+")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        login()
    elif pilihan == "2":
        mahasiswa()
    elif pilihan == "3":
        print("Terima kasih!")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_utama()

def pilihan_1():
    print("ANDA MEMILIH PILIHAN 1 UNTUK ITU HARAP ENTER UNTUK KE MENU BERIKUTNYA!!\n")
    # Tambahkan logika atau fungsi yang sesuai dengan pilihan 1 di sini
    # ...

def pilihan_2():
    print("Anda memilih Pilihan 2")
    # Tambahkan logika atau fungsi yang sesuai dengan pilihan 2 di sini
def login():
    print("==== LOGIN ====")
    username = input("Username: ")
    password = input("Password: ")
    #cek username dan password
    if username == "esgul" and password == "unggul":
      menu_admin()
    else:
      print("Username/Password Salah!")
      
def menu_admin():
    print("+=======================================+")
    print("|         MENU ADMIN KAMPUS             |")
    print("+=======================================+")
    print("1. Tambah Mahasiswa")
    print("2. Tambah Dosen")
    print("3. Lihat Data Mahasiswa")
    print("4. Lihat Data Dosen")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan == "2":
        tambah_dosen()
    elif pilihan == "3":
        lihat_data_mahasiswa()
    elif pilihan == "4":
        lihat_data_dosen()
    elif pilihan == "5":
        menu_utama()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_admin()
        
data_mahasiswa = []

def tambah_mahasiswa():
    print("========================")
    print("|  TAMBAH MAHASISWA    |")
    print("========================")
    #YANG DI ROMBAK ARYA KEMUNGKINAN SALAAH
    while True:
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        fakultas = input("Masukan Fakultas: ")
        prodi = input("Masukkan program studi mahasiswa: ")
        kampus = input("Masukan lokasi kampus: ")
    
        # Simpan data mahasiswa ke dalam struktur data yang sesuai
        mahasiswa = {
            'nama': nama,
            'nim': nim,
            'fakultas' : fakultas,
            'prodi': prodi,
            'kampus': kampus
        }
    
        # Tambahkan data mahasiswa ke dalam daftar mahasiswa atau database
        data_mahasiswa.append(mahasiswa)
    
        # Tampilkan konfirmasi bahwa mahasiswa telah ditambahkan
        print("Mahasiswa {} dengan NIM {} berhasil ditambahkan.".format(nama, nim))
        #codingan dari arya
        pilihan = input("Apakah anda ingin melanjutkannya? (ya/tidak)")
        if pilihan == "ya":
            continue
        elif pilihan == "tidak":
            menu_admin()
        else:
            print("pilihan tidak ada")

data_dosen = []
            
def tambah_dosen():
    print("=== TAMBAH DOSEN ===")
    while True:
        nama = input("Masukkan nama dosen: ")
        nip = input("Masukkan NIP dosen: ")
        jabatan = input("Masukkan jabatan dosen: ")
    
        # Simpan data dosen ke dalam struktur data yang sesuai
        dosen = {
            'nama': nama,
            'nip': nip,
            'jabatan': jabatan
        }
    
        # Tambahkan data dosen ke dalam daftar dosen atau database
    
        # Tampilkan konfirmasi bahwa dosen telah ditambahkan
        print("Dosen {} dengan NIP {} berhasil ditambahkan.".format(nama, nip))
        
        data_dosen.append(dosen)
        
        pilihan = input("Apakah anda ingin melanjutkannya? (ya/tidak)")
        if pilihan == "ya":
            continue
        elif pilihan == "tidak":
            menu_admin()
        else:
            print("pilihan tidak ada")
            
def lihat_data_mahasiswa():
    print("=== DATA MAHASISWA ===")
    # Periksa apakah ada data mahasiswa
    if len(data_mahasiswa) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        for mahasiswa in data_mahasiswa:
            print("Nama: ", mahasiswa['nama'])
            print("NIM: ", mahasiswa['nim'])
            print("Fakultas", mahasiswa['fakultas'])
            print("Program Studi: ", mahasiswa['prodi'])
            print("Lokasi: ", mahasiswa['kampus'])
            print("--------------------")
            while True:
                pilihan = input("ketik b untuk kembali ke menu admin: ")
                if pilihan == "b":
                    menu_admin()
                else:
                    print("Wajib ketik b")
                    continue
                break
            
def lihat_data_dosen():
    print("=== DATA DOSEN ===")
    # Periksa apakah ada data mahasiswa
    if len(data_dosen) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        for dosen in data_dosen:
            print("Nama: ", dosen['nama'])
            print("NIP: ", dosen['nip'])
            print("Jabatan", dosen['jabatan'])
            print("--------------------")
            while True:
                pilihan = input("ketik b untuk kembali ke menu admin: ")
                if pilihan == "b":
                    menu_admin()
                else:
                    print("Wajib ketik b")
                    continue
                break
            
def update_ipk(data_matkul,jumlah_sks,nilai):
    total_sks = 0
    total_bobot = 0
    for mata_kuliah in data_matkul:
        sks = jumlah_sks
        total_nilai = nilai
        total_sks += sks
        total_bobot += sks * total_nilai

    if total_sks != 0:
        ipk = total_bobot / total_sks
        return ipk

data_matkul = []

def tambah_matakuliah():
    nama_matkul = input("Masukan nama mata kuliah: ")
    jumlah_sks = int(input("Masukan jumlah sks: "))
    nilai = int(input("Masukan nilai: "))
    total_pertemuan = int(input("Masukan total pertemuan: "))
    total_kehadiran = int(input("Masukan total kehadiran dari total pertemuan: "))
    
    matkul = {
        'matkul': nama_matkul,
        'jumlah_sks': jumlah_sks,
        'nilai': nilai,
        'total_pertemuan': total_pertemuan,
        'total_kehadiran': total_kehadiran
    }
    print("Mata kuliah berhasil ditambahkan!")
    data_matkul.append(matkul)

def presentasi_kehadiran(pertemuan, kehadiran):
    tidak_hadir = pertemuan - kehadiran
    return (kehadiran/pertemuan) * 100
    

def grading(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 75:
        return"A-"
    elif nilai >= 70:
        return "B+"
    elif nilai >= 65:
        return "B"
    elif nilai >= 60:
        return "B-"
    elif nilai >= 55:
        return "C+"
    elif nilai >= 50:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

def lihat_informasi_mahasiswa():
    print("=== INFORMASI MAHASISWA ===")
    # Periksa apakah ada data mahasiswa
    if len(data_matkul) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        for matkul in data_matkul:
            nilai = matkul['nilai']
            pertemuan = matkul['total_pertemuan']
            kehadiran = matkul['total_kehadiran']
            jumlah_sks = matkul['jumlah_sks']
            nilai = matkul['nilai']
            print("Matkul: ", matkul['matkul'])
            print("Jumlah SKS: ", matkul['jumlah_sks'])
            print("Nilai", matkul['nilai'])
            print("Grade: ", grading(nilai))
            print("Total Pertemuan", matkul['total_pertemuan'])
            print("Total Kehadiran", matkul['total_kehadiran'])
            print("Presentase Kehadiran:", presentasi_kehadiran(pertemuan, kehadiran))
            print("IPK: ", update_ipk(data_matkul,jumlah_sks,nilai))
            print("--------------------")

def is_data_empty(data):
    if not data:
        return True
    elif isinstance(data, str) and data.strip() == "":
        return True
    elif isinstance(data, (list, dict, set, tuple)) and len(data) == 0:
        return True
    else:
        return False
            
def mahasiswa():
    while True:
        nama = input("silahkan Masukkan nama anda: ")
        if is_data_empty(nama):
            print("Data Nama Kosong!")
            continue
        else:
            while True:
              nim = input("silahkan Masukkan NIM mahasiswa anda: ")
              if is_data_empty(nim):
                  print("Data NIM Kosong!")
                  continue
              else:
                  while True:
                    fakultas = input("silahkan masukan Fakultas anda: ")
                    if is_data_empty(fakultas):
                      print("Data fakultas Kosong!")
                    else:
                      while True:
                        prodi = input("silahkan Masukkan program studi anda: ")
                        if is_data_empty(prodi):
                          print("Data Prodi Kosong!")
                        else:
                          print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                          while True:
                            print("\nMenu:")
                            print("1. Tambah Mata Kuliah")
                            print("2. Tampilkan Informasi Mahasiswa")
                            print("3. Keluar")
                            pilihan = input("Masukkan pilihan menu: ")
    
                            if pilihan == "1":
                                tambah_matakuliah()
                            elif pilihan == "2":
                              lihat_informasi_mahasiswa()
                            elif pilihan == "3":
                              print("Terima kasih telah menggunakan aplikasi ini!")
                              break
                            else:
                              print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

menu_utama()
