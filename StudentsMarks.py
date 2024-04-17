class Box:
    def __init__(self, name, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
        self.name = name
        self.rollNo = rollNo
        self.dbmsMarks = dbmsMarks
        self.pythonMarks = pythonMarks
        self.cMarks = cMarks
        self.osMarks = osMarks
        self.cnMarks = cnMarks

students = [
    Box("Harika", "5A1", 78, 67, 77, 89, 46),
    Box("Swapna", "5A2", 38, 65, 97, 59, 41),
    Box("Sushma", "5A3", 88, 95, 47, 89, 31)
]

for student in students:
    print(student.name, student.rollNo, student.dbmsMarks, student.pythonMarks, student.cMarks, student.osMarks, student.cnMarks
