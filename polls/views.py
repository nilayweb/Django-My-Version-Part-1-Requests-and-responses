from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    # En yeni sorular önce gelecek şekilde sırala
    latest_questions = Question.objects.all().order_by('-pub_date')
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})