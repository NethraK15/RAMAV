"""User lookup endpoint -- NEW in this PR.

VULNERABLE: user-controlled `username` is interpolated directly into
the SQL string via an f-string instead of a parameterized query.
"""


def get_user_by_username(conn, username):
    """@app.get("/users/<username>") -- looks up a user by username."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, username, email FROM users WHERE username = '{username}'")
    return cursor.fetchone()
