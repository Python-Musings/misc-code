class Something:
    """ global_name available outside the class
      __elvis_king available only inside the class. """
    global_name = "The"
    __elvis_king = "Elvis is The King"

    __slots__ = ('var_in_slots')

    def __init__(self):
        """ Assigned to __dict__
            {'name': 'King'} """
        self.name = "King"

    def print_self_name(self):
        """ print "King" from __dict__ """
        print self.name

    def __the_high(self):
        """ __the_high is a local function only """
        print "The High"

    def print_local_the_high(self):
        """ causes local function to print 'The High' """
        self.__the_high()

    def wont_print_global_name(self):
        """ This will not print global_name under the class name"""
        print global_name

    def can_print_global_name(self):
        """ Prints global_name under the class name """
        print self.global_name
        print Something.global_name

    def elvis_available(self):
        """ can print __elvis_king """
        print self.__elvis_king
        print Something.__elvis_king

    def local_var_in_def(self):
        """ local_var_elvis is not available to self.local_var_elvis """
        local_var_elvis = "Elvis"

    def no_print_elvis(self):
        print self.local_var_elvis

    def wont_print_elvis(self):
        print self.local_var_in_def

class_ref = Something()
print "Name:", class_ref.global_name # The

print "King:", class_ref.name # The

class_ref.print_self_name() # King

class_ref.print_local_the_high() # The High

class_ref.can_print_global_name() # The

class_ref.elvis_available() # Elvis is The King

class_ref.wont_print_elvis() # <bound method Something.local_var_in_def of <__main__.Something instance at 0x023930D0>>

print class_ref.local_var_in_def # <bound method Something.local_var_in_def of <__main__.Something instance at 0x023930D0>>

the_class = class_ref.__class__

print "__class__", the_class

the_doc = class_ref.__doc__

print "__doc__", the_doc

the_dict = class_ref.__dict__

print "__dict__", the_dict

the_init = class_ref.__init__()

print "__init__(self)", the_init

the_module = class_ref.__module__

print "__module__", the_module

the_slots = class_ref.__slots__

print "__slots__", the_slots

# class_ref.wont_print_global_name() # NameError: global name 'global_name' is not defined

# class_ref.no_print_elvis() # AttributeError: Something instance has no attribute 'local_var_elvis'

# print "__elvis_king:", class_ref.__elvis_king() # AttributeError: Something instance has no attribute '__elvis_king'

# class_ref.__the_high() # AttributeError: Something instance has no attribute '__the_high'