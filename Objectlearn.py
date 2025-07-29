class Company:
    def __init__(self, name ,location):
        self.__name = name
        self.location = location
    def get__Name(self):
        return self.__name
    def employee (self):
        return(
            f"Company Name: {self.__name}, Location: {self.location}"
        )
class Salary(Company):
    def __init__(self,name, location, salary):
        super().__init__(name, location)
        self.salary = salary
The_company = Company("Birla","Jharsuguda")
# # print(The_company.name)
# print(The_company.get__Name())
salary = Salary("bharat","odisha",50000)
# # print(salary.salary)
# print(salary.get__Name())
print(salary.employee())