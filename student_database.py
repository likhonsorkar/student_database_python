class StudentDatabase:
    student_list = []
class Student(StudentDatabase):
    def __init__(self,student_id,name,department,is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        found = self.exist(self.student_id)
        if (found[0]==-1):
            self.add_student(self.student_id,self.name,self.department,self.is_enrolled)
        else:
            print(found[0],found[1])
            self.enroll_student(found[0]-1)
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
    def enroll_student(self,idx):
        temp = list(StudentDatabase.student_list[idx])
        temp[3] = True
        StudentDatabase.student_list[idx] = tuple(temp)
    @classmethod
    def drop_student(self,id):
        found = self.exist(id)
        StudentDatabase.student_list.pop(found[0])
    @classmethod
    def view_student_info(self):
        for tl in StudentDatabase.student_list:
            print(f"ID: {tl[0]} ,STUDENT NAME: {tl[1]} , DEPARTMENT : {tl[2]}, ENROLLED: {tl[3]}")

Student('S001', "Md. Likhon Sorkar", "CSE", True)
Student('S002', "Ashraful ahsan", "EEE", False)
Student('S003', "Jahidul Islam", "EEE", True)