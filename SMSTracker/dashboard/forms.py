# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import AuthenticationForm, SignupForm
from django.contrib.auth.models import Group
from userena.models import UserenaSignup
from userena import settings as userena_settings


class AuthenticationFormCustom(AuthenticationForm):
    attrs_dict = {'class': 'input-block-level', 'name' : 'logUsername', 'autocomplete' : 'off', 'placeholder' : 'Login'}
    identification = forms.CharField(label='Login',
                           widget=forms.TextInput(attrs=attrs_dict),
                           max_length=75,)
     
    password = forms.CharField(label=_(u"Password"),
                               widget=forms.PasswordInput(attrs={'class': 'input-block-level', 'placeholder' : u'Password', 'autocomplete' : 'off', 'name' : 'logPass', }, render_value=False))


USERNAME_RE = r'^[\.\w]+$'
class SignupFormCustom(SignupForm):

    attrs_dict = {'class': 'input-block-level', 'name' : 'logUsername', 'autocomplete' : 'off',}

    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"),
                                error_messages={'invalid': _('Username must contain only letters, numbers, dots and underscores.')})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Email"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Create password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Repeat password"))

    
class FilterDashboardForm(forms.Form): 
    """
        Filter Form Table SMS
    """
    startDate = forms.DateField(widget=forms.TextInput(attrs={'data-fx': 'datepicker', 'data-date-format' : 'mm/dd/yy', 'class' : 'span3', 'placeholder' : 'Start Date', }))
    endsDate = forms.DateField(widget=forms.TextInput(attrs={'data-fx': 'datepicker', 'data-date-format' : 'mm/dd/yy', 'class' : 'span3', 'placeholder' : 'Ends Date',}))
    text_contains = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-xxlarge', 'class' : 'span3', 'placeholder' : 'Text Contains', }))
    fromphone_contains = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-xxlarge', 'placeholder' : 'From Phone Contains', 'class' : 'span3',}))


class MoreIdSpyForm(forms.Form):
    to_phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-large',}))
    pin = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-large', }))
