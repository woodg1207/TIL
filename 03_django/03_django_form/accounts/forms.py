from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model() #return user
        fields = ('email', 'first_name', 'last_name',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Meta정보를 상속받음. 간결해짐
        # fields = ('username',' password1','password2','email',)
        fields = UserCreationForm.Meta.fields + ('email',)