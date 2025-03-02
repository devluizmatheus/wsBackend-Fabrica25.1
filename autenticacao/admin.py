from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Exibindo campos na lista de usuários
    list_display = ['username', 'first_name', 'last_name', 'email', 'data_nascimento', 'numero_telefone', 'bio']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['email']

    # Organiza os campos na tela de edição do usuário
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email', 'data_nascimento', 'numero_telefone', 'bio')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Importante', {'fields': ('last_login', 'date_joined')}),
    )

    # Organiza os campos no formulário de criação de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'data_nascimento', 'numero_telefone', 'bio')
        }),
    )


    def save_model(self, request, obj, form, change):
        if not change:  
            obj.set_password(form.cleaned_data['password1'])
        obj.save()
