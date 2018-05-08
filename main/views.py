from django.views import generic
from django.shortcuts import render
from .models import Quiz


def login(request):
    return render(request, "main/login.html")


class Main(generic.ListView):
    template_name = "main/quiz_main.html"
    context_object_name = "quizs"

    def get_queryset(self):
        return Quiz.objects.order_by('number')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['name'] = self.request.GET
        return context


def leader(request):
    return render(request, "main/leader.html")


def result(request):
    return render(request, "main/result.html", {'result': request.POST})