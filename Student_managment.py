
class Student:
    def __init__(self, __student_id, __name, __department, __is_enrolled):
        self.student_id = __student_id
        self.name = __name
        self.department = __department
        self.is_enrolled= __is_enrolled

    def view_student_info(self):
        print(f'ID: {self.student_id}, Name: {self.name}, Department: {self.department}, Enrolled: {self.is_enrolled} ')

    def enroll_student(self):
        if self.is_enrolled == False:
            self.is_enrolled = True
            print(f"Student {self.student_id} Enrollment Completed")
        else:
            print(f"Student {self.student_id} Already Enrolled!")

    def drop_student(self):
        if self.is_enrolled == True:
            self.is_enrolled = False
            print(f"Student {self.student_id} Dropped Successfully")
        else:
            print(f"Student {self.student_id} Already Dropped")


class StudentDatabase:
    student_list = []

    @classmethod    
    def add_student(cls, student):
        cls.student_list.append(student)

student1 = Student("S01","fury","cst", True)
student2 = Student("S02","night","eee", False)
student3 = Student("S03","dark","civil", True)

StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)
StudentDatabase.add_student(student3)


while(True):
    print("\n----------\n")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    option =int(input("Enter Your option: "))

    if option == 1: 
        print("\n----------\n")
        for i in StudentDatabase.student_list:
            i.view_student_info()
            

    elif option == 2:   
        student_id = input("Enter Student ID: ")
        print("\n----------\n")
        flag = False
        for i in StudentDatabase.student_list:
            if student_id == i.student_id:
                Student.enroll_student(i)
                flag = True
        if flag == False:
            print("No Student Found")
        


    elif option == 3:  
        student_id = input("Enter Student ID: ")
        print("\n----------\n") 
        flag = False
        for i in StudentDatabase.student_list:
            if student_id == i.student_id:
                Student.drop_student(i)
                flag = True
        if flag == False:
            print("No Student Found")
            

    elif option == 4:
        print("\n----------\n") 
        print("Thank You Very Much")
        print("\n----------\n") 
        break
    
    else:
        print("\n----------\n") 
        print("Enter valid option !")

