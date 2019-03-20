class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):

        return ('{} {}'.format(self.first,self.last))

    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

#   Example of alternative constructor. general convention is to start as from
    @classmethod
    def from_string(cls,empl_str):
        first,last,pay = empl_str.split('-')
        return cls(first, last, pay)

# static methods are method which does not take class or instance as input

    @staticmethod
    def is_workday(day):
        if day.weekday()<5:
            return "Weekday"
        else:
            return "Weekend"

if __name__ == "__main__":

    empl1 = Employee('Partha','Roy',97000)
    empl2 = Employee('Suman','Roy',77000)

    print(empl2.pay)
    empl2.raise_amount = 1.06
    print(Employee.raise_amount)
    print(empl1.raise_amount)
    print(empl2.raise_amount)
    Employee.set_raise_amount(1.02)
    print(empl1.raise_amount)
    print(empl2.raise_amount)

    empl3 = Employee.from_string('Shukla-Roy-8000')
    print(empl3.email)

    import datetime
    my_date = datetime.date(2018,12,14)
    print(empl3.is_workday(my_date))

'''
    print(empl1.email)
    print(empl2.fullname())

    print(Employee.fullname(empl2))

    print(empl1.__dict__)
    print(empl2.__dict__)
    print(Employee.__dict__)
'''










