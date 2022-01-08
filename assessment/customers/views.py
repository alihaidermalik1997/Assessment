from django.shortcuts import render
from django.http import HttpResponse
from assessment.fetch_users import save_user
from django.http import JsonResponse
from assessment.customers.models import Customer


def home_view(request, *args, **kwargs):
    return render(request, "customers/index.html")


def fetch_save_users(request):
    if save_user():
        return JsonResponse({"message": "user added successfully"})
    return JsonResponse({"message": "unable to add user"})


def list_users(request):
    return render(
        request,
        "customers/list_user.html",
        {"customers": Customer.objects.all().order_by("client_id")},
    )
