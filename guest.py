from db_connection import get_connection
from auth import verify_admin
def add_guest():
    conn = get_connection()
    cursor = conn.cursor()

    # 🔹 Step 1: Show available rooms
    cursor.execute("""
        SELECT room_id, room_type, price 
        FROM rooms 
        WHERE status='available'
    """)
    rooms = cursor.fetchall()

    if not rooms:
        print(" No rooms available!")
        conn.close()
        return

    print("\n===== Available Rooms =====")
    for r in rooms:
        print(f"Room ID: {r[0]} | Type: {r[1]} | Price: ₹{r[2]}")

    # 🔹 Step 2: Take guest details
    print("\n===== Enter Guest Details =====")
    name = input("Enter guest name: ")
    phone = input("Enter phone number: ")
    id_proof = input("Enter ID proof: ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    # 🔹 Step 3: Select room
    try:
        room_id = int(input("Enter Room ID to book: "))
    except ValueError:
        print(" Invalid Room ID!")
        conn.close()
        return

    # 🔹 Step 4: Validate room availability again (important)
    cursor.execute("""
        SELECT room_type, price 
        FROM rooms 
        WHERE room_id=%s AND status='available'
    """, (room_id,))
    
    room = cursor.fetchone()

    if room is None:
        print(" Room not available or invalid!")
        conn.close()
        return

    room_type, price = room

    print(f"\n Room Selected: {room_type}")
    print(f" Price: ₹{price}")

    # 🔹 Step 5: Insert guest with room
    cursor.execute("""
        INSERT INTO guests (name, phone, id_proof, check_in, check_out, room_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, phone, id_proof, check_in, check_out, room_id))

    # 🔹 Step 6: Update room status
    cursor.execute("""
        UPDATE rooms 
        SET status='occupied' 
        WHERE room_id=%s
    """, (room_id,))

    conn.commit()
    conn.close()

    print("\n Booking Successful!")
    print(f" Room ID: {room_id} assigned to {name}")

def view_guests():
    if not verify_admin():
        return
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        g.name,
        g.phone,
        g.check_in,
        g.check_out,
        r.room_id,
        r.room_type,
        r.price
    FROM guests g
    JOIN rooms r 
    ON g.room_id = r.room_id
    """

    cursor.execute(query)
    data = cursor.fetchall()

    print("\n===== Guest Details with Room Info =====")
    print(f"Total Guests: {len(data)}")
    for row in data:
        print(f"""
Guest Name   : {row[0]}
Phone Number : {row[1]}
Check-In     : {row[2]}
Check-Out    : {row[3]}
Room ID      : {row[4]}
Room Type    : {row[5]}
Room Price   : ₹{row[6]}
----------------------------------------
""")

    conn.close()
