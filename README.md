# BrINV — Brian Inventory System

**Python-based Inventory Management System simulation for FMCG / warehouse operations**

> Capstone Project — Python Programming Module 1  
> Case Study: Unilever products  
> Technology: Python 3.x + local JSON persistence

## Project Overview

BrINV is a Python-based inventory-management simulation built around a simplified FMCG warehouse workflow.

The system demonstrates how a lightweight digital process can support:

- product master-data management,
- stock visibility,
- product and batch traceability,
- inventory valuation,
- low-stock monitoring,
- input validation,
- and CRUD operations.

This is a portfolio simulation, not a production warehouse-management system.

## Business Context

Inventory teams need reliable access to product information, stock quantities, pricing, categories, and batch references.

BrINV models a simplified digital workflow:

**Manage Inventory → Monitor Stock → Trace Product / Batch → Review Inventory Value → Identify Low Stock**

## Business Objective

Improve visibility of basic warehouse information and simplify routine inventory-management activities within the simulated process.

## Functional Scope

### Authentication
- Username/password login
- Maximum of 3 login attempts

### Inventory Management
- Create product
- Read / view products
- Update product
- Delete product
- Prevent duplicate product codes

### Inventory Monitoring
- Inventory Overview
- Total units on hand
- Total inventory value
- Low-stock threshold and report

### Traceability
- Search by brand
- Search by product code
- Search by initial or latest batch

### Reporting & Utility
- Sort by price
- Sort by stock
- Calculate stock value per product
- Calculate total inventory value

## Key Enhancements

This version extends the original CRUD implementation with practical workflow controls:

| Enhancement | Purpose |
|---|---|
| **Local JSON persistence** | Keeps inventory changes between application runs |
| **Inventory Overview** | Provides a quick operational summary |
| **Low-stock monitoring** | Highlights items at or below the defined threshold |
| **Stronger validation** | Reduces invalid or incomplete entries |
| **Duplicate-code prevention** | Protects product identifier uniqueness |
| **Product / batch search** | Improves record traceability |
| **Safer update flow** | Blank fields keep existing values |
| **Deletion confirmation** | Reduces accidental removal |

## Inventory KPIs

The application provides four simple operational indicators:

- **Total SKU** — number of inventory records
- **Total Units on Hand** — total current stock
- **Total Inventory Value** — stock quantity × unit price across products
- **Low-stock SKU Count** — products at or below the configured threshold

Default low-stock threshold:

**50 units**

## Process Documentation

- [Business Requirements](docs/business_requirements.md)
- [Process Flow](docs/process_flow.md)
- [Use Case](docs/use_case.md)

## Data Structure

Each inventory record contains:

| Field | Description |
|---|---|
| `kode` | Product identifier |
| `brand` | Product / brand name |
| `stok` | Quantity on hand |
| `harga` | Unit price |
| `batch_awal` | Initial batch reference |
| `batch_terbaru` | Latest batch reference |
| `kategori` | Product category |

The application uses `inventory_data.json` as a simple local persistence layer.

## Main Menu

~~~text
========== MAIN MENU - BrINV ==========
1. Inventory Overview
2. View & Report Inventory
3. Add New Product
4. Update Product
5. Delete Product
6. Exit
========================================
~~~

## How to Run

### Requirement

- Python 3.x
- No external Python packages required

### Run

~~~bash
python Project_CRUD.py
~~~

### Demo Login

~~~text
Username: Unilever
Password: unv11
~~~

The application automatically creates or updates `inventory_data.json` in the project directory.

## Business Analyst Relevance

The project documents a simple operational workflow rather than presenting CRUD functionality alone.

It demonstrates:

**Business Problem → Requirements → Process Flow → System Features → Data Structure → Reporting → Operational Monitoring**

This gives the project a clear BA discussion angle around:

- user needs,
- functional requirements,
- process mapping,
- business rules,
- data requirements,
- validation controls,
- and operational KPIs.

## Scope & Limitations

The current implementation uses:

- local JSON persistence,
- a terminal interface,
- a small demonstration dataset,
- single-user authentication,
- basic inventory calculations.

It does not include:

- relational database storage,
- multi-user role management,
- web interface,
- barcode scanning,
- purchase-order workflow,
- sales-order integration,
- real-time warehouse integration,
- or production-grade security.

These boundaries keep the project aligned with its original Python capstone scope while adding business-process documentation and practical inventory controls.

## Repository Structure

~~~text
CRUD-Inventory-System-Project/
├── Project_CRUD.py
├── inventory_data.json
├── README.md
└── docs/
    ├── business_requirements.md
    ├── process_flow.md
    └── use_case.md
~~~

## Developer

**Brian Naufal**  
Data Analyst / Business Analytics Portfolio

Capstone Project — Python Programming Module 1
