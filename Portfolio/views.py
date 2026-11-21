from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login , logout, get_user_model
from django.contrib.auth.decorators import login_required


User=get_user_model()


# Create your views here.


def home(request):
    portfolio = Portfolio.objects.filter(user=request.user) if request.user.is_authenticated else Portfolio.objects.none()
    
    return render(request, 'home.html',{
        'portfolio' : portfolio
    })
    
    
def about(request):
    return render(request, 'about.html')


def registration(request):
    if request.method =='POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
        # password=form.cleaned_data.get('password1')
        # user=form.save(commit=False)
        form.save()
        return redirect('login')
    else:
        form=RegistrationForm()
        
    return render(request, 'registration.html',{
        'form': form
    })
    

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = LoginForm()

    return render(request, 'loginform.html', {
        'form': form
    })

    
def logout_view(request):
        logout(request)
        return redirect('login')
   
    
@login_required
def dashboard(request):
    portfolio = Portfolio.objects.filter(
        user=request.user
    ).first()

    additional_infos = []

    if portfolio:
        additional_infos = portfolio.additional_infos.all()

    return render(request, 'dashboard.html', {
        'portfolio': portfolio,
        'additional_infos': additional_infos
    })
    
    
@login_required
def AddInfo(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)

        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()

            field_names = request.POST.getlist('field_name')
            field_values = request.POST.getlist('value')

            for name, value in zip(field_names, field_values):
                if name.strip() and value.strip():
                    AdditionalInfo.objects.create(
                        portfolio=portfolio,
                        field_name=name,
                        value=value
                    )

            return redirect('dashboard')

    else:
        form = PortfolioForm()

    return render(request, 'addinfo.html', {
        'form': form
    })
    
    
@login_required
def UpdateInfo(request, id):

    portfolio = Portfolio.objects.get(
        id=id,
        user=request.user
    )

    additional_infos = portfolio.additional_infos.all()

    if request.method == 'POST':

        # Add new field input
        if 'add_field' in request.POST:

            new_fields = int(request.POST.get('new_fields', 0)) + 1

            form = PortfolioForm(instance=portfolio)

            return render(request, 'updateinfo.html', {
                'form': form,
                'portfolio': portfolio,
                'additional_infos': additional_infos,
                'new_fields': range(new_fields)
            })

        # Update portfolio information
        form = PortfolioForm(
            request.POST,
            instance=portfolio
        )

        if form.is_valid():

            form.save()

            # Delete selected information
            delete_ids = request.POST.getlist('delete_info')

            portfolio.additional_infos.filter(
                id__in=delete_ids
            ).delete()

            # Update existing information
            info_ids = request.POST.getlist('info_id')
            field_names = request.POST.getlist('field_name')
            values = request.POST.getlist('value')

            for info_id, name, value in zip(
                info_ids, field_names, values
            ):

                info = portfolio.additional_infos.filter(
                    id=info_id
                ).first()

                if info:
                    info.field_name = name
                    info.value = value
                    info.save()

            # Add new information
            new_names = request.POST.getlist('new_field_name')
            new_values = request.POST.getlist('new_value')

            for name, value in zip(new_names, new_values):

                if name.strip() and value.strip():

                    AdditionalInfo.objects.create(
                        portfolio=portfolio,
                        field_name=name.strip(),
                        value=value.strip()
                    )

            return redirect('dashboard')

    else:

        form = PortfolioForm(instance=portfolio)

    return render(request, 'updateinfo.html', {
        'form': form,
        'portfolio': portfolio,
        'additional_infos': additional_infos,
        'new_fields': range(0)
    })   
    
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })

@login_required
def AddAdditionalInfo(request, id):

    portfolio = Portfolio.objects.get(
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        form = AdditionalInfoForm(request.POST)

        if form.is_valid():
            info = form.save(commit=False)
            info.portfolio = portfolio
            info.save()

            return redirect('updateinfo', id=portfolio.id)

    else:
        form = AdditionalInfoForm()

    return render(request, 'addadditionalinfo.html', {
        'form': form,
        'portfolio': portfolio
    })

@login_required
def resume(request):
    portfolio = Portfolio.objects.filter(user=request.user).first()

    return render(request, 'resume.html', {
        'portfolio': portfolio
    })
    
    
@login_required
def EditAdditionalInfo(request, id, info_id):

    portfolio = Portfolio.objects.get(
        id=id,
        user=request.user
    )

    info = AdditionalInfo.objects.get(
        id=info_id,
        portfolio=portfolio
    )

    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST, instance=info)

        if form.is_valid():
            form.save()
            return redirect('updateinfo', id=portfolio.id)

    else:
        form = AdditionalInfoForm(instance=info)

    return render(request, 'editadditionalinfo.html', {
        'form': form,
        'portfolio': portfolio
    })


@login_required
def DeleteAdditionalInfo(request, id, info_id):

    portfolio = Portfolio.objects.get(
        id=id,
        user=request.user
    )

    info = AdditionalInfo.objects.get(
        id=info_id,
        portfolio=portfolio
    )

    if request.method == 'POST':
        info.delete()

    return redirect('updateinfo', id=portfolio.id) 
    
