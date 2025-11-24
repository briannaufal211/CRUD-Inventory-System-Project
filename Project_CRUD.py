# ============================================================
# CAPSTONE PROJECT MODULE 1
# Tema: Aplikasi BrINV (Brian Inventory Management System)
# Studi Kasus: Sistem Inventory untuk Produk Perusahaan UNILEVER 
# Fitur: CRUD + Validasi Input + Sorting + Login + Traceability 
# ============================================================

# LOGIN SYSTEM (Security)
# -----------------------------
def login():
    """Fungsi login untuk keamanan awal program.
    User hanya bisa masuk jika username dan password benar.
    Dibatasi 3 kali percobaan login."""

    print("=== Selamat Datang di BrINV ===")
    percobaan_maks = 3
    for percobaan in range(percobaan_maks,0,-1):
        username = input("Masukkan username: ").capitalize()
        password = input("Masukkan password: ")

        # Validasi username dan password
        if username == "Unilever" and password == "unv11":
            print("Login berhasil! Selamat datang di BrINV APP - Unilever.\n")
            return True
        else:
            print(f"Username atau password salah! Sisa Percobaan Anda : {percobaan-1}")

    # Jika gagal 3 kali
    print("Anda telah melebihi batas percobaan login. Akses ditolak.")
    return False


# DATA DUMMY (List of Dictionary)
# -----------------------------
# Simulasi database produk di gudang
# -----------------------------
gudang = [
     {"kode": "UN40", "brand": "Blue Band Margarine", "stok": 100, "harga": 35000, "batch_awal": "AB030925A",
     "batch_terbaru": "AB031225B","kategori": "FNB" },
     {"kode": "UN20", "brand": "Lifebuoy Body Wash", "stok": 150, "harga": 25000, "batch_awal": "BC020725A",
     "batch_terbaru": "BC080825B", "kategori": "Kesehatan Pribadi"},
    {"kode": "UN10", "brand": "Rinso Anti Noda", "stok": 200, "harga": 18000, "batch_awal": "CD200325C",
     "batch_terbaru": "CD250525C", "kategori": "Kebersihan"},
    {"kode": "UN30", "brand": "Clear Shampoo", "stok": 120, "harga": 32000, "batch_awal": "DE180525C",
     "batch_terbaru": "DE20025C","kategori": "Kosmetik"} 
]

# -----------------------------
# MENU UTAMA
# -----------------------------
def main_menu():
    """Menampilkan daftar menu utama program BrINV.""" 
    print("""
========== MAIN MENU - BrINV UNILEVER ==========
1. Lihat & Laporan Produk (Read)
2. Tambah Produk Baru (Create)
3. Ubah Data Produk (Update)
4. Hapus Produk (Delete)
5. Keluar Aplikasi
===============================================
""")

    
# -----------------------------
# VALIDASI INPUT
# -----------------------------
def input_int(pesan):
    """ Validasi agar input hanya bilangan positif"""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 0:
                print("Nilai tidak boleh negatif!")
            else:
                return nilai
        except:
            print("Masukkan angka yang valid!")


# -----------------------------
# READ (Lihat Data Produk)
# -----------------------------
def menu_read():
    """Menampilkan sub-menu untuk fitur Read (lihat/laporan data)."""
    while True:
        print("""
=== MENU LIHAT & LAPORAN PRODUK ===
1. Lihat semua data produk
2. Lacak produk (berdasarkan brand/batch)
3. Urutkan produk (harga/stok)
4. Rekap nilai total persediaan
5. Kembali ke menu utama
""")
        pilih = input("Pilih menu (1-5): ")

        if pilih == "1":
            lihat_produk()
        elif pilih == "2":
            lacak_produk()
        elif pilih == "3":
            sort_produk()
        elif pilih == "4":
            total_nilai_stok()
        elif pilih == "5":
            main_menu()
            break
        else:
            print("Pilihan tidak valid!")

# -----------------------------
# TAMPIL SEMUA PRODUK
# -----------------------------
def lihat_produk():
    """Menampilkan semua produk yang tersimpan di gudang."""
    if not gudang:
        print("\nData gudang masih kosong.")
        return # fungsi akan stop 
    else:
        print("\n=== DAFTAR PRODUK UNILEVER (BrINV System) ===")
    print("=====================================================================================================================================================")
    for p in gudang:
        print(f"Kode: {p['kode']} | brand: {p['brand']} | Stok: {p['stok']} | Harga: Rp{p['harga']:,} | Batch_awal: {p['batch_awal']} | Batch Terbaru: {p['batch_terbaru']} | Kategori: {p['kategori']}")
    print("=====================================================================================================================================================")

# -----------------------------
# PELACAKAN DATA PRODUK
# -----------------------------
def lacak_produk():
    """Mencari produk berdasarkan nama brand atau kode batch."""
    kata = input("Masukkan brand produk atau kode batch awal: ").lower()
    hasil = []

    # Pencarian data yang cocok
    for p in gudang:
        if kata in p['brand'].lower() or kata in p['batch_awal'].lower():
            hasil.append(p)
    
    # Menampilkan hasil
    if hasil:
        print("\n=== HASIL PELACAKAN PRODUK ===")
        for p in hasil:
            print(f"""
Kode: {p['kode']}
brand: {p['brand']}
Stok: {p['stok']}
Harga: Rp{p['harga']:,}
Batch Awal: {p['batch_awal']}
Batch Terbaru: {p['batch_terbaru']}
Kategori: {p['kategori']}
""")
    else:
        print("Produk tidak ditemukan.")

# -----------------------------
# SORTING DATA PRODUK
# -----------------------------

def sort_produk():
    """Mengurutkan produk berdasarkan harga atau stok."""
    print("""
=== SORTING DATA PRODUK ===
1. Urutkan berdasarkan harga (termurah -> termahal)
2. Urutkan berdasarkan stok (terbanyak -> tersedikit)
3. Back to main menu
""")
    pilih = input("Pilih menu (1-3): ")

    if pilih == "1":
        # urut berdasarkan harga
        urutan = sorted(gudang, key=lambda x: x["harga"])
        for p in urutan:
            print(f"{p['brand']} | Rp{p['harga']:,} | Stok: {p['stok']}")

    elif pilih == "2":
        # urut berdasarkan stok
        urutan = sorted(gudang, key=lambda x: x["stok"], reverse=True)
        for p in urutan:
            print(f"{p['brand']} | Stok: {p['stok']} | Harga: Rp{p['harga']:,}")
    
    elif pilih == "3":
        print(main_menu())
        
    else:
        print("Pilihan tidak valid!")
    
# -----------------------------
# LAPORAN NILAI STOK
# -----------------------------
def total_nilai_stok():
    """Menghitung total nilai seluruh stok di gudang."""
    total = 0
    for p in gudang:
        total += p['stok'] * p['harga']
    print(f"\nTotal nilai seluruh stok: Rp{total:,}")

# -----------------------------
# CREATE (Tambah Produk Baru)
# -----------------------------
def menu_create():
    """Menampilkan menu tambah produk."""
    while True:
        print("""
=== MENU TAMBAH PRODUK ===
1. Tambah satu produk
2. Tambah beberapa produk sekaligus
3. Kembali ke menu utama
""")
        pilih = input("Pilih menu (1-3): ")

        if pilih == "1":
            tambah_produk()
        elif pilih == "2":
            jumlah = input_int("Berapa produk yang ingin ditambahkan?: ")
            for _ in range(jumlah):
                tambah_produk()
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")

def tambah_produk():
    """Fungsi untuk menambahkan satu produk baru ke gudang."""
    print("\n=== TAMBAH PRODUK BARU ===")
    kode = input("Masukkan kode produk (contoh: UN..): ").upper()

    # Cegah duplikasi kode
    for p in gudang:
        if p["kode"] == kode:
            print("Kode produk sudah terdaftar!")
            return
    
    # Input data produk baru
    brand = input("Nama brand: ")
    stok = input_int("Jumlah stok: ")
    harga = input_int("Harga per unit (Rp): ") 
    batch_awal = input("Kode batch awal produk: ").upper()
    batch_terbaru = input("Kode batch terbaru produk: ").upper()
    kategori = input("Kategori (FNB/Kosmetik/Kesehatan Pribadi/Kebersihan): ") 

    # Tambahkan ke gudang
    gudang.append({
        "kode": kode,
        "brand": brand,
        "stok": stok,
        "harga": harga,
        "batch_awal": batch_awal,
        "batch_terbaru": batch_terbaru,
        "kategori": kategori
    })
    print("Data produk berhasil ditambahkan!")


# -----------------------------
# UPDATE (Ubah Data Produk)
# -----------------------------

def menu_update():
    """Menampilkan menu ubah data produk."""
    while True:
        print("""
=== MENU UBAH DATA PRODUK ===
1. Ubah data produk
2. Kembali ke menu utama
""")
        pilih = input("Pilih menu (1-2): ")

        if pilih == "1":
            ubah_produk()
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")
            
def ubah_produk():
    """Mengubah data produk berdasarkan kode."""
    kode = input("Masukkan kode produk: ").upper()
    for p in gudang:
        if p["kode"] == kode:
            # Tampilkan data lama
            print("\n=== DATA LAMA PRODUK ===")
            print(f"Kode Produk   : {p['kode']}")
            print(f"Brand         : {p['brand']}")
            print(f"Stok          : {p['stok']}")
            print(f"Harga         : Rp{p['harga']:,}")
            print(f"Batch Awal    : {p['batch_awal']}")
            print(f"Batch Terbaru : {p['batch_terbaru']}")
            print(f"Kategori      : {p['kategori']}")

            # Input data baru
            print("\n=== MASUKKAN DATA BARU ===")
            p["brand"] = input("Brand baru (kosongkan jika tidak diubah): ") or p["brand"]
            p["stok"] = input_int("Stok baru (atau tidak diubah): ")
            p["harga"] = input_int("Harga baru (atau tidak diubah): ")
            p["batch_terbaru"] = input("Batch Terbaru (kosongkan jika tidak diubah): ") or p["batch_terbaru"]
            p["kategori"] = input("Kategori baru (kosongkan jika tidak diubah): ") or p["kategori"]

            # Tampilkan data baru
            print("\nData produk berhasil diperbarui!")
            print("=== DATA BARU PRODUK ===")
            print(f"Kode Produk   : {p['kode']}")
            print(f"Brand         : {p['brand']}")
            print(f"Stok          : {p['stok']}")
            print(f"Harga         : Rp{p['harga']:,}")
            print(f"Batch Awal    : {p['batch_awal']}")
            print(f"Batch Terbaru : {p['batch_terbaru']}")
            print(f"Kategori      : {p['kategori']}")
            print("=============================================")
            return
    print("Produk tidak ditemukan.")


# -----------------------------
# DELETE (Hapus Produk)
# -----------------------------
def menu_delete():
    """Menampilkan menu hapus data produk."""
    while True:
        print("""
=== MENU HAPUS PRODUK ===
1. Hapus satu produk
2. Hapus berdasarkan kategori
3. Hapus semua produk
4. Kembali ke menu utama
""")
        pilih = input("Pilih menu (1-4): ")

        if pilih == "1":
            hapus_satu()
        elif pilih == "2":
            hapus_kategori()
        elif pilih == "3":
            hapus_semua()
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")


def hapus_satu():
    """Menghapus satu produk berdasarkan kode."""
    kode = input("Masukkan kode produk yang ingin dihapus: ").upper()
    for p in gudang:
        if p["kode"] == kode:
            konfirmasi = input(f"Yakin ingin menghapus {p['brand']}? (y/n): ").lower()
            if konfirmasi == "y":
                gudang.remove(p)
                print("Produk berhasil dihapus.")
            elif konfirmasi == "n":
                print("Penghapusan dibatalkan.")
            else:
                print("Konfirmasi tidak valid!")
            return
    print("Produk tidak ditemukan.")


def hapus_kategori():
    """Menghapus semua produk berdasarkan kategori."""
    kategori = input("Masukkan kategori yang ingin dihapus: ").capitalize()
    global gudang
    before = len(gudang)
    gudang = [p for p in gudang if p["kategori"].capitalize() != kategori]
    after = len(gudang)
    if before != after:
        print(f"{before - after} produk dari kategori {kategori} dihapus.")
    else:
        print("Tidak ada produk dengan kategori tersebut.")

def hapus_semua():
    """Menghapus seluruh data produk di gudang (dengan konfirmasi)."""
    while True:
        konfirmasi = input("Yakin ingin menghapus SEMUA data produk? (y/n): ").lower()
        if konfirmasi == "y":
            gudang.clear()
            print("Semua data produk berhasil dihapus.")
            break
        elif konfirmasi == "n":
            print("Penghapusan dibatalkan.")
            break
        else:
            print("Konfirmasi tidak valid! Ulangi konfirmasi")
         

# -----------------------------
# PROGRAM UTAMA
# -----------------------------
if login():
    while True:
        main_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            menu_read()
        elif pilihan == "2":
            menu_create()
        elif pilihan == "3":
            menu_update()
        elif pilihan == "4":
            menu_delete()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BrINV System!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


