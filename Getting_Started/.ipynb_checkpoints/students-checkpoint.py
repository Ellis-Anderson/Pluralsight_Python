class Student:
    
    """
    Adds a Student to the list.
    :param name: string - student name
    :param student_id: integer - optional student ID
    """
    
    # Parent class
    
    school_name = "Springfield Elementary"
    
    def __init__(self, name, student_id = 1, last_name="none"):
        self.name = name
        self.student_id = student_id
        self.last_name = last_name
        #students.append(self)
        
    def __str__(self):
        return "Student " + self.name
    
    def get_name_capitalized(self):
        return self.name.capitalize()
        
    def get_school_name(self):
        return self.school_name
