# Nama Riaz Ramadhan Al Fattah
# NIM: 2509116106
# Kelas C

print("=== Playlist Lagu Riaz ===")

print("1. Pop")
print("2. Indie")
print("3. RnB")
print("4. Keluar")
print("5. Admin Terminal")

# Daftar lagu dalam setiap genre (List Dictionary)
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
    "riaz": "12345",
    "admin": "admin123"
}

while True:
    putar = (input(f"Masukkan Genre Playlist Lagu yang Ingin Diputar: "))

    if putar == "Pop" or putar == "1":
        print("Memutar lagu Pop: ", lagu["pop"])
        tambah_pop = str(input("Ingin menambah lagu Pop? (Ya/Tidak): "))
        if tambah_pop == "Ya":
            lagu_baru = str(input("Masukkan judul lagu baru: "))
            lagu["pop"].append(lagu_baru)
            print("Playlist Pop terbaru: ", lagu["pop"])
        hapus_pop = str(input("Ingin menghapus lagu Pop? (Ya/Tidak): "))
        if hapus_pop == "Ya":
            lagu_hapus = str(input("Masukkan judul lagu yang ingin dihapus: "))
            if lagu_hapus in lagu["pop"]:
                lagu["pop"].remove(lagu_hapus)
                print("Playlist Pop terbaru: ", lagu["pop"])
            else:
                print("Lagu tidak ditemukan dalam playlist.")
        elif tambah_pop == "Tidak":
            print("Terima kasih. Selamat mendengarkan lagu Pop!")

    


