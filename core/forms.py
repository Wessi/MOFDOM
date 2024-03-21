from django import forms
from django.conf import settings
from about_us.models import About
from django.forms import modelform_factory

LANGS = {}
for item in getattr(settings, 'LANGUAGES'): LANGS[item[0]] = item[1]

class TranslatedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        to_exclude = [] #empty list to store names of fields to be excluded
        lang_codes = LANGS.keys()
        for name, field in self.fields.items():
            for lang_code in lang_codes:
                
                if name.endswith("_"+lang_code): # If the field is a translation field
                    
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
        

def get_form(model, fields="__all__", exclude = None):
    return modelform_factory(model=model, form=TranslatedForm, fields=fields, exclude=exclude) 
