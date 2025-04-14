class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(self,student):
        self.student_list.append(student)
StudentDatabase.add_student("Likhon")
StudentDatabase.add_student("Jahidul")

print(StudentDatabase.student_list)