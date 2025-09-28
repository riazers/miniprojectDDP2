#   Mini Project Playlist Lagu
#   Nama Riaz Ramadhan Al Fattah
#   NIM 2509116106
#   Kelas C 

#Dictionary List
lagu = {
    "pop": [
        "As It Was - Harry Styles", 
        "About Damn Time - Lizzo", 
        "Bad Habit - Steve Lacy"
    ],
    "indie": [
        "Anti-Hero - Taylor Swift", 
        "Fallen Star - The Neighbourhood", 
        "Made You Look - Meghan Trainor"
    ],
    "rnb": [
        "Blinding Lights - The Weeknd", 
        "Twenties - GIVEON", 
        "Peaches - Justin Bieber"
    ]
}

akun = {
    "riaz": "ganteng",
    "admin": "admin123"
}

def login_pengguna():
    print("=== Sistem Login Playlist Riaz ===")
    for i in range(3):  # Maksimal 3 kali percobaan
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in akun and akun[username] == password:
            print(f"Login berhasil! Selamat datang Pengguna, {username.capitalize()}!\n")
            return username
        else:
            print("Username atau password salah. Coba lagi.\n")
    print("Terlalu banyak percobaan gagal. Program keluar.")
    exit()

def login_admin():
    print("=== Sistem Login Admin ===")
    for i in range(3):  # Maksimal 3 kali percobaan
        username = input("Masukkan username admin: ")
        password = input("Masukkan password: ")
        if username == "admin" and username in akun and akun[username] == password:
            print(f"Login berhasil! Selamat datang, {username.capitalize()}!\n")
            return username
        else:
            print("Username atau password salah. Coba lagi.\n")
    print("Terlalu banyak percobaan gagal. Program keluar.")
    exit()


#Program Def Agar singkat 
def putar_genre(genre):
    genre = genre.lower()
    if genre in lagu:
        print(f"Memutar lagu {genre.capitalize()}: ", lagu[genre])
        tambah = input(f"Ingin menambah lagu {genre.capitalize()}? (Ya/Tidak): ")
        if tambah.lower() == "ya":
            lagu_baru = input("Masukkan judul lagu baru: ")
            lagu[genre].append(lagu_baru)
            print(f"Playlist {genre.capitalize()} terbaru: ", lagu[genre])
        
        hapus = input(f"Ingin menghapus lagu {genre.capitalize()}? (Ya/Tidak): ")
        if hapus.lower() == "ya":
            lagu_hapus = input("Masukkan judul lagu yang ingin dihapus: ")
            if lagu_hapus in lagu[genre]:
                lagu[genre].remove(lagu_hapus)
                print(f"Playlist {genre.capitalize()} terbaru: ", lagu[genre])
            else:
                print("Lagu tidak ditemukan dalam playlist.")
        else:
            print(f"Terima kasih. Selamat mendengarkan lagu {genre.capitalize()}!")
    else:
        print("Genre tidak tersedia.")

# Main loop
while True:
    print("=== Playlist Lagu Riaz ===")
    print("1. Pop")
    print("2. Indie")
    print("3. RnB")
    print("4. Keluar")
    print("5. Admin Terminal")
    pilihan = input("Masukkan Genre Playlist Lagu yang Ingin Diputar, Atau Pilih Menu Lain: ").lower()
    if pilihan == "1" or pilihan == "Pop":
        login_pengguna()
        putar_genre("Pop")
    elif pilihan == "2" or pilihan == "Indie":
        login_pengguna()
        putar_genre("Indie")
    elif pilihan == "3" or pilihan == "RnB":
        login_pengguna()
        putar_genre("RnB")
    elif pilihan == "4" or pilihan == "keluar":
        print("Keluar dari program. Sampai jumpa!")
        break
    elif pilihan == "5" or pilihan == "Admin Terminal":
        login_admin()
        admin_command1 = input("Hapus Playlist Secara Menyeluruh Ya/Tidak: ")
        if admin_command1.lower() == "ya":
            while True:
                try:
                    hapus_playlist = input("Masukkan Nama Playlist Yang Ingin Dihapus: ")
                    if hapus_playlist in lagu:
                        del lagu[hapus_playlist]
                        print(f"Playlist '{hapus_playlist}' berhasil dihapus beserta semua lagunya.")
                        break
                    else:
                        print(f"Playlist '{hapus_playlist}' tidak ditemukan.")
                except ValueError:
                    print("\ntidak bisa keluar dari program ini (Selesaikan)")
                    continue
    else:
        print("Pilihan tidak valid.")
