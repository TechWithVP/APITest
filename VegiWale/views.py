from django.shortcuts import render, redirect
from VegiApp.models import User
from django.http import HttpResponse

usr = None

def checkUser(username, password):
    userCount = 0
    try:
        global usr
        usr = User.objects.get(userEmail = username, userPassword = password, userDeletionStatus = 0)
        userCount = 1
    except User.DoesNotExist:
        userCount = 0

    return userCount


def delSessions(request):
    if(request.session.has_key('success') and request.session.has_key('msg')):
        del request.session['success']
        del request.session['msg']
        return HttpResponse(status = 302)
    else:
        return HttpResponse(status = 302)

def login(request):
    if(request.method == 'POST'):
        un = request.POST.get('username')
        pa = request.POST.get('password')
        
        permission = checkUser(un, pa)
    
        if(permission == 1):
            global usr
            if(usr.userRole == 'ROLE_USER'):
                pass
            else:
                request.session['UserEmail'] = usr.userEmail
                request.session['UserName'] = usr.userFName + " " + usr.userLName
                request.session['UserId'] = usr.userId
                request.session['UserRole'] = usr.userRole
                return redirect('admin-site/dashboard/')
        else:
            request.session['LoginError'] = True
            request.session.modify = True
            return redirect('/?error=true')
    return render(request, 'Vegi/login.html')

def logout(request):
    request.session.flush()
    request.session.clear()

    for key in request.session.keys():
        del request.session[key]
    return render(request, 'Vegi/login.html')