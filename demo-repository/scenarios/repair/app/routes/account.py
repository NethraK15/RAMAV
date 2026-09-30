"""Account lookup endpoint -- pre-existing, unchanged in this PR."""


def get_account_by_id(conn, account_id):
    cursor = conn.cursor()
    cursor.execute("SELECT id, owner FROM accounts WHERE id = ?", (account_id,))
    return cursor.fetchone()
