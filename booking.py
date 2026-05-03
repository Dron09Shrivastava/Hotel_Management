from db_connection import get_connection

def book_room():
    name = input("Enter guest name: ")
    phone = input("Enter phone: ")
    room_type = input("Enter room type (Single/Double/Deluxe): ")

    conn = get_connection()
    cursor = conn.cursor()

    # Step 1: Check available room
    query = """
    SELECT room_id, price FROM rooms 
    WHERE room_type=%s AND status='available' 
    LIMIT 1
    """
    cursor.execute(query, (room_type,))
    room = cursor.fetchone()

    if room is None:
        print(" No available rooms of this type!")
        conn.close()
        return

    room_id, price = room

    print(f"✅ Room Available! Price: ₹{price}")

    # Step 2: Insert guest with room
    insert_query = """
    INSERT INTO guests (name, phone, room_id)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (name, phone, room_id))

    # Step 3: Update room status
    update_query = """
    UPDATE rooms SET status='occupied' WHERE room_id=%s
    """
    cursor.execute(update_query, (room_id,))

    conn.commit()
    conn.close()

    print(f" Booking Successful! Room ID: {room_id}")