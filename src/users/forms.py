from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

   class Meta:

      model = get_user_model()
      fields = ('email', 'username', 'is_superuser', 'is_staff', 'is_group',)


class CustomUserChangeForm(UserChangeForm):

   class Meta:

      model = get_user_model()
      fields = ('email', 'username', 'is_superuser', 'is_staff', 'is_group',) 