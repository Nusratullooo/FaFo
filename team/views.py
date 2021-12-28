from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from team.models import Team


def team(request):
    team = Team.objects.all()
    paginator = Paginator(team, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        team = paginator.page(page)
    except PageNotAnInteger:
        team = paginator.page(1)
    except EmptyPage:
        team = paginator.page(paginator.num_pages)
    context = {
        'team': team
    }
    return render(request, 'team.html', context)


def team_detail(request, id):
    team = Team.objects.get(pk=id)

    context = {
        'team': team
    }
    return render(request, 'team_details.html', context)
