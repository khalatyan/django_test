from django import forms

from second.models import Lead, LeadState


class LeadForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=255)
    state = forms.ModelChoiceField(
        queryset=LeadState.Tag.objects.all(), widget=forms.CheckboxInput
    )

    class Meta:
        model = Lead

    def state_clean(self):
        print(self.data)
        print(self.cleaned_data)
        print(self.instance)
