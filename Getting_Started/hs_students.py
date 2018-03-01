class HighSchoolStudent(Student):
    
    """
    Adds a High School Student to the list.
    :param name: string - student name
    :param student_id: integer - optional student ID
    """
    
    # Derived/child class. Attributes, like school_name,  can be overridden
    
    school_name = "Springfield High School"
    
    # Methods can also be overridden, as below
    
    def get_school_name(self):
        return "This is a high school student"
    
    # You can also modify parent methods as shown below
    # super() refers to the parent classes method
    
    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + ' -HS'
