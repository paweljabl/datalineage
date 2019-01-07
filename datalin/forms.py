from django import forms
from collections import OrderedDict

from .models import Node, Entity, Technology, Application

class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = ('__all__')

class EntityForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = ('__all__')

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('owner_name', 'contact_email', 'is_bi')



class NodeForm(forms.ModelForm):

    # IS_APPLICATION_CHOICES = (
    #     ('N', 'Technology'),
    #     ('Y', 'Application'),
    # )

    class Meta:
        model = Node
        fields = ('name', 'display_name', 'description', 'entity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['entity'].queryset = Entity.objects.none()
        self.fields['technology'] = forms.ModelChoiceField(queryset=Technology.objects.all(), empty_label=None)
        # self.fields['is_application'] = forms.ChoiceField(choices=IS_APPLICATION_CHOICES, default='Y')
        self.fields['display_name'].required = False
        self.fields['description'].required = False

        new_fields = OrderedDict()
        # new_fields['is_application'] = self.fields['is_application']
        new_fields['technology'] = self.fields['technology']
        new_fields['entity'] = self.fields['entity']
        new_fields['name'] = self.fields['name']
        new_fields['display_name'] = self.fields['display_name']
        new_fields['description'] = self.fields['description']
        self.fields = new_fields

        if 'technology' in self.data:
            try:
                technology_id = int(self.data.get('technology'))
                self.fields['entity'].queryset = Entity.objects.filter(technology_id=technology_id).order_by('name')
                self.fields['entity'].empty_value = 'Next choose entity'
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty entity queryset
        elif self.instance.pk:
            self.fields['entity'].queryset = self.instance.technology.entity_set.order_by('name')

    # from django import forms
# from .models import Person, entity, technology
#
#
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('name', 'birthdate', 'technology', 'entity')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['entity'].queryset = entity.objects.none()
#         self.fields['technology'].queryset = technology.objects.none()