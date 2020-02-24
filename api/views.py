from django.shortcuts import render
from django.views import generic
from .models import Team

def index(request):
    num_teams = Team.objects.all().count()
    team1, team2 = list(Team.objects.values_list('name', 'color'))[-2:]
    context = {
        'num_teams':num_teams,
        'team1_name': team1[0],
        'team1_color': team1[1],
        'team2_name': team2[0],
        'team2_color': team2[1]
    }

    return render(request, 'index.html', context=context)

class TeamListView(generic.ListView):
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.all()
    template_name ='teams/teams_list_template.html'