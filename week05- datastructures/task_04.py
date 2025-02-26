#4. Write a program that stores a student name and a list of her courses and
#grades in a dict, the program should then print out her data.
#The number of course she has could change
import pprint

struct = {
    "Student Name": "Mary",
    "Courses": {
        "Math": 90,
        "Science": 85,
        "English": 80
    }
}

pprint.pprint(struct)