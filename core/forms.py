import datetime
from typing import Any
from django import forms
from django.conf import settings
from django.forms import modelform_factory
from django.forms.fields import FileField, ImageField, DateField,DateTimeField
from django.db.models import Model

ACCEPTABLE_DOCUMENT_TYPES_STR = '.doc, .docx, .pdf, .xlsx, .pptx'
ACCEPTABLE_IMAGE_TYPES_STR = '.png, .jpg, .jiff, .gif, .jpeg, .webp'

LANGS = {}
for item in getattr(settings, 'LANGUAGES'): LANGS[item[0]] = item[1]

class TranslatedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        to_exclude = [] #empty list to store names of fields to be excluded
        lang_codes = LANGS.keys()
        for name, field in self.fields.items(): 

            # Control file types of uploaded files
            if isinstance(field, FileField):
                field.widget.attrs.update({'accept':ACCEPTABLE_DOCUMENT_TYPES_STR})

            # Control Image Types of uploaded contents
            if isinstance(field, ImageField):
                field.widget.attrs.update({'accept':ACCEPTABLE_IMAGE_TYPES_STR})

            # Further customization on Translation fields
            for lang_code in lang_codes:
                # If the field is a translation field
                if name.endswith("_"+lang_code): 
                    # make the english version the default
                    if lang_code=="en":
                        original_name = name[:-3] # get the original field name
                        original = self.fields.get(original_name) # get the original field
                        # If the original field is required, then make the _en version to be required
                        if original and hasattr(original, 'required') and original.required:
                            setattr(field, 'required', True)
                            setattr(field, 'label', str(field.label).replace(" [en]", ""))

                            # Now add the original field into to_exclude list
                            to_exclude.append(original_name)

                    else: #For other types of languages, just update the label name
                        new_label = str(field.label).replace(f" [{lang_code}]", f" {LANGS[lang_code]}")
                        setattr(field,"label", new_label)

        # Exclude original fields
        for name in to_exclude:
            self.fields.pop(name)
    
    def clean_bid_close_date(self):
        end_date = self.cleaned_data.get('bid_close_date')
        open_date = self.cleaned_data.get('bid_open_date')

        if end_date < open_date:
            raise forms.ValidationError("Bid end date should not exceed bid open date.")
        return end_date
    
    # def clean_bid_open_date(self):
    #     open_date = self.cleaned_data.get('bid_open_date')
    #     if open_date < datetime.datetime.now():
    #         raise forms.ValidationError("Bid open date can't be before today.")
    #     return open_date

def get_form(model:Model, fields="__all__", exclude = None):
    widgets = {}
    model_name = model._meta.verbose_name 
    if model_name == 'bid':
        widgets = {'bid_close_date': forms.DateInput(attrs={'type':'date', 'class':"form-control"}),
                   'bid_open_date': forms.DateInput(attrs={'type':'date', 'class':"form-control"})
                }
        
    return modelform_factory(model=model, form=TranslatedForm, fields=fields, exclude=exclude,widgets=widgets, ) 
