from db_connection import get_connection
from tabulate import tabulate


# ➤ Add Room
def add_room():
    room_type = input("Enter room type (Single/Double/Deluxe): ")
    price = int(input("Enter room price: "))

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO rooms (room_type, price)
    VALUES (%s, %s)
    """

    cursor.execute(query, (room_type, price))
    conn.commit()
    conn.close()

    print("Room added successfully!")


# ➤ View Rooms
def view_rooms():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT r.room_id, r.room_type, r.price, r.status, g.name, g.phone
    FROM rooms r
    LEFT JOIN guests g ON r.room_id = g.room_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    print("\nRoom Details with Guest Info:")
    for row in data:
        print(f"""
Room ID: {row[0]}
Type: {row[1]}
Price: ₹{row[2]}
Status: {row[3]}
Guest: {row[4] if row[4] else "None"}
Phone: {row[5] if row[5] else "None"}
-------------------------
""")

    conn.close()


# ➤ Update Room Status
def update_room_status():
    room_id = int(input("Enter room ID: "))
    status = input("Enter new status (Available/Booked): ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE rooms
    SET status = %s
    WHERE room_id = %s
    """

    cursor.execute(query, (status, room_id))
    conn.commit()
    conn.close()

    print("Room status updated successfully!")


# ➤ Delete Room
def delete_room():
    room_id = int(input("Enter room ID to delete: "))

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM rooms WHERE room_id = %s"
    cursor.execute(query, (room_id,))

    conn.commit()
    conn.close()

    print("Room deleted successfully!")