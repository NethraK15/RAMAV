"""Invoice lookup endpoint -- NEW in this PR.

VULNERABLE: same class of SQL injection as the sql_injection scenario,
used here to demonstrate the Repair Agent + revalidation loop.
"""


def get_invoice_by_customer(conn, customer_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, total FROM invoices WHERE customer = '{customer_name}'")
    return cursor.fetchone()
