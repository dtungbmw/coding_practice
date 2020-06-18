import re
from pprint import pprint

SemesterMap = {}
SemesterMap["F"] = "Fall"
SemesterMap["FALL"] = "Fall"
SemesterMap["SPRING"] = "Spring"
SemesterMap["S"] = "Spring"
SemesterMap["SUMMER"] = "Summer"
SemesterMap["SU"] = "Summer"
SemesterMap["W"] = "Winter"
SemesterMap["WINTER"] = "Winter"

# need to check the negative cases

class CourseParser:

    def parse(self, line):
        course = Course()
        numbers = re.findall('[0-9]+', line)
        course.course_num = str(numbers[0])
        course.year = str(self.__nomalize_year(numbers[1]))
        strings = re.findall('[A-Za-z]+', line)
        course.department = strings[0]
        course.semester = self.__nomalize_semester(strings[1])
        return course

    def __nomalize_year(self, year):
        if len(year) < 4:
            year = "20" + year
        return year

    def __nomalize_semester(self, semester):
        return SemesterMap[semester.upper()]


class Course:

    @property
    def semester(self):
        return self.Semester

    @semester.setter
    def semester(self, value):
        self.Semester = value

    @property
    def year(self):
        return self.Year

    @year.setter
    def year(self, value):
        self.Year = value

    @property
    def course_num(self):
        return self.Course_Number

    @course_num.setter
    def course_num(self, value):
        self.Course_Number = value

    @property
    def department(self):
        print("Getting value...")
        return self.Department

    @department.setter
    def department(self, value):
        self.Department = value


# Test
courseParser = CourseParser()
tests = []
tests.append("CS111 2016 Fall")
tests.append("CS-111 Fall 2016")
tests.append("CS 111 F2016")
tests.append("ME:365 Su2020")
for test in tests:
    print(test)
    course = courseParser.parse(test)
    pprint(vars(course))
