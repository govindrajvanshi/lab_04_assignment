class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
        self.load_data()

    def load_data(self):
        data = [
            ("161E90", "Raman", 41, 56000),
            ("161F91", "Himadri", 38, 67500),
            ("161F99", "Jaya", 51, 82100),
            ("171E20", "Tejas", 30, 55000),
            ("171G30", "Ajay", 45, 44000)
        ]
        for emp_id, name, age, salary in data:
            self.employees.append(Employee(emp_id, name, age, salary))

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        return result

    def search_by_salary(self, operator, amount):
        if operator == "<":
            result = [emp for emp in self.employees if emp.salary < amount]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= amount]
        elif operator == ">":
            result = [emp for emp in self.employees if emp.salary > amount]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= amount]
        else:
            result = []
        return result

    def search(self, option, value):
        if option == 1:
            return self.search_by_age(value)
        elif option == 2:
            return self.search_by_name(value)
        elif option == 3:
            operator, amount = value.split()
            return self.search_by_salary(operator, int(amount))
        else:
            return []

def main():
    db = EmployeeDatabase()
    
    print("Search Options:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    option = int(input("Enter search option: "))
    value = input("Enter search value: ")

    results = db.search(option, value)
    
    if results:
        print("Search Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
