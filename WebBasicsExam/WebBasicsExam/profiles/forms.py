from django import forms

from WebBasicsExam.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password',)
        labels = {'first_name': "", 'last_name': "", 'email': "", 'password': ""}
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                })
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'image_url',
            'age'
        ]


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = [

        ]

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            return self.instance

