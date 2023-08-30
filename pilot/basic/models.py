from django.db import models

# Create your models here.
from django.db import models

class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]

    EDUCATION_LEVELS = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('D', 'Doctorate'),
    ]

    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    country = models.CharField(max_length=100)
    education_level = models.CharField(max_length=2, choices=EDUCATION_LEVELS)
    occupation = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    consent = models.BooleanField(default=False)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TestQuestion(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='test_images/', null=True, blank=True)  # If you want to add images

class UserResponse(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    response = models.TextField()

# models.py

from django.db import models

class TestTimer(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)

from django.db import models

class TestFeedback(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    was_the_platform_smooth = models.BooleanField()
    were_the_instructions_clear = models.BooleanField()
    did_you_have_issues_with_saving = models.BooleanField()
    test_difficulty = models.CharField(max_length=50)
    were_questions_clear = models.BooleanField()
    poorly_worded_questions = models.TextField()
    did_you_have_enough_time = models.BooleanField()
    did_you_have_unexpected_issues = models.TextField()
    was_the_interface_intuitive = models.BooleanField()
    improvement_suggestions = models.TextField()
    was_the_test_format_appropriate = models.BooleanField()
    preferred_question_types = models.TextField()
    did_you_feel_anxious = models.BooleanField()
    reason_for_anxiety = models.TextField()
    was_the_sequence_logical = models.BooleanField()
    give_score_for_overall_experience = models.IntegerField()
