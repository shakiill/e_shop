from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.StaffListView.as_view(), name='staff_list'),
    path('staff/add/', views.StaffAddView.as_view(), name='staff_add'),

    path('teacher/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher/add/', views.TeacherAddView.as_view(), name='teacher_add'),
    path('teacher/<int:pk>/profile/add/', views.TeacherProfileView.as_view(), name='teacher_profile_add'),
]
