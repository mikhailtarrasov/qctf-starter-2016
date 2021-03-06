from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse, Http404
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from .models import Task, Hint
from cabinet.models import Team


@login_required
def index(request):
    tasks = Task.objects.all().prefetch_related('teams')
    team = request.user.team
    for task in tasks:
        task.is_solved_by_current_team = task.is_solved(team)
    return render(request, 'checker/index.html', {'tasks': tasks})


@login_required
@require_POST
def check_flag(request, task_id):
    team = request.user.team
    task = get_object_or_404(Task, pk=task_id)
    flag = request.POST.get('flag', '')
    result = task.submit_flag(team, flag)
    result.update({'flags': team.tasks.count(), 'balance': team.balance})
    return JsonResponse(result)


def scoreboard(request):
    teams = (Team.objects 
        .filter(region__start_time__lte=timezone.now(), is_visible=True)
        .select_related('region')
        .order_by('-balance', 'submit_time', 'pk')
        .prefetch_related('hints'))
    return render(request, 'checker/scoreboard.html', {'teams': teams})


@login_required
def hints(request):
    hints = Hint.objects.select_related('task', 'task__parent').all().prefetch_related('task__parent__teams')
    # tasks = Task.objects.all()
    return render(request, 'checker/hints.html', {'hints': hints})


@login_required
@require_POST
def buy_hint(request, hint_id):
    team = request.user.team
    hint = get_object_or_404(Hint, pk=hint_id)
    task = hint.task
    if hint.is_bought(team):
        return JsonResponse({'error': False, 'balance': team.balance,
                             'hint': hint.get_hint_text(team)})

    if task.is_solved(team):
        return JsonResponse({'error': False, 'balance': team.balance,
                             'hint': 'Вы выполнили задание, к которому относится этот лот'})

    hint.buy(team)
    return JsonResponse({'error': False, 'balance': team.balance,
                         'hint': hint.get_hint_text(team)})


@staff_member_required
@login_required
def admin_scoreboard(request):
    teams = (Team
        .objects
        .select_related('region')
        .order_by('-balance', 'submit_time', 'pk')
        .prefetch_related('tasks'))
    tasks = Task.objects.all().prefetch_related('teams')
    return render(request, 'checker/admin_scoreboard.html', {'teams': teams,
                                                             'tasks': tasks})
