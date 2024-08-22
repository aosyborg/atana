# ATANA Take Home Quiz

## Objective: 
Extract learner interaction/response data from registrations correlated with the course from cloud.scorm.com. Organize the data into a basic data model that could then be used to analyze overall interaction results and trends. 

## Assumptions & Notes
* "Organize the data into a basic data model" is very vague. I made an assumption about what specific data was needed and is detailed in the project > models > registration_interaction.py file
* This is a take home quiz so I chose sqlite as my database. Obviously in a production environment I would choose differently.
* As I don't know how this data will be used, my "verify" function just prints the data to the screen.
* Data is stored as a many-to-many relationship in the database. Many learners have many courses, and the interactions join them.
* For brevity, models have some tests to show I am thinking about testing. In a production environment I would use a full testing suite with much more comprehensive tests.
* In the middle of my work, the /registrations endpoint stopped returning runtime data. I did my best with my test data but wasn't able to verify end-to-end.
* There were some trade-offs and assumptions with the data. I generally made an assumption that data will be there and it is mostly formatted as expected. I'm sure if I started getting some unexpected values for expected keys, errors would arise. If that is a concern, I would want to validate the response a bit more than I did.
* I attempt to load all data first, then save to a local database. This could cause issues with extremely large datasets and would need to be mitigated if the data could not be stored in memory.
* Each run drops the existing tables and recreates everything. Of course this is only for ease of testing and verifying everything works as expected.

Hopefully this is enough to pique your interest. I'd love to talk it through and answer any questions!