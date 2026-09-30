"""Product lookup endpoint -- pre-existing, unchanged in this PR."""


def get_product_by_sku(conn, sku):
    """@app.get("/products/<sku>") -- safe, parameterized query."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products WHERE sku = ?", (sku,))
    return cursor.fetchone()
