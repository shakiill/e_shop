from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div, Fieldset, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory

from apps.teacher.models import TeacherProfile
from apps.user.models import Staff, Teacher


class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('username', 'name', 'email', 'phone_number', 'dob', 'gender')

    def __init__(self, *args, **kwargs):
        super(StaffCreateForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('dob', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                ),
            )
        )


class TeacherCreateForm(UserCreationForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Teacher
        fields = ('username', 'name', 'email', 'phone_number', 'dob', 'gender', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(TeacherCreateForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                Column('dob', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                ),
            )
        )


class TeacherProfileForm(forms.ModelForm):
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TeacherProfile
        fields = ('teacher', 'joining_date', 'about')

    def __init__(self, pk, *args, **kwargs):
        super(TeacherProfileForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].disabled = True
        self.initial['teacher'] = Teacher.objects.get(pk=pk)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('teacher', css_class='form-group col-md-6 mb-0'),
                Column('joining_date', css_class='form-group col-md-6 mb-0'),
                Column('about', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                ),
            )
        )
