# ============================================================
# BrINV — Brian Inventory Management System
# Capstone Project: Python Programming Module 1
# Case Study: FMCG Inventory / Warehouse Operations
#
# Business-focused enhancements:
# - Persistent local inventory data (JSON)
# - Inventory overview and low-stock monitoring
# - CRUD + product/batch traceability
# - Input validation and duplicate-code prevention
# - Stock value reporting
# ============================================================

import json
from pathlib import Path

APP_NAME = "BrINV"
COMPANY = "Unilever"
DATA_FILE = Path("inventory_data.json")
LOW_STOCK_THRESHOLD = 50
MAX_LOGIN_ATTEMPTS = 3

DEFAULT_INVENTORY = [
    {"kode": "UN40", "brand": "Blue Band Margarine", "stok": 100, "harga": 35000, "batch_awal": "AB030925A", "batch_terbaru": "AB031225B", "kategori": "FNB"},
    {"kode": "UN20", "brand": "Lifebuoy Body Wash", "stok": 150, "harga": 25000, "batch_awal": "BC020725A", "batch_terbaru": "BC080825B", "kategori": "Kesehatan Pribadi"},
    {"kode": "UN10", "brand": "Rinso Anti Noda", "stok": 200, "harga": 18000, "batch_awal": "CD200325C", "batch_terbaru": "CD250525C", "kategori": "Kebersihan"},
    {"kode": "UN30", "brand": "Clear Shampoo", "stok": 120, "harga": 32000, "batch_awal": "DE180525C", "batch_terbaru": "DE20025C", "kategori": "Kosmetik"},
]

CATEGORIES = ["FNB", "Kosmetik", "Kesehatan Pribadi", "Kebersihan"]


def load_inventory():
    """Load inventory from local JSON; use demo data when unavailable."""
    if not DATA_FILE.exists():
        return [item.copy() for item in DEFAULT_INVENTORY]

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except (OSError, json.JSONDecodeError):
        print("Data inventory tidak dapat dibaca. Menggunakan data demo.")

    return [item.copy() for item in DEFAULT_INVENTORY]


def save_inventory():
    """Persist current inventory to local JSON."""
    try:
        DATA_FILE.write_text(
            json.dumps(gudang, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
    except OSError as exc:
        print(f"Gagal menyimpan data inventory: {exc}")


gudang = load_inventory()


def input_int(prompt, allow_zero=True):
    """Read a valid non-negative integer."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0 or (value == 0 and not allow_zero):
                raise ValueError
            return value
        except ValueError:
            print("Masukkan angka yang valid.")


def input_required(prompt):
    """Read a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong.")


def choose_category():
    """Select a product category from the supported list."""
    print("\nKategori:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    while True:
        choice = input("Pilih kategori (1-4): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Pilihan kategori tidak valid.")


def confirm_action(prompt):
    """Read a yes/no confirmation."""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Masukkan y atau n.")


def login():
    """Authenticate the user with a three-attempt limit."""
    print(f"\n=== SELAMAT DATANG DI {APP_NAME} ===")
    print("Inventory Management System")

    for attempt in range(MAX_LOGIN_ATTEMPTS):
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username.casefold() == COMPANY.casefold() and password == "unv11":
            print(f"\nLogin berhasil. Selamat datang di {APP_NAME} - {COMPANY}.\n")
            return True

        print(
            "Username atau password salah. "
            f"Sisa percobaan: {MAX_LOGIN_ATTEMPTS - attempt - 1}"
        )

    print("Batas percobaan login tercapai. Akses ditolak.")
    return False


def main_menu():
    """Display the main application menu."""
    print(
        """
========== MAIN MENU - BrINV ==========
1. Inventory Overview
2. View & Report Inventory
3. Add New Product
4. Update Product
5. Delete Product
6. Exit
========================================
"""
    )


def display_product(item):
    """Display one product record in a readable format."""
    print(
        f"""
Kode Produk   : {item["kode"]}
Brand         : {item["brand"]}
Stok          : {item["stok"]}
Harga/Unit    : Rp{item["harga"]:,}
Batch Awal    : {item["batch_awal"]}
Batch Terbaru : {item["batch_terbaru"]}
Kategori      : {item["kategori"]}
Nilai Stok    : Rp{item["stok"] * item["harga"]:,}
"""
    )


def inventory_overview():
    """Summarize inventory scale, value, and low-stock exposure."""
    total_skus = len(gudang)
    total_units = sum(item["stok"] for item in gudang)
    total_value = sum(item["stok"] * item["harga"] for item in gudang)
    low_stock = [item for item in gudang if item["stok"] <= LOW_STOCK_THRESHOLD]

    print("\n=== INVENTORY OVERVIEW ===")
    print(f"Total SKU             : {total_skus}")
    print(f"Total Units on Hand   : {total_units:,}")
    print(f"Total Inventory Value : Rp{total_value:,}")
    print(f"Low-stock Threshold   : {LOW_STOCK_THRESHOLD} units")
    print(f"Low-stock SKU Count   : {len(low_stock)}")

    if low_stock:
        print("\nLow-stock items:")
        for item in low_stock:
            print(f"- {item['kode']} | {item['brand']} | {item['stok']} units")
    else:
        print("\nTidak ada item yang berada di bawah threshold.")


def lihat_produk():
    """Display all products."""
    if not gudang:
        print("\nInventory kosong.")
        return

    print("\n=== INVENTORY LIST ===")
    print("-" * 120)

    for item in gudang:
        print(
            f"Kode: {item['kode']:<5} | "
            f"Brand: {item['brand']:<23} | "
            f"Stok: {item['stok']:>4} | "
            f"Harga: Rp{item['harga']:>8,} | "
            f"Kategori: {item['kategori']}"
        )

    print("-" * 120)


def lacak_produk():
    """Search by brand, product code, or batch code."""
    keyword = input_required(
        "Masukkan brand, kode produk, atau batch: "
    ).casefold()

    results = [
        item
        for item in gudang
        if any(
            keyword in str(item[field]).casefold()
            for field in ("brand", "kode", "batch_awal", "batch_terbaru")
        )
    ]

    if not results:
        print("Produk tidak ditemukan.")
        return

    print(f"\n=== HASIL PELACAKAN ({len(results)} produk) ===")
    for item in results:
        display_product(item)


def sort_produk():
    """Sort inventory by price or stock."""
    print(
        """
=== SORTING INVENTORY ===
1. Harga: termurah -> termahal
2. Stok: terbanyak -> tersedikit
3. Kembali
"""
    )

    choice = input("Pilih menu (1-3): ").strip()

    if choice == "1":
        items = sorted(gudang, key=lambda x: x["harga"])
    elif choice == "2":
        items = sorted(gudang, key=lambda x: x["stok"], reverse=True)
    elif choice == "3":
        return
    else:
        print("Pilihan tidak valid.")
        return

    for item in items:
        print(
            f"{item['kode']} | {item['brand']} | "
            f"Stok: {item['stok']} | Harga: Rp{item['harga']:,}"
        )


def total_nilai_stok():
    """Calculate total inventory value."""
    total = sum(item["stok"] * item["harga"] for item in gudang)
    print(f"\nTotal nilai seluruh persediaan: Rp{total:,}")


def low_stock_report():
    """List products at or below the configured threshold."""
    items = sorted(
        (item for item in gudang if item["stok"] <= LOW_STOCK_THRESHOLD),
        key=lambda x: x["stok"],
    )

    print(f"\n=== LOW-STOCK REPORT (<= {LOW_STOCK_THRESHOLD} units) ===")

    if not items:
        print("Tidak ada produk yang memenuhi kondisi low-stock.")
        return

    for item in items:
        print(
            f"{item['kode']} | {item['brand']} | "
            f"Stok: {item['stok']} | Kategori: {item['kategori']}"
        )


def menu_read():
    """Display inventory reporting options."""
    while True:
        print(
            """
=== VIEW & REPORT INVENTORY ===
1. View all products
2. Trace product / batch
3. Sort inventory
4. Total inventory value
5. Low-stock report
6. Back to main menu
"""
        )

        choice = input("Pilih menu (1-6): ").strip()

        if choice == "1":
            lihat_produk()
        elif choice == "2":
            lacak_produk()
        elif choice == "3":
            sort_produk()
        elif choice == "4":
            total_nilai_stok()
        elif choice == "5":
            low_stock_report()
        elif choice == "6":
            break
        else:
            print("Pilihan tidak valid.")


def tambah_produk():
    """Add a product after validation."""
    print("\n=== TAMBAH PRODUK BARU ===")

    kode = input_required("Kode produk: ").upper()

    if any(item["kode"].upper() == kode for item in gudang):
        print("Kode produk sudah terdaftar.")
        return

    item = {
        "kode": kode,
        "brand": input_required("Nama brand: "),
        "stok": input_int("Jumlah stok: "),
        "harga": input_int("Harga per unit (Rp): "),
        "batch_awal": input_required("Kode batch awal: ").upper(),
        "batch_terbaru": input_required("Kode batch terbaru: ").upper(),
        "kategori": choose_category(),
    }

    gudang.append(item)
    save_inventory()
    print("Produk berhasil ditambahkan.")


def menu_create():
    """Create one or multiple products."""
    while True:
        print(
            """
=== CREATE PRODUCT ===
1. Add one product
2. Add multiple products
3. Back
"""
        )

        choice = input("Pilih menu (1-3): ").strip()

        if choice == "1":
            tambah_produk()
        elif choice == "2":
            count = input_int("Jumlah produk yang ingin ditambahkan: ")
            for _ in range(count):
                tambah_produk()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")


def ubah_produk():
    """Update a product by code; blank input keeps the old value."""
    print("\n=== UPDATE PRODUCT ===")

    kode = input_required("Kode produk: ").upper()
    item = next((x for x in gudang if x["kode"].upper() == kode), None)

    if item is None:
        print("Produk tidak ditemukan.")
        return

    print("\n=== DATA SAAT INI ===")
    display_product(item)
    print("Kosongkan input untuk mempertahankan nilai lama.\n")

    value = input("Brand baru: ").strip()
    if value:
        item["brand"] = value

    value = input("Stok baru: ").strip()
    if value:
        try:
            new_stock = int(value)
            if new_stock < 0:
                raise ValueError
            item["stok"] = new_stock
        except ValueError:
            print("Stok tidak diubah karena input tidak valid.")

    value = input("Harga baru (Rp): ").strip()
    if value:
        try:
            new_price = int(value)
            if new_price < 0:
                raise ValueError
            item["harga"] = new_price
        except ValueError:
            print("Harga tidak diubah karena input tidak valid.")

    value = input("Batch terbaru baru: ").strip()
    if value:
        item["batch_terbaru"] = value.upper()

    if input("Ubah kategori? (y/n): ").strip().lower() == "y":
        item["kategori"] = choose_category()

    save_inventory()

    print("\n=== DATA SETELAH UPDATE ===")
    display_product(item)
    print("Data produk berhasil diperbarui.")


def menu_update():
    """Display update options."""
    while True:
        print(
            """
=== UPDATE PRODUCT ===
1. Update product
2. Back
"""
        )

        choice = input("Pilih menu (1-2): ").strip()

        if choice == "1":
            ubah_produk()
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")


def hapus_satu():
    """Delete one product by code with confirmation."""
    kode = input_required("Kode produk yang ingin dihapus: ").upper()
    item = next((x for x in gudang if x["kode"].upper() == kode), None)

    if item is None:
        print("Produk tidak ditemukan.")
        return

    display_product(item)

    if confirm_action(f"Hapus {item['brand']}?"):
        gudang.remove(item)
        save_inventory()
        print("Produk berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def hapus_kategori():
    """Delete all products from a category with confirmation."""
    category = choose_category()
    matches = [item for item in gudang if item["kategori"] == category]

    if not matches:
        print(f"Tidak ada produk dengan kategori {category}.")
        return

    if confirm_action(f"Hapus seluruh produk kategori {category}?"):
        gudang[:] = [
            item for item in gudang if item["kategori"] != category
        ]
        save_inventory()
        print(f"{len(matches)} produk berhasil dihapus.")


def hapus_semua():
    """Delete all products with confirmation."""
    if not gudang:
        print("Inventory sudah kosong.")
        return

    if confirm_action("Yakin ingin menghapus SEMUA data inventory?"):
        gudang.clear()
        save_inventory()
        print("Semua data inventory berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def menu_delete():
    """Display delete options."""
    while True:
        print(
            """
=== DELETE PRODUCT ===
1. Delete one product
2. Delete by category
3. Delete all products
4. Back
"""
        )

        choice = input("Pilih menu (1-4): ").strip()

        if choice == "1":
            hapus_satu()
        elif choice == "2":
            hapus_kategori()
        elif choice == "3":
            hapus_semua()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid.")


def run_app():
    """Run the BrINV application."""
    if not login():
        return

    save_inventory()

    while True:
        main_menu()
        choice = input("Pilih menu (1-6): ").strip()

        if choice == "1":
            inventory_overview()
        elif choice == "2":
            menu_read()
        elif choice == "3":
            menu_create()
        elif choice == "4":
            menu_update()
        elif choice == "5":
            menu_delete()
        elif choice == "6":
            print("\nTerima kasih telah menggunakan BrINV.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    run_app()
