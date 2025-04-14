class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(self,*student):
        self.student_list.append(student)
    @classmethod
    def exist(self,id):
        for stdnt in self.student_list:
            if stdnt[0] == id:
                return stdnt[0],id
        return -1,id
    @classmethod
    def enroll_student(self,idx):
        temp = list(self.student_list[idx])
        temp[3] = True
        self.student_list[idx] = tuple(temp)
class Student:
    def __init__(self,student_id,name,department,is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        found = StudentDatabase.exist(self.student_id)
        if (found[0]==-1):
            StudentDatabase.add_student(self.student_id,self.name,self.department,self.is_enrolled)
        else:
            StudentDatabase.enroll_student(1)

Student(1, "Likhon", "CSE", True)
Student(2, "Jahidul", "EEE", False)
print(StudentDatabase.student_list)
# Change enroll
Student(2, "Jahidul", "EEE", True)
print(StudentDatabase.student_list)