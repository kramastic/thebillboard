from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApartmentForm, RoomForm, ParkingForm, LandPlotForm, CatActForm, RegisterUserForm, LoginUserForm
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    models_list = [Room, Parking, LandPlot]
    bbs = Apartment.objects.all().values('id', 'item_type', 'specification', 'time_create')
    for i in models_list:
        bbs = bbs.union(getattr(i, 'objects').all().values('id', 'item_type', 'specification', 'time_create'))
    item_types = Type.objects.all()
    actions = Action.objects.all()
    context = {'bbs': bbs, 'item_types': item_types, 'actions': actions}
    return render(request, 'bboard/index.html', context)


class ByTypeView(ListView):
    template_name = 'bboard/by_type.html'
    context_object_name = 'bbs'
    ordering = ['time create']
    allow_empty = False

    def get_queryset(self):
        return getattr(Type.objects.prefetch_related(self.kwargs['item_type']).get(name=self.kwargs['item_type']),
                       f"{self.kwargs['item_type']}").order_by('-time_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_types'] = Type.objects.all()
        context['actions'] = Action.objects.all()
        context['current_item_type'] = Type.objects.get(name=self.kwargs['item_type'])

        return context


def by_action(request, action):
    current_action = Action.objects.get(name=action)
    models_action_list = ['room', 'parking', 'landplot']
    bbs = Apartment.objects.filter(action=action).values('id', 'item_type', 'specification', 'time_create')
    for i in models_action_list:
        bbs = bbs.union(getattr(Action.objects.prefetch_related(f'{i}_set').get(name=action),
                                f'{i}_set').values('id', 'item_type', 'specification', 'time_create'))
    actions = Action.objects.all()
    item_types = Type.objects.all()
    context = {'bbs': bbs, 'item_types': item_types, 'actions': actions, 'current_action': current_action}
    return render(request, 'bboard/by_action.html', context)


def by_cat_act(request, item_type, action):
    bbs = getattr(Action.objects.prefetch_related(f'{item_type}_set').get(name=action),
                  f'{item_type}_set').values('id', 'item_type', 'specification', 'time_create')
    current_action = Action.objects.get(name=action)
    current_item_type = Type.objects.get(name=item_type)
    actions = Action.objects.all()
    item_types = Type.objects.all()
    context = {'bbs': bbs, 'item_types': item_types, 'actions': actions, 'current_item_type': current_item_type,
               'current_action': current_action}
    return render(request, 'bboard/by_cat_act.html', context)


def show_adv(request, item_type, adv_id):
    current_item_type = Type.objects.get(name=item_type)
    actions = Action.objects.all()
    item_types = Type.objects.all()
    adv = getattr(Type.objects.prefetch_related(current_item_type.name).get(name=item_type),
                  f'{current_item_type.name}').get(id=adv_id)
    current_action = Action.objects.get(name=adv.action)
    context = {'adv': adv, 'current_item_type': current_item_type, 'current_action': current_action,
               'item_types': item_types, 'actions': actions}
    return render(request, 'bboard/show_adv.html', context)


class AddBbCreateView(CreateView):
    template_name = 'bboard/create_bb.html'
    form_class = LandPlotForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item_types'] = Type.objects.all()
        context['actions'] = Action.objects.all()
        return context


def cat_act_create_bb(request):
    if request.method == 'POST':
        cat_act = CatActForm(request.POST)
        if cat_act.is_valid():
            action = cat_act.cleaned_data['action']
            item_type = cat_act.cleaned_data['item_type']
            context = {'action': action, 'item_type': item_type}
            return reverse('add_bb_info', kwargs=context)
    else:
        cat_act = CatActForm()
    context = {'form': cat_act}
    return render(request, 'bboard/create_bb_cat_act.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm  # стд форма джанго
    template_name = 'bboard/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Sign up")
    #     return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):  #польз-ль правильно заполнил форму регистрации - автоматическая авторизация
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'bboard/login.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Authentication")
    #     return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


@login_required
def personal_account(request):
    models_list = [Room, Parking, LandPlot]
    bbs = Apartment.objects.all().values('id', 'item_type', 'specification', 'time_create')
    for i in models_list:
        bbs = bbs.union(getattr(i, 'objects').filter(user_id=request.user.id).values('id', 'item_type', 'specification',
                                                                                     'time_create'))
    context = {'bbs': bbs}
    return render(request, 'bboard/personal_account.html', context)
