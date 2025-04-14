class StudentDatabase:
    student_list = []
class Student(StudentDatabase):
    def __init__(self,student_id,name,department,is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        # if (found[0]==-1):
        self.add_student(self.student_id,self.name,self.department,self.is_enrolled)
        # else:
            # print(found[0],found[1])
            # self.enroll_student(found[0]-1)
    @classmethod
    def add_student(self,*student):
        StudentDatabase.student_list.append(student)
    @classmethod
    def exist(self,id):
        idx = 0
        for stdnt in StudentDatabase.student_list:
            if stdnt[0] == id:
                return idx,id
            else:
                idx+=1
        return -1,id
    @classmethod
    def enroll_student(self,stid):
        exist = Student.exist(stid)
        idx = exist[0]
        if exist[0]==-1:
            print("Student Not Found")
            return
        elif  StudentDatabase.student_list[idx] == True:
            print("Student Already Enrolled")
            return
        temp = list(StudentDatabase.student_list[idx])
        temp[3] = True
        StudentDatabase.student_list[idx] = tuple(temp)
        print("Student Successfully Enrolled")
    @classmethod
    def drop_student(self,stid):
        exist = Student.exist(stid)
        idx = exist[0]
        if exist[0]==-1:
            print("Student Not Found")
            return
        elif  StudentDatabase.student_list[idx] == False:
            print("Student Not Enrolled")
            return
        temp = list(StudentDatabase.student_list[idx])
        temp[3] = False
        StudentDatabase.student_list[idx] = tuple(temp)
        print("Succesfully Droped This Student")
    @classmethod
    def view_student_info(self):
        for tl in StudentDatabase.student_list:
            print(f"ID: {tl[0]} ,STUDENT NAME: {tl[1]} , DEPARTMENT : {tl[2]}, ENROLLED: {tl[3]}")
def menu():
    print(" ")
    print("----- Student Management Menu ----")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
Student('S001', "Md. Likhon Sorkar", "CSE", True)
Student('S002', "Ashraful ahsan", "EEE", False)
Student('S003', "Jahidul Islam", "EEE", True)
while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        Student.view_student_info()
    elif choice == '2':
        stid = input("Enter student id: ")
        Student.enroll_student(stid)
    elif choice == '3':
        stid = input("Enter student id: ")
        Student.drop_student(stid)
    elif choice == '4':
        print("System Exited")
        break