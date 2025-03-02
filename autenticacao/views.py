from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def exibir_perfil(request):
    usuario = request.user

    # Se o método for POST, tenta salvar o formulário com os novos dados
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            # Redireciona para a mesma página, para que as mudanças sejam refletidas imediatamente
            return redirect('exibir_perfil')  

    # Caso contrário, cria um formulário pré-preenchido com os dados do usuário
    else:
        form = UserProfileForm(instance=usuario)

    return render(request, 'perfil.html', {'usuario': usuario, 'form': form})
