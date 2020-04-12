# Implicit Inheritance
class Parent:
    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


print()
# Override Explicitly
class Parent2:
    def override(self):
        print("PARENT override()")


class Child2(Parent2):
    def override(self):
        print("CHILD override")


dad = Parent2()
son = Child2()

dad.override()
son.override()


print()
# Alter Before or After
class Parent3:
    def altered(self):
        print("PARENT altered()")


class Child3(Parent3):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child3, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent3()
son = Child3()

dad.altered()
son.altered()
