from db_connection import get_connection

def verify_admin():

    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT * FROM admins
    WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    admin = cursor.fetchone()

    conn.close()

    if admin:
        print("\nAccess Granted!")
        return True

    else:
        print("\nAccess Denied!")
        return False