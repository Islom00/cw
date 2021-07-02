from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import NameForm
from django.views.generic import TemplateView
from .models import Users



def users(request):
    model = Users.objects.all()
    context = {
        "data": model
    }
    return render(request, "Users/users.html", context)


def form (request):
    return render(request, "Users/form.html")


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("user")
    else:
        form = NameForm()

        return render(request, "Users/users.html", {
            "form": form
        })


class User(TemplateView):
    template_name = "Users/users.html"



