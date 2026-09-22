# Business Requirements

## Business Problem

The simulated FMCG warehouse process needs a simple way to maintain product information, monitor stock, trace batches, and review inventory value.

BrINV models a lightweight digital workflow to centralize these activities in one interactive application.

## Business Objective

Improve visibility of basic warehouse information and simplify routine inventory-management activities within the simulated process.

## Primary User

**Warehouse / Inventory Administrator**

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | User can authenticate before accessing the application |
| FR-02 | User can view inventory records |
| FR-03 | User can add one or multiple products |
| FR-04 | User can update product information |
| FR-05 | User can delete product records |
| FR-06 | User can search by brand, product code, or batch |
| FR-07 | User can sort inventory by price or stock |
| FR-08 | User can review total inventory value |
| FR-09 | User can review low-stock items |
| FR-10 | System prevents duplicate product codes |
| FR-11 | System validates numeric input |
| FR-12 | Inventory changes persist between runs |

## Data Requirements

Each inventory record contains:

- Product code
- Brand
- Stock quantity
- Unit price
- Initial batch
- Latest batch
- Category

## Operational KPIs

- Total SKU
- Total Units on Hand
- Total Inventory Value
- Low-stock SKU Count

## Business Rules

1. Product codes must be unique.
2. Stock and unit price cannot be negative.
3. Category must come from the supported category list.
4. Product deletion requires confirmation.
5. Inventory changes are saved to the local JSON file.
6. Low-stock status is triggered when stock is less than or equal to the configured threshold.

## Scope Boundary

This is a portfolio simulation and is not intended to represent a production warehouse-management system.
