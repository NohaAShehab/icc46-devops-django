class Student:
    def __init__(self, name, age, email, gender, birth_date):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
        self.birth_date = birth_date

    # if you need to print the object , you need to define __str__ method
    def __str__(self):
        "this function must return a string"
        # return f"student object(age={self.age})"
        return f"{self.name}"

s = Student("John", 20, "john@gmail.com", "male", "1990-01-01")
print(s)

s2 = Student("Jane", 21, "jane@gmail.com", "female", "1991-01-01")
print(s2)



