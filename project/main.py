import lib
from models import Course, Learner, Registration, RegistrationInteraction


def main():
    courses = lib.fetch_objects('/courses', Course)
    Course.save(lib.db_cursor, courses)

    registrations = lib.fetch_objects('/registrations', Registration)
    learners = [reg.learner for reg in registrations]
    Learner.save(lib.db_cursor, learners)

    registration_interactions = [RegistrationInteraction(reg) for reg in registrations]
    RegistrationInteraction.save(lib.db_cursor, registration_interactions)


def verify():
    lib.db_cursor.execute('''
        SELECT * FROM courses
        JOIN registration_interactions ON courses.id = registration_interactions.course_id
        JOIN learners ON registration_interactions.learner_id = learners.id
    ''')
    print(lib.db_cursor.fetchall())


if __name__ == '__main__':
    lib.db_setup()
    main()
    verify()
    print('done.')