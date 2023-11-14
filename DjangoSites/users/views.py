from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from users.forms import AuthUserForm, RegistrationForm, CreateUserForm, HelpMeForm, IcanHelpForm
from users.models import HelpMe, IcanHelp, Science


class LoginUser(LoginView):
    form_class = AuthUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class RegistrationUser(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_profile')


class CreateProfile(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def profile_view(request):
    obj_h = None
    scn = Science.objects.all()
    if 'helpme' in request.POST and request.method == "POST":
        for i in Science.objects.filter(scn=request.POST.get('item')):
            obj_h = i
            break
        help_me_db = HelpMe(
            user_id=request.user.id,
            item=obj_h,
            add_information=request.POST.get('add_information')
        )
        help_me_db.save()
    if 'can_help' in request.POST and request.method == "POST":
        for i in Science.objects.filter(scn=request.POST.get('items')):
            obj_h = i
            break
        can_help_db = IcanHelp(
            user_id=request.user.id,
            items=obj_h,
            skills=request.POST.get('skills')
        )
        can_help_db.save()

    cont = {
        'science': scn,
        'obj1': HelpMe.objects.all(),
        'obj2': IcanHelp.objects.all()
    }
    return render(request, 'profile/profile.html', cont)



