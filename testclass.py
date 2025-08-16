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

# s = Student("John", 20, "john@gmail.com", "male", "1990-01-01")
# print(s)

# s2 = Student("Jane", 21, "jane@gmail.com", "female", "1991-01-01")
# print(s2)

###################### functions tip 

info = {
    "name": "John",
    "age": 20,
    "email": "john@gmail.com",
    "gender": "male",
    "birth_date": "1990-01-01"
}

def printInfo(name, age, email, gender, birth_date):
    print(f"name: {name}, age: {age}, email: {email}, gender: {gender}, birth_date: {birth_date}")

printInfo("ahmed", 20, "ahmed@gmail.com", "male", "1990-01-01")

printInfo(info["name"], info["age"], info["email"], info["gender"], info["birth_date"])

# if you function have a lot of parameters, you can use a dictionary to pass the parameters

printInfo(**info)





