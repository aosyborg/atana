import os
import requests
import sqlite3


SCORM_APP_ID: str = os.getenv('APP_ID')
SCORM_APP_SECRET: str = os.getenv('APP_SECRET')
SCORM_AUTH: tuple[str, str] = (SCORM_APP_ID, SCORM_APP_SECRET)
SCORM_API: str = 'https://cloud.scorm.com/api/v2'

db_connection = sqlite3.connect('local.db')
db_cursor = db_connection.cursor()


def db_setup() -> bool:
    '''
    Assumption: This is a prototype script so we are going to assume we always want to start fresh.
    '''
    db_cursor.execute('DROP TABLE IF EXISTS courses')
    db_cursor.execute('CREATE TABLE courses(id, title, created, updated, version, registrationCount)')

    db_cursor.execute('DROP TABLE IF EXISTS learners')
    db_cursor.execute('CREATE TABLE learners(id, email, firstName, lastName)')

    db_cursor.execute('DROP TABLE IF EXISTS registration_interactions')
    db_cursor.execute('CREATE TABLE registration_interactions(course_id, learner_id, completionStatus, credit, entry, exit, timeTracked, learnerComments, UNIQUE(course_id, learner_id))')


def make_request(endpoint: str, params: dict):
    response = requests.get(SCORM_API + endpoint, params=params, auth=SCORM_AUTH)
    return response.json()


def fetch_objects(endpoint: str, Model: object):
    result = []
    more = None

    while True:
        '''Results are paginated so we loop to ensure we have all objects'''
        response = make_request(endpoint, {'more': more})
        objects = response.get(Model.name, [])
        for obj in objects:
            result.append(Model(**obj))
        
        more = response.get('more')
        if not more:
            break

    return result