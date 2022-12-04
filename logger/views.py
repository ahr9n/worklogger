import datetime
from .forms import LogForm, ViewForm
from .models import Log
from .helpers import get_total_hours_logged_today, get_total_hours_logged_week, get_total_hours_logged_month
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        return render(
            request,
            "logger/login.html",
            {"message": "Invalid username and/or password."},
        )
    else:
        return render(request, "logger/login.html")


def logout_view(request):
    logout(request)
    return redirect("login_view")


@login_required(login_url="/login")
def index(request):
    log_form, view_form = LogForm(), ViewForm()
    if "add" in request.POST:
        log_form = LogForm(request.POST)
    if "view" in request.POST:
        view_form = ViewForm(request.POST)

    message = "Failed"
    if request.method == "POST" and "add" in request.POST and log_form.is_valid():
        duration = log_form.cleaned_data["duration"]
        day = log_form.cleaned_data["day"]
        project = log_form.cleaned_data.get("project")
        user = request.user
        description = log_form.cleaned_data["description"]
        log = Log.objects.create(
            duration=duration,
            day=day,
            description=description,
            user=user,
            project=project,
        )
        message = "Success"
        log_form = LogForm()  # clear data after save form

    day = datetime.date.today()
    if request.method == "POST" and "view" in request.POST and view_form.is_valid():
        day = view_form.cleaned_data["day"]

    logs = Log.objects.filter(
        user=request.user,
    ).filter(day=day)

    # where Monday is 0 and Sunday is 6
    weekday_now = datetime.date.weekday(day)
    start_week_day = day - datetime.timedelta(days=weekday_now)
    end_week_day = start_week_day + datetime.timedelta(days=6)

    total_hours_logged_today = get_total_hours_logged_today(request, day)
    total_hours_logged_week = get_total_hours_logged_week(
        request, start_week_day, end_week_day
    )
    total_hours_logged_month = get_total_hours_logged_month(request, day)

    return render(
        request,
        "logger/index.html",
        {
            "message": message,
            "user": request.user,
            "log_form": log_form,
            "view_form": view_form,
            "total_hours_logged_today": total_hours_logged_today,
            "total_hours_logged_month": total_hours_logged_month,
            "total_hours_logged_week": total_hours_logged_week,
            "logs": logs,
        },
    )


def error_404(request, exception):
    return render(request, "logger/404.html")
