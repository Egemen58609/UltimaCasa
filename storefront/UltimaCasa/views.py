from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Gebruiker, Home, Bieding, status,Role
from .forms import Memberform,Memberform1, HuisForm, Homeform, Statusform, Rolform, Memberform2
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from datetime import date

def home(request):
    if request.user.is_authenticated == True:
        current_user = request.user
        functie = current_user.role
        if functie.naam == "koper":
            return redirect("koper")
        if functie.naam == "beheer":
            return redirect("beheer")
        if functie.naam == "admin":
            return redirect("admin")
        current_user = request.user
        username = current_user.username  
        all_members = Gebruiker.objects.all
        return render(request, 'home.html', {'all':all_members, "username":username})
    else:
        return redirect("login")
def account(request):
    current_user = request.user
    user_id = current_user.id
    form = Memberform1(instance=current_user)

    if request.method == "POST":
        form = Memberform1(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            


    return render(request, 'account.html', {"user": current_user, "form":form} ) 


def admin(request):
    statussen = status.objects.all
    if request.user.is_authenticated == True:
        current_user = request.user
        functie = current_user.role
    if functie.naam == "admin":
        
        return render(request, "admin.html", {"statussen":statussen})
    else:
            messages.success(request, "You do not have permission to visit this page!")
            return redirect('home')
def admin_status_voegen(request):
    form = Statusform()
    if request.method == "POST":
        form = Statusform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Status toegevoegd!")
            return redirect("admin")

    return render(request, "admin_statusvoegen.html", {"form":form})
def adminrollen(request):
    rollen = Role.objects.all
    return render(request, "admin_rollen.html", {"rollen":rollen})

def adminaccounts(request):
    Gebruikers = Gebruiker.objects.all
    return render(request, "admin_accounts.html", {"gebruikers":Gebruikers})

def adminstatuswijzigen(request, status_id):
    status1 = status.objects.get(id=status_id)
    form = Statusform(instance=status1)
    if request.method == "POST":
        form = Statusform(request.POST, instance=status1)

        if form.is_valid():
            form.save()
            messages.success(request, "Status succesvol gewijzigd!")
            return redirect("admin")

    
    return render(request, "adminstatus_wijzigen.html", {"status":status1, "form":form})

def adminrolvoegen(request):
    form = Rolform()

    if request.method == "POST":
        form = Rolform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Rol succesvol toegevoegd!")
            return redirect("adminrollen")

    return render(request, "adminrol_voegen.html", {"form":form})

def adminrolwijzigen(request,rol_id ):
    rol = Role.objects.get(id=rol_id)
    form = Rolform(instance=rol)

    if request.method == "POST":
        form = Rolform(request.POST, instance=rol)

        if form.is_valid():
            form.save()
            messages.success(request, "Rol succesvol gewijzigd!")
            return redirect("adminrollen")
        
    return render(request, "adminrol_wijzigen.html", {"rol":rol, "form":form})

def adminrolverwijderen(request, rol_id):
    rol = Role.objects.get(id=rol_id)

    if request.method == "POST":
        rol.delete()
        messages.success(request, "Rol succesvol verwijderd!")
        return redirect("adminrollen")
    return render(request, "adminrol_delete.html", {"rol":rol})

def adminaccountwijzigen(request, gebruiker_id):
    gebruiker = Gebruiker.objects.get(id=gebruiker_id)
    form = Memberform2(instance=gebruiker)
    
    

    if request.method == "POST":
        form = Memberform2(request.POST, instance=gebruiker)
        username = request.POST['username']
        email = request.POST['email']
        print(username,email)
        

        


        if form.is_valid():
            form.save()
            messages.success(request, "Account succesvol gewijzigd!")
            return redirect("adminaccounts")
    return render(request, "adminaccount_wijzigen.html", {"gebruiker":gebruiker, "form":form})

def koper(request):
    if request.user.is_authenticated == True:
        current_user = request.user
        functie = current_user.role
        biedingen = Bieding.objects.all

        if functie.naam == "koper":
            return render(request, "koper.html", {"functie":functie, "biedingen":biedingen})
        else:
            messages.success(request, "You do not have permission to visit this page!")
            return redirect('home')
    else:
        return redirect("home")
    
def koperverwijderhuis(request, huis_id):
    bieding = Bieding.objects.get(id=huis_id)
    if request.user.is_authenticated == True:
        current_user = request.user
        functie = current_user.role

    if request.method == "POST":
        bieding.delete()
        messages.success(request, "Huis succesvol van de markt afgehaald!")
        return redirect("verkoop")
    if functie.naam == "koper":
        return render(request, "koperhuis_verwijderen.html", {"bieding":bieding})
    else:
        return redirect("home")    

def verkoop(request):
    current_user = request.user
    biedingen = Bieding.objects.filter(user=current_user)
    
    

    return render(request, "verkoop.html", {"biedingen":biedingen})

def verkoopform(request):
    
    current_user = request.user
    

    if request.method == "POST":
        form = Homeform(request.POST or None)
        current_user = request.user
        
        
        
       
        if form.is_valid():
           datum = form.cleaned_data['datum']
           straat = form.cleaned_data['straat']
           postcode = form.cleaned_data['postcode']
           plaats = form.cleaned_data['plaats']

           messages.success(request, "Huis succesvol toegevoegd!")
           
           home = Home(datum=datum,user=current_user,straat=straat,postcode=postcode,plaats=plaats)
           home.save()
           bieding = Bieding(datum=datum,user=current_user,house=home)
           bieding.save()
           return redirect("verkoop")
        else:
            messages.success(request, "error")

    else:
        gebruiker = current_user
        form = Homeform(initial={ 'datum': date.today})

    return render(request, "verkoop_form.html", {"date":date.today, "user":current_user, "form":form})

def beheerrelaties(request, relatie_id):
    gebruiker = Gebruiker.objects.get(id=relatie_id)

    if request.method == "POST":
        gebruiker.delete()
        messages.success(request, "Gebruiker succesvol verwijderd!")
        return redirect("relaties")
    return render(request, "relaties_beheer.html", {"gebruiker":gebruiker})

def beheerview(request, bieding_id):
    bieding = Bieding.objects.get(id=bieding_id)
    

    if request.method == "POST":
        bieding.delete()
        messages.success(request,"Huis succesvol van de markt gehaald!")
        return redirect("beheer")

    return render(request, "update_beheer.html", {"bieding":bieding})

def beheeradres(request, adres_id):
    huis = Home.objects.get(id=adres_id)

    if request.method == "POST":
        huis.delete()
        messages.success(request, "Adres succesvol verwijderd!")
        return redirect("adres")

    return render(request, "adres_beheer.html", {"huis":huis})

def koperview(request, bieding_id ):
    bieding = Bieding.objects.get(id=bieding_id)
    form = HuisForm(instance=bieding)

    

    if request.method == "POST":
        form = HuisForm(request.POST, instance=bieding)
        current_bod = bieding.bod
        bod = int(form.data['bod'])
        print(current_bod)
        print(bod)
    
        if form.is_valid() and current_bod is None or bod >= current_bod:
            form.save()
            messages.success(request, "bod geplaatst!")
            return redirect("koper")
        elif current_bod >= bod:
            messages.success(request, "bod moet hoger zijn dan de vorige")

            
            
    return render(request, 'update_koper.html', {'bieding':bieding, "form":form})
    

def beheer(request):
    if request.user.is_authenticated == True:
        biedingen = Bieding.objects.all
        
        current_user = request.user
        functie = current_user.role
        if request.method == "GET":
            print("functie:" + functie.naam)
        if functie.naam == "beheer":
            return render(request, 'beheer.html', {"functie":functie, "user":current_user, "biedingen":biedingen,})
        else:
            messages.success(request, "You do not have permission to visit this page!")
            return redirect('home')
    else:
        return redirect("home")
    
def relatieview(request):

    gebruikers = Gebruiker.objects.all
    return render(request, 'relaties.html' ,{"gebruikers":gebruikers})
def adresview(request):
    huizen = Home.objects.all
    return render(request, "adres.html", {"homes":huizen})
def login_user(request):
    all_members = Gebruiker.objects.all
    if request.method == "POST":


        email = request.POST["email1"]
        password = request.POST["passwd"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

            
        else:
            messages.success(request, ("there was an error logging in"))
            return render(request, 'loginpage.html', {}) 
    
    else:
        return render(request, 'loginpage.html', {'all':all_members})
    
def logout_user(request):
    if request.user.is_authenticated == True:
        logout(request)
        messages.success(request, ("uitgelogd"))
        return redirect('home')
    
    else:
        messages.success(request, ("je bent al uitgelogd"))
        return redirect('home')


def registreer(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        passwd = request.POST['password']
        passwd_len = len(passwd)
    
       
        
        if passwd_len > 8:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                passwd = form.cleaned_data['password']
                

    # Hash the password
                hashed_passwd = make_password(passwd)

    # Create and save the user
                user = Gebruiker(username=username, email=email, password=hashed_passwd)
                user.save()

                
        # messages.success(request, "Your Form has been submitted succsefully")
                login(request, user)
                return redirect('home')
        else:
            messages.success(request, "password too short")
            
            username = request.POST['username']
            email = request.POST['email']
            passwd = request.POST['password']
            

            # messages.success(request, "Your Form could not be submitted, try again")
            return render(request, 'registreer.html', {'username':username, 'email':email, 'password':passwd, })

    else:
        return render(request, 'registreer.html', {})    
        
        

    
   
