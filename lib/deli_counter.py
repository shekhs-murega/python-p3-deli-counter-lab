def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_msg = "The line is currently:"
        formatted_line = ", ".join([f"{i+1}. {person}" for i, person in enumerate(deli_line)])
        print(line_msg, formatted_line.replace(",", ", "), sep=' ')


def take_a_number(deli_line, person_name):
    deli_line.append(person_name)
    position = len(deli_line)
    print(f"Welcome, {person_name}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli_line.pop(0)
        print(f"Currently serving {serving_person}.")
