from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse


def home(request):
    return HttpResponse('''<h1>Welcome to Home Page</h1>
                            <br/>
                            <a href="about/"> About</a><br/>
                            <a href="contact/"> Contact</a><br/>
                            <a href="address/"> Address</a>
                             ''')


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def about(request):
    return HttpResponse('''<a href="/polls/">back</a><br/><h1>About Page!</h1>''')


def contact(request):
    return HttpResponse('''<a href="/polls/">back</a><br/><h1>Contact Page!</h1>''')


def address(request):
    return HttpResponse('''<a href="/polls/">back</a><br/><h1>Address Page!</h1>''')


def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
