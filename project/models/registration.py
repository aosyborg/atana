from dataclasses import dataclass
from enum import Enum

from .course import Course
from .learner import Learner


class RegistrationCompletion(Enum):
    UNKNOWN = 'UNKNOWN'
    COMPLETED = 'COMPLETED'
    INCOMPLETE = 'INCOMPLETE'


class RegistrationSuccess(Enum):
    UNKNOWN = 'UNKNOWN'
    PASSED = 'PASSSED'
    FAILED = 'FAILED'


@dataclass
class Runtime(object):
    completionStatus: str = None
    credit: str = None
    entry: str = None
    exit: str = None
    learnerPreference: dict = None
    location: str = None
    mode: str = None
    progressMeasure: str = None
    scoreScaled: str = None
    scoreRaw: str = None
    scoreMin: str = None
    scoreMax: str = None
    totalTime: str = None
    timeTracked: str = None
    runtimeSuccessStatus: str = None
    suspendData: str = None
    learnerComments: list = None
    lmsComments: list = None
    runtimeInteractions: list = None
    runtimeObjectives: list = None


@dataclass
class ActivityResult(object):
    id: str
    title: str = None
    attempts: int = None
    activityCompletion: str = None
    activitySuccess: str = None
    score: dict = None
    timeTracked: str = None
    completionAmount: dict = None
    suspended: bool = None
    children: list = None
    objectives: list = None
    staticProperties: dict = None
    runtime: Runtime = None

    def __post_init__(self):
        self.runtime = Runtime(**self.runtime) if self.runtime else Runtime()

@dataclass
class Registration(object):
    id: str
    instance: int = None
    xapiRegistrationId: str = None
    dispatchId: str = None
    updated: str = None
    registrationCompletion: RegistrationCompletion = None
    registrationCompletionAmount: str = None
    registrationSuccess: RegistrationSuccess = None
    score: dict = None
    totalSecondsTracked: float = None
    firstAccessDate: str = None
    lastAccessDate: str = None
    completedDate: str = None
    createdDate: str = None
    course: Course = None
    learner: Learner = None
    tags: list[str] = None
    globalObjectives: dict = None
    sharedData: dict = None
    suspendedActivityId: str = None
    activityDetails: ActivityResult = None

    name: str = 'registrations'

    def __post_init__(self):
        self.course = Course(**self.course)
        self.learner = Learner(**self.learner)
        self.activityDetails = ActivityResult(**self.activityDetails)


if __name__ == '__main__':
    import test_data

    '''Only a few tests here to give you an idea'''
    registration_test = test_data.registration
    registration = Registration(**registration_test)
    assert registration.id == registration_test['id']
    assert registration.instance == registration_test['instance']
    print('Registration tests passed!')

    activity_details_test = registration_test['activityDetails']
    activity_details = registration.activityDetails
    assert activity_details.id == activity_details_test['id']
    assert activity_details.title == activity_details_test['title']
    print('ActivityDetails tests passed!')

    runtime_test = activity_details_test['runtime'] 
    runtime = activity_details.runtime
    assert runtime.completionStatus == runtime_test['completionStatus']
    assert runtime.credit == runtime_test['credit']
    print('Runtime tests passed!')