from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput())

    password = forms.CharField(
        widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput()
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput()
    )


class AddQuestionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput()
    )

    question = forms.CharField(
        widget=forms.Textarea()
    )
