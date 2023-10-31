# all private features start with __
# all public start without __

import itertools, gc

class Subject:
    set_id = itertools.count()

    def __init__(self, name):
        self.__id = next(Subject.set_id)
        self.__name = name

    def get_id(self):
        return self.__id

    def get_subj_name(self):
        return self.__name

class Student:
    set_id = itertools.count()

    def __init__(self, name, last_name):
        self.__id = next(Student.set_id)
        self.__name = name
        self.__last_name = last_name

    def get_id(self):
        return self.__id

    def get_stud_initials(self):
        return f"{self.__name} {self.__last_name}"

class Diary:
    set_id = itertools.count()

    def __init__(self, student):
        self.__id = next(Diary.set_id)
        self.__stud_id = student.get_id()

    def get_id(self):
        return self.__id

    def __get_stud_id(self):
        return self.__stud_id

    def get_stud_info(self):
        for obj in gc.get_objects():
            if isinstance(obj, Student):
                if obj.get_id() == self.__get_stud_id():
                    return obj.get_stud_initials()

    def get_all_grades(self):
        grades = []
        
        for obj in gc.get_objects():
            if isinstance(obj, Grade):
                if obj.get_diary_id() == self.get_id():
                    grades.append((obj.get_subj_info(), obj.get_grade()))

        return grades

class Grade:
    set_id = itertools.count()

    def __init__(self, subject, diary, grade=None):
        self.__id = next(Grade.set_id)
        self.__subj_id  = subject.get_id()
        self.__diary_id = subject.get_id()
        if grade is not None: 
            self.__grade = grade

    def get_subj_id(self):
        return self.__subj_id

    def get_subj_info(self):
        for obj in gc.get_objects():
            if isinstance(obj, Subject):
                if obj.get_id() == self.get_subj_id():
                    return obj.get_subj_name()

    def get_diary_id(self):
        return self.__diary_id

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

# Here we create student and get info about him using encapsulation
alibek = Student("Alibek", "Baigulov")
print(alibek.get_stud_initials())

diary_alibek = Diary(alibek)
# Here we get info about the owner of a diary using encapsulation
print(diary_alibek.get_stud_info())

geography = Subject("Geography")
chemistry = Subject("Chemistry")
science = Subject("Science")

# Putting grades
g1 = Grade(geography, diary_alibek, 2)
g2 = Grade(geography, diary_alibek, 3)
g3 = Grade(chemistry, diary_alibek, 5)
print(gc.get_objects())

print(diary_alibek.get_all_grades())
