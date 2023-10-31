Custom Test Platform
Project Overview
This Django-based web application serves as a custom test platform for educators. It allows the creation of test questions, collection of candidate details, and recording of responses and feedback, making it a comprehensive tool for educational assessments.

Features
Candidate Registration: Collects candidate information before starting the test.
Test Handling: Dynamically presents questions and records responses.
Feedback Collection: Gathers feedback from candidates post-assessment.
Result Compilation: Automatically aggregates responses for review.
Installation
To set up the project environment:

Clone the repository.
Install Django and other dependencies.
Run migrations to set up the database.

pip install django
python manage.py migrate

Usage
Start the server with python manage.py runserver and navigate to the provided localhost URL. The platform consists of several endpoints:

/candidate_form/: Entry point for candidate registration.
/instructions/: Displays instructions to the candidate before the test begins.
/question/<number>/: Renders individual test questions.
/feedback_form/: Presents a form to collect feedback after the test.
Customization
Educators can customize test questions and feedback forms by modifying the TestQuestion and FeedbackForm models in the code.

Contributing
Contributions to extend the functionality or improve the existing setup are welcome. Please feel free to fork the project and submit a pull request.

License
This project is released into the public domain and can be used by anyone for any purpose without any restrictions.
