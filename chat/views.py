from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.db.utils import IntegrityError
from .models import User, Message


@csrf_protect
def homepage(request):
    if request.method == "GET":
        return render(request, "chat/homepage.html")
    if request.method == "POST":
        if "login" in request.POST:
            return redirect("login")
        elif "register" in request.POST:
            return redirect("register")
        return Http404


@csrf_protect
def login(request):
    if request.method == "GET":
        return render(request, "chat/login.html", context={"show": False})
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                current_user = User.objects.get(username=username, password=password)
                current_user.is_logged_in = True
                current_user.save()
                return redirect("menu", username=username)
            except User.DoesNotExist:
                return render(request, "chat/login.html", context={"show": True})
        return Http404


@csrf_protect
def register(request):
    if request.method == "GET":
        return render(request, "chat/register.html", context={"show": False})
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                new_user = User.objects.create(username=username, password=password)
                new_user.is_logged_in = True
                new_user.save()
                return redirect("menu", username=username)
            except IntegrityError:
                return render(request, "chat/register.html", context={"show": True})
        return Http404


@csrf_protect
def menu(request, username):
    current_user = User.objects.get(username=username)
    other_users = User.objects.all().exclude(username=username)
    if not current_user.is_logged_in:
        return redirect("login")
    if request.method == "GET":
        return render(request, "chat/menu.html", context={"show": False, "users": other_users})
    if request.method == "POST":
        if "log_out" in request.POST:
            current_user.is_logged_in = False
            current_user.save()
            return redirect("homepage")
        elif "username" in request.POST:
            chosen_username = request.POST["username"]
            try:
                to_user = User.objects.get(username=chosen_username)
                return redirect("chat", username=username, to_user=to_user.username)
            except User.DoesNotExist:
                return render(request, "chat/menu.html", context={"show": True, "users": other_users})
        return Http404


@csrf_protect
def chat(request, username, to_user):
    to_user = User.objects.get(username=to_user)
    current_user = User.objects.get(username=username)
    if not current_user.is_logged_in:
        return redirect("login")
    if request.method == "GET":
        messages = Message.objects.filter(to_user=current_user) | Message.objects.filter(from_user=current_user)
        messages = messages.order_by("time")
        return render(request, "chat/chat.html", context={"user": to_user, "messages": messages})
    if request.method == "POST":
        if "close" in request.POST:
            return redirect("menu")
        elif "send" in request.POST:
            message = request.POST["message"]
            Message.objects.create(to_user=to_user, from_user=current_user, text=message)
            return redirect("chat", username=username, chat_username=to_user)
        return Http404
