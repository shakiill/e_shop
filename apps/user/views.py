from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.user.forms import StaffCreateForm, TeacherCreateForm, TeacherProfileForm
from apps.user.models import Staff, Teacher


# Create your views here.
class StaffListView(ListView):
    model = Staff
    template_name = 'user/list.html'


class StaffAddView(CreateView):
    model = Staff
    form_class = StaffCreateForm
    template_name = 'add.html'
    success_url = reverse_lazy('staff_list')


class TeacherAddView(CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    template_name = 'add.html'
    success_url = reverse_lazy('staff_list')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'user/teacher.html'


class TeacherProfileView(CreateView):
    model = Teacher
    form_class = TeacherProfileForm
    template_name = 'add.html'
    success_url = reverse_lazy('teacher_list')

    def get_form_kwargs(self):
        kwargs = super(TeacherProfileView, self).get_form_kwargs()
        pk = self.kwargs['pk']
        kwargs.update({'pk': pk})
        return kwargs
