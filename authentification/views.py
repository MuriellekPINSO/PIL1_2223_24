from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    errors = []

    if request.method == 'POST':

        matricule = request.POST.get('matricule')
        password = request.POST.get('password')

        if password and matricule:
            user = authenticate(request, username=matricule, password=password)

            if user is not None:
                
                if user.username == "55555555":
                    user_login(request, user)
                    return redirect('admin_index')
                user_login(request, user)
                return redirect('home')
            errors.append("Mot de passe ou numero matricule invalide")
        else:
            errors.append("Veuillez remplir tout les champs")

    context = {
        'errors': errors
    }

    return render(request, 'authentification/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    errors = []


    if request.method == 'POST':

        matricule = request.POST.get('matricule')
        firstname = request.POST.get('prenom')
        lastname = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password and matricule and firstname and lastname:
            if len(matricule) == 8 and matricule.isdigit():
                
                if password == confirm_password:
                    user = User.objects.create_user(
                        username=matricule,
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        password=password,
                    )

                    user = authenticate(request, username=matricule, password=password)
                    if user is not None:
                        user_login(request, user)
                        return redirect('home')
                    else:
                        errors.append("Mot de passe ou numero matricule invalide")

                else:
                    errors.append("Vos deux mots de passe ne sont pas identiques")
            else:
                errors.append("Entrer un matricule valide")
                
    else:
        errors.append("Veuillez remplir tout les champs")

    context = {
        'errors': errors
    }

    return render(request, 'authentification/register.html', context)

def new_password(request):

    errors = []  
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
    
        if matricule and password and password_confirmation:
            user = User.objects.filter(username=matricule).first()

            if user is None:
                errors.append("Matricule non trouvé")

            else:
                if password_confirmation != password:
                    errors.append("Mots de passe non conformes")

                else: 
                    user.set_password(password)
                    user.save()
                    user_login(request, user)
                    if user.username == '55555555':
                        return redirect('admin_index')

                    return redirect('home')  
        else:
            errors.append("Remplissez tous les champs")   
    context = {
        'errors': errors
    }     

    return render(request, 'authentification/forgot-password.html', context)


def logout(request):
    user_logout(request)
    return redirect('login')

