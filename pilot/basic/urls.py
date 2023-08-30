from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_form, name='candidate_form'),
    path('test/start/', views.start_test, name='start_test'),
    path('test/finish/', views.test_finish, name='test_finish'),
    path('test/<int:question_number>/', views.question_view, name='question_view'),
    path('instructions/', views.instructions_view, name='instructions'),
    path('test/feedback/', views.feedback_form, name='feedback_form'),
        path('test/complete', views.test_complete, name='test_complete'),

]
