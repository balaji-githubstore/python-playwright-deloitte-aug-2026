from demo2_employee.employee_module import Employee

Employee.company_name="Deloitte"
Employee.company_name="Deloitte pvt ltd"
print(Employee.company_name)


emp1=Employee(1001,'kevin',50000)
emp2=Employee(1002,'peter',40000)
emp6=Employee()


# emp1.emp_id=101
# emp1.emp_name="John"
# emp1.emp_salary=9000

# emp2.emp_id=102
# emp2.emp_name="Saul"
# emp2.emp_salary=4000

# print(type(emp1))


emp2.display_employee_detail()

# emp1.display_employee_detail()

# # To call the static method
# res=Employee.get_company_name()
# print(res)


# res=Employee.get_company_details()
# print(res)
# print(res[0])


ls=emp2.get_employee_detail_as_list()
print(ls)

dic=emp2.get_employee_detail_as_dic()
print(dic)


emp3=Employee.get_employee_instance()

print(emp3.emp_id)

emp3.display_employee_detail()


emp1.emp_salary=9000
emp2.emp_salary=-9000


print(emp1.emp_salary)
print(emp2.emp_salary)

name=Employee.get_company_name()


emp5=Employee.get_employee_instance()
emp5.display_employee_detail()
emp5.get_employee_detail_as_list()

ls=Employee.get_employee_instance().get_employee_detail_as_list()

