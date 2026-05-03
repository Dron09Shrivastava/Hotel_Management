from db_connection import get_connection

def add_feedback():
    name=input("Enter your Name: ")
    email=input("Enter your mail id: ")
    feedback=input("Enter your feedback: ")

    conn=get_connection()
    cursor=conn.cursor()

    query=""" INSERT INTO feedback (name,email,feedback) VALUES(%s,%s,%s)"""

    cursor.execute(query, (name, email, feedback))

    conn.commit()
    conn.close()

    print("Feedback Added Successfully!")

def view_feedbacks():
    conn = get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT name, email, feedback FROM feedback")
    feedback= cursor.fetchall()

    print("\n---Feedbacks---")
    for name, email,feed in feedback:
        print(f"Name     : {name}")
        print(f"Email    : {email}")
        print(f"Feedback : {feed}")
        print("-!"*30)
    conn.close()
