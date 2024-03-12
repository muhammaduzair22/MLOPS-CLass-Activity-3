class mlops:
	def __init__(self,totalStudents):
		self.totalStudents = totalStudents

	def getTotalStudents(self):
		return self.totalStudents

	def addStudent(self):
		self.totalStudents = self.totalStudents + 1	
	
	def removeStudent(self):
		self.totalStudents = self.totalStudents - 1	

	def getClassName(self):
		return "Machine Learning Operations (CS-B)"
	
mlops_class = mlops(5)
print("Number of students in the class : ", mlops_class.getTotalStudents())

# mlops_class.addStudent()
# print("Number of students in the class : ", mlops_class.getTotalStudents())

# mlops_class.removeStudent()
# print("Number of students in the class : ", mlops_class.getTotalStudents())

# print(mlops_class.getClassName())

