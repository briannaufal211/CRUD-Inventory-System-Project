# Use Case

## Primary Actor

**Warehouse / Inventory Administrator**

## Core Use Cases

| Use Case | Purpose |
|---|---|
| Login | Control access to the application |
| Inventory Overview | Review stock scale, value, and low-stock exposure |
| View Products | Review current inventory records |
| Trace Product / Batch | Locate a product or batch reference |
| Sort Inventory | Review products by price or stock |
| Add Product | Register a new inventory record |
| Update Product | Maintain an existing inventory record |
| Delete Product | Remove a selected inventory record |
| Inventory Value Report | Quantify current stock value |
| Low-stock Report | Identify products at or below the threshold |

## Example: Update Product

**Precondition:** User is authenticated and the product code exists.

1. User selects **Update Product**.
2. User enters a product code.
3. System displays the current record.
4. User enters changes.
5. Blank fields retain existing values.
6. System validates numeric input.
7. System saves the updated record.
8. System displays the updated record.

**Postcondition:** The updated inventory record is persisted.

## Example: Low-stock Monitoring

1. User opens **Inventory Overview** or **Low-stock Report**.
2. System compares each product's stock to the configured threshold.
3. System lists items at or below the threshold.
4. User reviews the list for operational follow-up.

**Business Output:** A focused list of inventory items requiring attention.
