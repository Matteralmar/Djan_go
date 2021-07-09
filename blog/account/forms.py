from account.models import Ava
from main import forms


class AvaForm(forms.ModelForm):
    class Meta:
        model = Ava
        fields = ('file_path',)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance