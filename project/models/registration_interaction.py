from sqlite3 import Cursor
from .registration import Registration

class RegistrationInteraction(object):
    def __init__(self, registration: Registration):
        self.course_id = registration.course.id
        self.learner_id = registration.learner.id
        self.completionStatus = registration.activityDetails.runtime.completionStatus
        self.credit = registration.activityDetails.runtime.credit
        self.entry = registration.activityDetails.runtime.entry
        self.exit = registration.activityDetails.runtime.exit
        self.timeTracked = registration.activityDetails.runtime.timeTracked
        self.learnerComments = registration.activityDetails.runtime.learnerComments

    @staticmethod
    def save(db_cursor: Cursor, interactions: list):
        '''Static method to save many courses at once instead of multiple db calls'''
        data = [
            (interaction.course_id, interaction.learner_id, interaction.completionStatus, interaction.credit,
             interaction.entry, interaction.exit, interaction.timeTracked, interaction.learnerComments)
             for interaction in interactions
        ]
        db_cursor.executemany('INSERT OR IGNORE INTO registration_interactions VALUES('
            ':course_id, :learner_id, :completionStatus, :credit, :entry, :exit, :timeTracked, :learnerComments)',
            tuple(data)
        )


if __name__ == '__main__':
   import test_data

   registration_test = test_data.registration
   registration = Registration(**registration_test)
   interaction = RegistrationInteraction(registration)
   assert interaction.course_id == registration_test['course']['id']
   assert interaction.learner_id == registration_test['learner']['id']
   assert interaction.completionStatus == registration_test['activityDetails']['runtime']['completionStatus']
   assert interaction.credit == registration_test['activityDetails']['runtime']['credit']
   assert interaction.entry == registration_test['activityDetails']['runtime']['entry']
   assert interaction.exit == registration_test['activityDetails']['runtime']['exit']
   assert interaction.timeTracked == registration_test['activityDetails']['runtime']['timeTracked']
   assert interaction.learnerComments == registration_test['activityDetails']['runtime']['learnerComments']
   print('Interaction tests passed!')