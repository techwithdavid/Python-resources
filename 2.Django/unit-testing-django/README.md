# unit-testing-django
This is a sample Django application that demonstrates different ways to run unit tests for a Django project. 

## Run all unit tests.
In order to run all unit tests, the following command can be used: 

`./manage.py test`

This will run all unit tests in any files that match the `test*.py` pattern. In this specific project, there are only two matching test files located in the `./main/hello_app/tests` directory. Each matching file only has one unit test. Therefore, the test runner should run two unit tests. 

## Run only the unit tests in a sub-folder.
In order to only run the unit tests located in the `./main/hello_app/tests/sub-tests` directory, the following command can be used:

`./manage.py test hello_app.tests.sub-tests`

This will only run unit tests that are found within the `sub-tests` directory. Please note that the test files must still match the `test*.py` pattern. There is only one test file located in the `sub-tests` directory, and that file only contains one unit test. Therefore, the test runner should only run one unit test. 

Please note, it is also possible to simply pass a folder name to the `manage.py` test command, rather than configuring a folder as a package. For example:

`./manage.py test hello_app/tests/sub-tests/`

## More information.
Django unit testing documentation: [Writing and running tests](https://docs.djangoproject.com/en/3.2/topics/testing/overview/)