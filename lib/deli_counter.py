katz_deli = []

def line(persons):
    if persons:
        for i, person in enumerate(persons, start=1):
            print(f"{person} is currently at place {i} in line.")
    else:
        print("The line is currently empty.")


def now_serving(persons):
    if persons:
        serving_person = persons[0]
        del persons[0]
        print(f"Now serving: {serving_person}")
    else:
        print("There is nobody waiting to be served!")


persons = ["Alice", "Bob", "Charlie", "David"]
now_serving(persons)