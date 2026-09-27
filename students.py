students = [ {"name": "Thabo",
    "maths": 80,
    "english": 85,
    "science": 75},

    {"name": "Mbali",
    "maths": 60,
    "english": 85,
    "science": 75},

    {"name": "Thando",
    "maths": 80,
    "english": 50,
    "science": 75},

    {"name": "Litha",
    "maths": 80,
    "english": 85,
    "science": 90},


    {"name": "Mike",
    "maths": 50,
    "english": 90,
    "science": 60}
    ]
   

for student in students:
    avg_mark = (student["maths"] + student["english"] + student["science"]) / 3  #with list you cant add them up as args in on parenthesis, gotta be individual
    student["avg_mark"] = round(avg_mark, 2)

    if avg_mark >= 80:
     print("Passed! Level A achieved")
    elif avg_mark >= 70:
        print("Passed! Level B achieved")
    elif avg_mark >= 60:
        print("Passed! Level C achieved")
    elif avg_mark >= 50:
        print("Passed! Level D achieved")
    else:
        print("Needs intervention")

for student in students:
    print(f"Name    : {student['name']}")
    print(f"Maths   : {student['maths']}")
    print(f"English : {student['english']}")
    print(f"Science : {student['science']}")
    print(f"Average : {student['avg_mark']}")
    print("-" * 30)

#class average
total  = 0 

for student in students:
    total += student["avg_mark"]

class_avg = round(total/len(students), 2)

print(f"Class average: {class_avg}")

#highest mark
highest = max(students, key=lambda student: student["avg_mark"])

print("\nHighest Performing Student")
print(f"Name: {highest['name']}")
print(f"Average: {highest['avg_mark']}")

#lowest mark
lowest = min(students, key=lambda student: student["avg_mark"])

print("\nLowest Performing Student")
print(f"Name: {lowest['name']}")
print(f"Average: {lowest['avg_mark']}")

def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student

    return None
    
