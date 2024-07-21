
SAMSUNG_PDK = """
CREATE TABLE gat_pdk
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    hash TEXT NOT NULL UNIQUE,
    product_type TEXT NOT NULL,
    foundry TEXT NOT NULL,
    process TEXT NOT NULL,
    architecture TEXT NOT NULL,
    update_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

TSMC_PDK = """
"""