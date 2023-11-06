from django.shortcuts import render

from ligue1data.requests import getLigue1Teams


def index(request):
    team_ids = [84, 85, 91, 93, 79, 106, 111, 83, 81, 116, 94, 95, 82, 96, 97, 112, 99, 80]
    teams_data = []
    for team_id in team_ids:
        team_data = getLigue1Teams(team_id)
        teams_data.append(team_data)
    return render(request, "index.html", context={"teams_data": teams_data})
