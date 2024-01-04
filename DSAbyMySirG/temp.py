class Student:
    def __init__(self, names):
        self.names=names

    def __getitem__(self,index):
        return self.names[index]

section_A= Student(["David", "Elsa", "Qasim"])
print(section_A[1])


