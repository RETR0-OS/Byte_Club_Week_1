from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Competition
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreateCompetitionForm, EditCompetitionForm
from django.urls import reverse_lazy, reverse
from django_staff_required.views import StaffRequiredMixin
import datetime
# Create your views here.
class ListCompetitions(generic.ListView):
    model = Competition
    ordering = ["-Registration_Start_Date"]
    template_name = 'competitions/competition_list.html'

#def get_is_register_started(date):


def ListCompetitionsView(request):
    competitions = Competition.objects.all().order_by("Registration_End_Date")
    competition_list =[]
    for competition in competitions:
        if competition.Registration_Start_Date <= datetime.date.today() and competition.Registration_End_Date >= datetime.date.today():
            competition_list.append(competition)
    data = {
        "competition_list": competition_list
    }
    return render(request, 'competitions/competition_list.html', data)

def CompetitionDetails(request, slug):
    if request.method == "GET":
        competition = Competition.objects.get(slug=slug)
        if competition.Registered_Users.filter(id=request.user.id).exists():
            registered = True
        else:
            registered = False
        data = {
            "competition": competition,
            "registered": registered,
        }
        return render(request, "competitions/competition_details.html", data)

@login_required
def RegisterUserForCompetition(request, slug):
    competition = get_object_or_404(Competition, slug=slug)
    if competition.Registered_Users.filter(id=request.user.id).exists():
        competition.Registered_Users.remove(request.user)
        return redirect("competitions:compete")
    else:
        competition.Registered_Users.add(request.user)
        return redirect("competitions:compete")

class AddCompetitionView(StaffRequiredMixin, generic.CreateView):
    model = Competition
    form_class = CreateCompetitionForm
    template_name = 'competitions/add_competition.html'
    success_url = reverse_lazy('competitions:compete')

class EditCompetitionDetails(StaffRequiredMixin, generic.UpdateView):
    model = Competition
    form_class = EditCompetitionForm
    template_name = 'competitions/edit_competition.html'
    success_url = reverse_lazy("competitions:compete")
