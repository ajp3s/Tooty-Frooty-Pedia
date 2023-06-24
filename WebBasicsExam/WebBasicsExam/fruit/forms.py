from django import forms

from WebBasicsExam.fruit.models import Fruit


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {'name': "", 'description': "", 'image_url': "", 'nutrition': ""}

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',

                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                })
        }


class FruitDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

