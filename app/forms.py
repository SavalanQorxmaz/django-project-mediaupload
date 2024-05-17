from django import forms
from .models import Logo,Picture,Project,Contacts
import base64



class LogoForm(forms.ModelForm):
    
    class Meta:
        model = Logo
        fields = [
            'title',
            'link',
            'logo'
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        
        if instance:
            
            # print('tempdata:   ',base64.b64encode(self.temporaryData))
            initial = {
                # 'logoImage': base64.b64decode(temporaryData)
            }
        
           
            
        super().__init__(*args, **kwargs )

    def save(self, commit=True):
        if self.cleaned_data.get('logo') is not None:
            
            data = self.cleaned_data['logo'].file.read()
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass