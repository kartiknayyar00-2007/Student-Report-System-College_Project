stu = {}


def add_stu():
    print("--- Add Student ---")
    rn = input("Enter registration number: ")

    if rn in stu:
        print("Student already exists!")
        return

    nm = input("Enter name: ")
    crs = input("Enter course: ")

    while True:
        try:
            cg = float(input("Enter CGPA: "))
            break
        except ValueError:
            print("Please enter a valid CGPA (number).")

    st = input("Enter state: ")

    stu[rn] = {
        "name": nm,
        "course": crs,
        "cgpa": cg,
        "state": st
    }

    print("Student added successfully!")


def search_stu():
    print("--- Search Student ---")
    rn = input("Enter registration number: ")

    if rn in stu:
        inf = stu[rn]
        print("Record Found:")
        print("Reg No : " + rn)
        print("Name   : " + inf["name"])
        print("Course : " + inf["course"])
        print("CGPA   : " + str(inf["cgpa"]))
        print("State  : " + inf["state"])
    else:
        print("Student not found!")


def update_stu():
    print("--- Update Student ---")
    rn = input("Enter Registration number: ")

    if rn not in stu:
        print("Student not found!")
        return

    print("Leave blank to keep old value.")

    nm = input("Name (" + stu[rn]['name'] + "): ") or stu[rn]["name"]
    crs = input("Course (" + stu[rn]['course'] + "): ") or stu[rn]["course"]

    cg_in = input("CGPA (" + str(stu[rn]['cgpa']) + "): ")
    if cg_in:
        cg = float(cg_in)
    else:
        cg = stu[rn]["cgpa"]

    st = input("State (" + stu[rn]['state'] + "): ") or stu[rn]["state"]

    stu[rn] = {
        "name": nm,
        "course": crs,
        "cgpa": cg,
        "state": st
    }

    print("Record updated successfully!")


def delete_stu():
    print("--- Delete Student ---")
    rn = input("Enter registration number: ")

    if rn in stu:
        del stu[rn]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def display_all():
    print("--- All Students ---")

    if not stu:
        print("No records found.")
        return

    for rn, inf in stu.items():
        print("-----------------------")
        print("Reg No : " + rn)
        print("Name   : " + inf["name"])
        print("Course : " + inf["course"])
        print("CGPA   : " + str(inf["cgpa"]))
        print("State  : " + inf["state"])


while True:
    print("====== STUDENT RECORD SYSTEM ======")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    try:
        c = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number from 1 to 6.")
        continue

    if c == 1:
        add_stu()
    elif c == 2:
        search_stu()
    elif c == 3:
        update_stu()
    elif c == 4:
        delete_stu()
    elif c == 5:
        display_all()
    elif c == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
