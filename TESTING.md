# Inventory System Test Cases

## Requirements

### R1 — Add Equipment

The system shall allow a user to add equipment to the inventory.

### R2 — View Inventory

The system shall allow a user to view all equipment currently in inventory.

### R3 — Search Equipment

The system shall allow a user to determine whether an equipment type exists
in the inventory.

### R4 — Remove Equipment

The system shall allow a user to remove equipment from the inventory.

### R5 — Duplicate Equipment

The system shall allow multiple pieces of the same equipment type to exist
in the inventory.

### R6 — Unique Equipment IDs

Each individual equipment item shall eventually have a unique identifier.

# Inventory System Test Cases

## Add

1. Add normal item
Expected: item appears in inventory

2. Add empty item
Expected: error message

3. Add whitespace-only item
Expected: error message

4. Add duplicate item
Expected: Duplicate item added with unique Equipment ID.

## Search

5. Search existing item
Expected: "Item is in stock."

6. Search nonexistent item
Expected: "Item is not in stock."

## Remove

7. Remove existing item
Expected: item removed

8. Remove nonexistent item
Expected: error message

## Menu

9. Enter 1
Expected: Add

10. Enter invalid menu option
Expected: error message and return to menu