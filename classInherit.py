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


class Developer(Employee):
    raise_amount = 1.05

    def __init__(self,first,last,pay,prog_lang=None):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

    def desc(self):
        return('Email is {} and lang is  {}'.format(self.email,self.prog_lang))
    #pass
class Manager(Employee):

        def __init__(self,first,last,pay,empls=None):
            super().__init__(first,last,pay)
            if empls != None:
                self.empls = empls
            else:
                self.empls = []

        def show_reportees(self):

            if self.empls == None:
                print('No Reportees')
            else:
                print('Manager is ' + self.first + ' ' + self.last)
                for rpt in self.empls:
                    print(' Employee --->',rpt.first + ' ' + rpt.last)

        def add_reportees(self,rpts=None):

            if rpts == None:
                print('None was added as reportees list is empty')
            else:
                for rpt in rpts:
                    self.empls.append(rpt)
                print('reportees were added sucessfully')

        def remove_reportees(self,rpts=None):

            if rpts == None:
                print('None was added as reportees list is empty')
            else:
                for rpt in rpts:
                    self.empls.remove(rpt)
                print('reportees were removed sucessfully')



if __name__ == "__main__":

    empl1 = Employee('Partha','Roy',97000)
    empl2 = Employee('Suman','Roy',77000)

    dev1 = Developer('Steve','Jobs',50000,'Java')
    dev2 = Developer('Mike','Shinoda',60000,'Python')
    dev3 = Developer('Suman','Sharma',75000,'Cobol')

    print(dev1.email)
    dev1.applyraise()
    print(dev1.pay)
    print(dev1.desc())

    mngr1 = Manager('Partha','Roy',90000,[dev1,dev2])
    print(mngr1.email)
    mngr1.show_reportees()
    mngr1.add_reportees([dev3])
    mngr1.show_reportees()
    mngr1.remove_reportees([dev2])
    mngr1.show_reportees()
    #print(help(dev1))

    #print(dev1.isinstance(Developer))


