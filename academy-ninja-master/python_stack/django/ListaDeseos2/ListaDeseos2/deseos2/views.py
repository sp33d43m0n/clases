from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
import bcrypt
from deseos2.models import User1, Book1
from datetime import datetime, time, timezone
from time import gmtime, strftime



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    
    if 'u_id' not in request.session:
        request.session['u_id'] = 0

    return render(request, 'index.html')

def reg_validate(request):
    check = User1.objects.filter(email = request.POST['email'])
    
    error = False

    if len(request.POST['first_name'])< 2:
        messages.error(request,'First Name must be longer than 1 character', extra_tags = 'fn_error' )
        error = True

    if not NAME_REGEX.match(request.POST['first_name']):
        messages.error(request,'Name Field must ONLY contain Alpha characters', extra_tags = 'fn_error')
        error = True

    if not NAME_REGEX.match(request.POST['last_name']):
        messages.error(request,'Name Field must ONLY contain Alpha characters', extra_tags = 'ln_error')
        error = True

    if len(request.POST['last_name'])< 2:
        messages.error(request,'Last Name must be longer than 1 character', extra_tags = 'ln_error')
        error = True

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Email is in an invalid format', extra_tags = 'email_error')
        error = True

    if check:
        messages.error(request,'Email has already been registered', extra_tags = 'email_error')
        error = True

    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request,'Passwords do not match', extra_tags = 'pw_error')
        error = True

    if len(request.POST['password']) < 8 :
        messages.error(request,'Password must be 8 or more characters long', extra_tags = 'pw_error')

    if error == True:
        return redirect('/')

    elif error == False:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User1.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], release_date = request.POST['release_date'], password = pw_hash)
        print(new_user)
        request.session['user_id'] = new_user.id
        # save User._id in session
        messages.success(request, 'You have registered succesfully. You may now login', extra_tags = 'registered')
        
        return redirect('/')

def login_validate(request):
        email = request.POST["email"]
        password = request.POST["password"]
        print(f"{email} {password}")
        echeck = User1.objects.filter(email=email) 
        print (echeck)
        
        if echeck:
            print('existe')
            #if echeck[0].password == password:
            if bcrypt.checkpw(request.POST['password'].encode(), echeck[0].password.encode()):
                print(echeck[0].password)
                request.session['login'] = True
                request.session['u_id'] = echeck[0].id
                return redirect('/home')
            else:
                print('passwor bad')
                messages.error(request,'Password invalido', extra_tags = 'badpas')
                return redirect('/')

        else: 
            messages.error(request,'Email No registrado', extra_tags = 'malem')
            return redirect('/')
            
        
        
    
def home(request):
        
    if request.session['login'] == True:
        user = User1.objects.filter(id = request.session['u_id'])
        user_info = {
            'user':user[0]
        }
        
        return render(request, 'AllBook.html', user_info)

    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

############################################################

# Create your views here.
# *********************************************
# 1. # GET /bookss/new ------ 'Book' was 'bookss'
def AddNewBook(request): # GET /bookss/new 
    context = {
        'bookss': Book1.objects.all()
    }
    return render(request, 'AddNewBook.html', context)
# *********************************************
#2. # POST /bookss/create
def CreateNewBook(request): # POST /bookss/create
    Book2 = Book1.objects.create(title=request.POST['title'], network=request.POST['network'])
    return redirect(f'/bookss/{Book2.id}')
# *********************************************
# 3. GET bookss/id
def TvBook(request, id): # GET /bookss/<id>
    context = {
        'Book': Book1.objects.get(id=id)
             
    }
    return render(request, 'TVBook.html', context)
# *********************************************
# 4 GET /bookss ------ 'Book' was 'bookss'
def AllBook(request): # GET /bookss
    context = {
        'bookss': Book1.objects.all()
    }
    return render(request, 'AllBook.html', context)
# *********************************************
# 5 GET /bookss/<id>
def EditBook(request, id):
    context = {
        'Book': Book1.objects.get(id=id)
    }
    return render(request, 'EditBook.html', context)
# *********************************************
# 6 POST bookss/<id>/update
def UpdateBook(request, id):
    Book = Book1.objects.get(id=id)
    Book.title = request.POST['title']
    Book.network = request.POST['network']
    #Book.release_date = request.POST['release_date']
    #Book.description = request.POST['description']
    Book.save()
    return redirect(f'/bookss/{id}')
# *********************************************
# 7 POST bookss/<id>/destroy
def DeleteBook(request, id):
    Book = Book1.objects.get(id=id)
    Book.delete()
    return redirect('/bookss')
# *********************************************
# 8 POST /bookss Root Rout redirects to /books