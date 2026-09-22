# Process Flow

## End-to-End Inventory Workflow

~~~mermaid
flowchart TD
    A[User Login] --> B[Main Menu]
    B --> C[Inventory Overview]
    B --> D[View & Report]
    B --> E[Create Product]
    B --> F[Update Product]
    B --> G[Delete Product]

    D --> D1[View Products]
    D --> D2[Trace Product / Batch]
    D --> D3[Sort Inventory]
    D --> D4[Inventory Value]
    D --> D5[Low-stock Report]

    E --> H[Validate Input]
    F --> H
    G --> I[Deletion Confirmation]
    H --> J[Save JSON Data]
    I --> J
    J --> K[Updated Inventory]
~~~

## Business Flow

1. User authenticates.
2. User selects an inventory-management or reporting activity.
3. The system validates relevant inputs.
4. Inventory data is created, updated, deleted, searched, or reported.
5. Changes are persisted to the local JSON data store.
6. User can review inventory value and low-stock exposure.

## Business Analyst Perspective

The process identifies:

- **Actor:** Warehouse / Inventory Administrator
- **Business activities:** Maintain, monitor, report, and trace inventory
- **Controls:** Authentication, validation, duplicate prevention, deletion confirmation
- **Outputs:** Inventory visibility, inventory valuation, and low-stock monitoring
