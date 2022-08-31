from django.utils.translation import gettext_lazy as _
from django import forms

from django import forms

# creating a form
class StackSearchForm(forms.Form):

    BOOLEAN_CHOICES = (
        ('', _("")),
        (True, _("True")),
        (False, _("False"))
    )

    SORT_CHOICES = (
        ('relevance', _("Activity")),
        ('activity', _("Votes")),
        ('votes', _("Creation")),
        ('creation', _("Relevance"))
    )

    ORDE_BY_CHOICES = (
        ('desc', _("DESC")),
        ('asc', _("ASC"))
    )


    # specify fields for form
    page = forms.IntegerField(required=False)
    pagesize = forms.IntegerField(required=False)
    from_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}), required=False)
    to_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}), required=False)
    order = forms.ChoiceField(choices=ORDE_BY_CHOICES, required=False)
    min_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}), required=False)
    max_date = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}), required=False)
    sort = forms.ChoiceField(choices=SORT_CHOICES, required=False)
    q = forms.CharField(widget=forms.Textarea, required=False)
    accepted = forms.ChoiceField(choices=BOOLEAN_CHOICES, required=False)
    answers = forms.IntegerField(required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)
    closed = forms.ChoiceField(choices=BOOLEAN_CHOICES, required=False)
    migrated = forms.ChoiceField(choices=BOOLEAN_CHOICES, required=False)
    notice = forms.ChoiceField(choices=BOOLEAN_CHOICES, required=False)
    nottagged = forms.CharField(required=False)
    tagged = forms.CharField(required=False)
    title = forms.CharField(required=False)
    user = forms.IntegerField(required=False)
    url = forms.URLField(required=False)
    views = forms.IntegerField(required=False)
    wiki = forms.ChoiceField(choices=BOOLEAN_CHOICES, required=False)


