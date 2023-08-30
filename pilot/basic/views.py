from django.shortcuts import render, redirect
from .forms import CandidateForm, FeedbackForm
from .models import TestQuestion, UserResponse, Candidate

def candidate_form(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructions')
    else:
        form = CandidateForm()
    return render(request, 'basic/candidate_form.html', {'form': form})

def question_view(request, question_number):
    try:
        question = TestQuestion.objects.get(pk=question_number)
    except TestQuestion.DoesNotExist:
        return redirect('test_finish')
    
    saved_response = request.session.get(f'response_{question_number}', '')

    if request.method == "POST":
        response_data = request.POST.get('response')
        request.session[f'response_{question_number}'] = response_data
        UserResponse.objects.update_or_create(
            user=Candidate.objects.last(),
            question=question,
            defaults={'response': response_data}
        )
        next_question = question_number + 1
        if 'submit_test' in request.POST:
            return redirect('test_finish')
        elif next_question <= TestQuestion.objects.count():
            return redirect('question_view', question_number=next_question)

    context = {
        'question': question,
        'saved_response': saved_response,
        'question_numbers': range(1, TestQuestion.objects.count() + 1),
        'question_number': question_number,
    }

    return render(request, 'basic/question_template.html', context)

def test_finish(request):
    # Existing logic here
    return redirect('feedback_form')


def start_test(request):
    return redirect('question_view', question_number=1)

def instructions_view(request):
    if request.method == "POST":
        return redirect('start_test')
    return render(request, 'basic/instructions.html')

def feedback_form(request):
    candidate = Candidate.objects.last()
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.candidate = candidate
            feedback.save()
            return redirect('test_complete')  # Create a 'test_complete' view for finalizing the test
    
    else:
        form = FeedbackForm()
    
    return render(request, 'basic/feedback_form.html', {'form': form})

def test_complete(request):
    # Existing logic here
    return render(request, 'basic/test_finish.html')
