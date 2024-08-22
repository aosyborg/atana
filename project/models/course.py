from dataclasses import dataclass
from enum import Enum
from sqlite3 import Cursor


class CourseLearningStandard(Enum):
    UNKNOWN = 'UNKNOWN'
    SCORM11 = 'SCORM11'
    SCORM12 = 'SCORM12'
    SCORM20042NDEDITION = 'SCORM20042NDEDITION'
    SCORM20043RDEDITION = 'SCORM20043RDEDITION'
    SCORM20044THEDITION = 'SCORM20044THEDITION'
    AICC = 'AICC'
    XAPI = 'XAPI'
    CMI5 = 'CMI5'
    LTI13 = 'LTI13'


@dataclass
class Course(object):
   id: str
   title: str = None
   xapiActivityId: str = None
   created: str = None
   updated: str = None
   version: int = None
   registrationCount: int = None
   activityId: str = None

   courseLearningStandard: CourseLearningStandard = None
   tags: list = None
   dispatched: bool = None
   rootActivity: dict = None

   name: str = 'courses'


   @staticmethod
   def save(db_cursor: Cursor, courses: list):
      '''Static method to save many courses at once instead of multiple db calls'''
      data = [
         (course.id, course.title, course.created, course.updated, course.version, course.registrationCount)
         for course in courses
      ]
      db_cursor.executemany("INSERT INTO courses VALUES ("
         ":id, :title, :created, :updated, :version, :registrationCount)",
         data
      )


if __name__ == '__main__':
   import test_data

   '''Only a few tests here to give you an idea'''
   course_test = test_data.course
   course = Course(**course_test)
   assert course.id == course_test['id']
   assert course.title == course_test['title']
   print('Course tests passed!')