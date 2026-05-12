from db_connection import get_connection

def receptionist_login():
    username = input("Enter Receptionist Username: ")
    password = input("Enter Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT * FROM receptionist
    WHERE username=%s AND password=%s
    """

    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        print("Login Successful!")
        return True
    else:
        print("Invalid Receptionist Credentials!")
        return False