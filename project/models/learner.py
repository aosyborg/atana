from dataclasses import dataclass
from sqlite3 import Cursor

@dataclass
class Learner(object):
    id: str
    email: str = None
    firstName: str = None
    lastName: str = None

    @staticmethod
    def save(db_cursor: Cursor, learners: list['Learner']):
        data = [
            (learner.id, learner.email, learner.firstName, learner.lastName)
            for learner in learners
        ]

        db_cursor.executemany(
            "INSERT INTO learners VALUES (:id, :email, :firstName, :lastName)",
            data
        )


if __name__ == '__main__':
   import test_data

   learner_test = test_data.learner
   learner = Learner(**learner_test)
   assert learner.id == learner_test['id']
   assert learner.email == learner_test['id']
   assert learner.firstName == learner_test['firstName']
   assert learner.lastName == learner_test['lastName']
   print('Learner tests passed!')