from db_connection import get_connection
from auth import verify_admin
from reception_login import receptionist_login

def checkout_guest():

    # Receptionist Login
    if not receptionist_login():
        return

    # Admin Verification
    if not verify_admin():
        return

    guest_id = input("Enter Guest ID to Checkout: ")

    conn = get_connection()
    cursor = conn.cursor()

    # Get guest details
    query = """
    SELECT * FROM guests
    WHERE guest_id = %s
    """

    cursor.execute(query, (guest_id,))
    guest = cursor.fetchone()

    if not guest:
        print("Guest Not Found!")
        conn.close()
        return

    room_id = guest[6]

    # Insert into history table
    history_query = """
    INSERT INTO guest_history
    (guest_id, name, phone, id_proof, room_id,
     check_in, check_out, total_bill, checkout_time)

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())
    """

    # Calculate total bill (you might want to implement proper billing logic)
    # For now, using a placeholder value
    total_bill = 0.00  # TODO: Calculate actual bill based on stay duration and room rate

    cursor.execute(history_query, (
    guest[0],  # guest_id
    guest[1],  # name
    guest[2],  # phone
    guest[3],  # id_proof
    guest[6],  # room_id
    guest[4],  # check_in
    guest[5],  # check_out
    total_bill # total_bill
))



    # Delete guest from current guests table
    delete_query = """
    DELETE FROM guests
    WHERE guest_id=%s
    """

    cursor.execute(delete_query, (guest_id,))

    # Make room available again
    room_query = """
    UPDATE rooms
    SET status='available'
    WHERE room_id=%s
    """

    cursor.execute(room_query, (room_id,))

    conn.commit()
    conn.close()

    print("Guest Checked Out Successfully!")
    print("Room is now Available.")