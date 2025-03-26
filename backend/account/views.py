from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
# Create your views here.
from .models import User
from .forms import UserCreateForm

def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'account/user_list.html', context)

def user_create(requset):
    pass


def user_edit(request):
    pass

class UserCreate(CreateView):
    "Создание пользователя"

    form_class = UserCreateForm
    success_url = reverse_lazy('account:user_list')
    template_name = 'account/user_create.html'


class UserEdit(UpdateView):
    "Редактирование пользователя"

    pass
