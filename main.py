from guest import add_guest, view_guests
from feedback import add_feedback,view_feedbacks
from room import add_room, view_rooms, update_room_status, delete_room
while True:
    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Guest Management.")
    print("2. Room Management.")
    print("3. Employee Management.")
    print("4. Services")
    print("5. Feedback")
    print("6. Exit")
    choice = input("Enter your choice:")
    #Guest management
    if choice=='1':
        while True:
            print("\n---Guest Management---")
            print("1. Add Guest")
            print("2. View Guest")
            print("3. Back")
            
            g_choice=input("Enter your choice:")


            if g_choice == '1':
                add_guest()
            elif g_choice == '2':
                view_guests()
            elif g_choice == '3':
                break
            else:
                print("Invalid choice")

                
        

    #Room Management
    elif choice == '2':
        while True:
            print("\n--- ROOM MANAGEMENT ---")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Update Room Status")
            print("4. Delete Room")
            print("5. Back")

            ch = input("Enter your choice: ")

            if ch == '1':
                add_room()
            elif ch == '2':
                view_rooms()
            elif ch == '3':
                update_room_status()
            elif ch == '4':
                delete_room()
            elif ch == '5':
                break
            else:
                print("Invalid choice!")
                
    #Employee Management
    elif choice=='3':
        while True:
            print("\n---Employee Management---")
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Back")
            
            e_choice=input("Enter your choice:")
            if e_choice=='3':
                break
            else:
                print("Feature coming soon")
                
    #Service Management
    elif choice=='4':
        while True:
            print("\n---Services---")
            print("1. View Services")
            print("2. Back")
            
            s_choice=input("Enter your choice:")
            if s_choice=='2':
                break
            else:
                print("Feature coming soon")

    elif choice=='5':
        while True:
            print("\n---Feedback---")
            print("1. Add Feedback.")
            print("2. View Feedback")
            print("3. Back")

            f_choice=input("Enter your choice: ")
            if f_choice == '1':
                add_feedback()
            elif f_choice == '2':
                view_feedbacks()
            elif f_choice == '3':
                break
            else:
                print("INVALID CHOICE")
            
        
    elif choice=='6':
        print("Thank You for using the system!")
        break

    else:
        print("Invalid Choice")
