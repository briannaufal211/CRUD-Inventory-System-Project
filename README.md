# BrINV (Brian Inventory System)
BrINV App is a **Python-based inventory management simulation** designed for **FMCG (Fast Moving Consumer Goods)** companies.  
This system is developed as a **Capstone Project for Python Programming Module 1**, using **Unilever products as a case study**.  


## Business Understanding
Inventory management remains a crucial challenge in many FMCG companies.  
Without a proper digital system, staff often struggle to track product data, stock levels, or production batches accurately.  
BrINV provides a simplified simulation to demonstrate how an automated system can reduce manual workload, human errors, and inefficiencies in tracking inventory movement. It enables users to manage warehouse data interactively, including adding, updating, deleting, sorting, and tracking products — all within a terminal-based interface.

---

**Benefits:** 
- Develop a functional **inventory management system** to simulate real-world warehouse operations.  
- Practice implementing **Python fundamentals**, including loops, conditionals, functions, and input validation.  
- Demonstrate the use of **CRUD operations (Create, Read, Update, Delete)** in data management.   
- Provide users with a simplified digital system to monitor inventory efficiently.  

---

## Users
This program is designed for:
- **Students and learners** studying Python programming.  
- **Developers** who want to understand warehouse management logic.  
- **Instructors or evaluators** assessing CRUD, validation, and modular programming skills.  
- **Warehouse staff or administrators** seeking to simulate basic inventory processes.  

---

## System Features
| Feature | Description |
|----------|--------------|
| **Login System** | Secures system access with username/password authentication and retry limits. |
| **Create** | Allows adding one or multiple new products to the warehouse database. |
| **Read** | Displays all product data, tracks items by name or batch, and generates stock value reports. |
| **Update** | Updates product details such as stock, price, category, or batch code. |
| **Delete** | Removes products based on code, category, or all records. |
| **Sorting** | Sorts products by price or stock quantity. |
| **Stock Value Report** | Calculates the total monetary value of all items in stock. |

---

## Data Structure Example
```python
gudang = [
    {
        "kode": "UN40",
        "brand": "Blue Band Margarine",
        "stok": 100,
        "harga": 35000,
        "batch_awal": "AB030925A",
        "batch_terbaru": "AB031225B",
        "kategori": "FNB"
    }
]
```
**Explanation:**
- `kode` → Unique product ID (Primary Key)  
- `brand` → Product name  
- `stok` → Quantity in stock  
- `harga` → Unit price  
- `batch_awal` / `batch_terbaru` → Production batch tracking  
- `kategori` → Product category  

---

## How to Run the Program
1. Ensure **Python 3.x** is installed on your computer.  
2. Open the project folder in your IDE (VS Code, PyCharm, or IDLE).  
3. Run the program using the command:
   ```bash
   Project_CRUD.py
   ```
4. Login using default credentials:
   - **Username:** `Unilever`  
   - **Password:** `UNV1`
5. Follow the interactive menu to use BrINV features.

---

## Example Output
```
=== Welcome to BrINV ===
Enter username: Unilever
Enter password: INVunil1
Login successful! Welcome to BrINV APP - Unilever.

========== MAIN MENU ==========
1. View & Report Products
2. Add New Product
3. Update Product Data
4. Delete Product
5. Exit Application
===============================
Select menu (1-5):
```

---

## Program Logic Flow
1. User logs in to the system.  
2. After successful login, the **Main Menu** is displayed.  
3. User selects a menu option (CRUD, Sort, Report).  
4. The selected function interacts with the `gudang` list (warehouse database).  
5. System loops until the user chooses to exit.

---

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [brian.naufal5420@gmail.com] or submit an issue if you encounter any problems or have suggestions for improvements.

---

## Developer
**Brian Naufal**  
Purwadhika Student
Capstone Project 1: Python Fundamental Programming  
Year: 2025
