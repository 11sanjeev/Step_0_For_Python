employee = {
    'name':"Holy" ,
    'age':42,
    'Salary':430000,
    'Desiganation':"Manager"
}
for i in employee:
    print(i)
for i in employee.values():
    print(i)
for key in employee:
    print(key +': '+str(employee[key]))