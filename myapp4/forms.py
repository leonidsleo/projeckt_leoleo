import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    
    def clean_name(self):
        """Плохой пример, подмена параметра min_length"""
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно быть не мее 3 символов')
        return name
    
# пример на проверку использования корпаративной почты
    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
        return email



# больше значений полей узнать в документации


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)    
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    # initial=datetime.date.today - значение по умолчанию сегодняшняя дата
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Famale')])
    # ChoiceField(choices=[('M', 'Male'), ('F', 'Famale')]) - форма выбора из
    # choices - значения M - для базы, сохранение Male - всплываем для выбора пользователя


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 
                                                                        'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))    
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # добавим тип к полю даты
    birthdate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                           'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Famale')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()