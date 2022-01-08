# Python Assessment
## _The repo doesnot contain any useful code this is just for assessment_

## Prerequisite
- Docker
- Docker Compose

## Runing the project
- clone the repo ``git clone git@github.com:alihaidermalik1997/Assessment.git``
- Use the command ``docker-compose up``
- The site will be running on ``http://0.0.0.0:8000/``
- Click on this line to load and save data from mifos **Click here to fetch and save users from mifos site**.
- Clink on this line to view saved customer list **Click here to see list of saved users**.
- Run this command to execute the unit test ``docker exec assessment_web_1 python manage.py test``

## Explanation

- The [script](https://github.com/alihaidermalik1997/Assessment/blob/master/assessment/fetch_users.py) for fetching and saving mifos customer data.
- The required filter funtion is also inside the same [script](https://github.com/alihaidermalik1997/Assessment/blob/master/assessment/fetch_users.py) **parse_user_data**.
- The unit test for filter function is in this [file](https://github.com/alihaidermalik1997/Assessment/blob/master/assessment/customers/tests.py).
