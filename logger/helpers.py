from .models import Log
from django.db.models import Sum


def get_total_hours_logged_today(request, day):
    total_hours_logged_today = Log.objects.filter(user=request.user, day=day).aggregate(
        total=Sum("duration")
    )["total"]
    if total_hours_logged_today == None:
        return 0
    return total_hours_logged_today


def get_total_hours_logged_week(request, start_week_day, end_week_day):
    total_hours_logged_week = Log.objects.filter(
        user=request.user, day__gte=start_week_day, day__lte=end_week_day
    ).aggregate(total=Sum("duration"))["total"]
    if total_hours_logged_week == None:
        return 0
    return total_hours_logged_week


def get_total_hours_logged_month(request, day):
    total_hours_logged_month = Log.objects.filter(
        user=request.user, day__month=day.month
    ).aggregate(total=Sum("duration"))["total"]
    if total_hours_logged_month == None:
        return 0
    return total_hours_logged_month
