class Employee:
    # static variable or class variable
    company_name = None
    company_location = None

    # constructor
    def __init__(self, id, name, salary):
        # non-static variable or instance variable
        self.emp_id = id
        self.emp_name = name
        self.__emp_salary = salary

    # non-static method
    def display_employee_detail(self):
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.__emp_salary)
        print("Company Name:", Employee.company_name)
        print("--------------------------------------------")

    # static method - how to create and call it?
    @staticmethod
    def get_company_name():
        return Employee.company_name

    # @staticmethod
    # def get_company_details():
    #     return [Employee.company_name,Employee.company_location]

    def get_employee_detail_as_list(self):
        return [self.emp_id, self.emp_name, self.__emp_salary, Employee.company_name]

    def get_employee_detail_as_dic(self):
        return {
            "id": self.emp_id,
            "name": self.emp_name
        }

    @staticmethod
    def get_employee_instance():
        emp=Employee(0,None,None)
        return emp

    # get property - set 
    @property
    def emp_salary(self):
        return self.__emp_salary

    # set property - write 
    @emp_salary.setter
    def emp_salary(self, value):
        if value>0:
            self.__emp_salary = value
        else:
            self.__emp_salary=0
            # raise ValueError("Salary cannot be negative.!!!")