from django.views import generic
from django.shortcuts import render
from .models import Quiz


class Main(generic.ListView):
    template_name = "main/quiz_main.html"
    context_object_name = "quizs"

    def get_queryset(self):
        return Quiz.objects.order_by('number')


def result(request):
    return render(request, "main/result.html", {'result': request.POST})