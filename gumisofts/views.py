from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

release_date = datetime(2025, 4, 1)


def home(request, *args, **kwargs):
    remaining = release_date - datetime.now()
    seconds = remaining.seconds
    days = seconds // (24 * 60 * 60)
    days = remaining.days

    seconds = seconds % (24 * 60 * 60)

    hours = seconds // (60 * 60)
    seconds = seconds % (60 * 60)
    mins = seconds // 60
    seconds = seconds % 60

    secs = seconds

    return render(
        request,
        template_name="gumisofts.com/home.html",
        context={"days": days, "hours": hours, "mins": mins, "secs": secs},
    )
