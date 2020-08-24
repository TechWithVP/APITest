from django.shortcuts import render, redirect
from VegiApp.models import User, VFCategory, VegiFruits
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
import json
from django.core import serializers
import secrets

UserSecret = ""

# File Upload Function
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def getAllUsers(ur, ue):
    allUsers = None
    userCount = 0
    if(ur == "ROLE_ADMIN"):
        try:
            allUsers = User.objects.filter(userRole = 'ROLE_USER').filter(userDeletionStatus = 0)
            userCount = allUsers.count()
        except User.DoesNotExist:
            userCount = 0
    elif(ur == "ROLE_SUPER_ADMIN"):
        try:
            allUsers = User.objects.exclude(userEmail = ue).filter(userDeletionStatus = 0)
            userCount = allUsers.count()
        except User.DoesNotExist:
            userCount = 0
    params = {'allUsers': allUsers, 'allUserCount': userCount}
    return params

def getUserForDelAdmin():
    allUsers = User.objects.filter(userDeletionStatus = 1)
    userCount = allUsers.count()
    params = {'allUsers': allUsers, 'allUserCount': userCount}
    return params

def getSelectedUser(username):
    userCount = 0
    try:
        usr = User.objects.get(userEmail = username, userDeletionStatus = 0)
        userCount = 1
    except User.DoesNotExist:
        userCount = 0

    return userCount

def checkUserForPassChange(username, password):
    userCount = 0
    try:
        usr = User.objects.get(userEmail = username, userPassword = password)
        userCount = 1
    except User.DoesNotExist:
        userCount = 0

    return userCount

def getUserEmailFromId(uId):
    usr = User.objects.get(userId = uId, userDeletionStatus = 0)
    return usr.userEmail

# Categories Function
def getAllCategories(ur):
    allCategories = None
    catCount = 0
    if(ur == "ROLE_ADMIN" or ur == "ROLE_SUPER_ADMIN"):
        try:
            allCategories = VFCategory.objects.all()
            catCount = allCategories.count()
        except User.DoesNotExist:
            catCount = 0

    params = {'allCategories': allCategories, 'allCategoryCount': catCount}
    return params

# Vegis Function
def getAllVegiFruits(ur):
    allVegis = None
    vegiCount = 0
    if(ur == "ROLE_ADMIN" or ur == "ROLE_SUPER_ADMIN"):
        try:
            allVegis = VegiFruits.objects.all()

            for i,v in enumerate(allVegis):
                singleCat = VFCategory.objects.get(catId = v.catId)

                if(v.vegifruitStatus == 0):
                    allVegis[i].vegifruitStatus = "In Active"
                elif(v.vegifruitStatus == 1):
                    allVegis[i].vegifruitStatus = "Active"

                allVegis[i].catId = singleCat.catName

            vegiCount = allVegis.count()
        except User.DoesNotExist:
            vegiCount = 0

    params = {'allVegis': allVegis, 'allVegiCount': vegiCount}
    # params = {'allVegiCount': vegiCount}
    return params

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    if(request.session.has_key('UserEmail') == True):
        return render(request, 'VegiApp/dashboard.html')
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def icons(request):
    if(request.session.has_key('UserEmail') == True):
        return render(request, 'VegiApp/icons.html')
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user(request):
    if(request.session.has_key('UserEmail') == True):
        params = getAllUsers(request.session['UserRole'], request.session['UserEmail'])
        return render(request, 'VegiApp/user.html', params)
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def categories(request):
    if(request.session.has_key('UserEmail') == True):
        params = getAllCategories(request.session['UserRole'])
        return render(request, 'VegiApp/categories.html', params)
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def vegis(request):
    if(request.session.has_key('UserEmail') == True):
        params = getAllVegiFruits(request.session['UserRole'])
        return render(request, 'VegiApp/vegis.html', params)
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addVegiFruits(request):
    if(request.session.has_key('UserEmail') == True):
        if request.method == "POST":
            if request.FILES.get('vImage', None) != None:
                vName = request.POST.get('vName')
                vMPrice = request.POST.get('vMPrice')
                vOPrice = request.POST.get('vOPrice')
                vStock = request.POST.get('vStock')
                vPPWeight = request.POST.get('vPPWeight')
                vSKU = request.POST.get('vSKU')
                vCatId = request.POST.get('vCatId')
                vDesc = request.POST.get('vDesc')
                vStatus = request.POST.get('vStatus')

                if(vStatus == None or vStatus == 0):
                    vStatus = 0

                vImage = request.FILES['vImage']

                vi = ""
                fs = FileSystemStorage()
                cat = VFCategory.objects.get(catId = vCatId)
                if(cat.catName == 'Fruits'):
                    vi = fs.save('fruits/' + vImage.name, vImage)
                if(cat.catName == 'Vegis'):
                    vi = fs.save('vegis/' + vImage.name, vImage)

                v = VegiFruits()
                v.vegifruitName = vName
                v.vegifruitMarketPrice = vMPrice
                v.vegifruitOurPrice = vOPrice
                v.vegifruitTotalStock = vStock
                v.vegifruitPricePerWeight = vPPWeight
                v.vegifruitSKU = vSKU
                v.catId = vCatId
                v.vegifruitDescription = vDesc
                v.vegifruitStatus = vStatus
                v.vegifruitImage = vi
                v.save()

                request.session['success'] = True
                request.session['msg'] = "Vegi Inserted Successfully."

                return redirect('/admin-site/vegis')
            else:
                returnMsg = "Please select Vegi image."
                returnMsgType = "error"

                allCategories = VFCategory.objects.filter(catStatus = 1)
                params = {'msgtype': returnMsgType, 'msg': returnMsg, 'allCategories': allCategories}

            return render(request, 'VegiApp/addVegis.html', params)
        else:
            allCategories = VFCategory.objects.filter(catStatus = 1)
            params = {'allCategories': allCategories}
            return render(request, 'VegiApp/addVegis.html', params)
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteVegiFruits(request):
    if(request.session.has_key('UserEmail') == True):
        if(request.method == "POST"):
            delId = request.POST.get('delId')
            aa = VegiFruits.objects.get(vegifruitId = delId)
            
            fs = FileSystemStorage()
            fs.delete(aa.vegifruitImage)
            
            aa.delete()

            request.session['success'] = True
            request.session['msg'] = "Vegi-Fruit Deleted Successfully."
            return redirect('/admin-site/vegis/')
        else:
            return HttpResponse("Access Denied.!")
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editVegiFruits(request):
    if(request.session.has_key('UserEmail') == True):
        editId = request.POST.get('editId')
        if(request.method == "POST"):
            cc = VegiFruits.objects.get(vegifruitId = editId)
            allCategories = VFCategory.objects.filter(catStatus = 1)
            params = {'singleVegiFruit': cc, 'allCategories': allCategories}

            return render(request, 'VegiApp/editVegis.html', params)
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def saveVegiFruits(request):
    if(request.session.has_key('UserEmail') == True):
        if request.method == "POST":
            vi = ""
            vStatus = 0

            vName = request.POST.get('vName')
            vMPrice = request.POST.get('vMPrice')
            vOPrice = request.POST.get('vOPrice')
            vStock = request.POST.get('vStock')
            vPPWeight = request.POST.get('vPPWeight')
            vSKU = request.POST.get('vSKU')
            vCatId = request.POST.get('vCatId')
            vDesc = request.POST.get('vDesc')
            vStatus = request.POST.get('vStatus')
            
            if(vStatus == None or vStatus == 0 or vStatus == '0' or vStatus == 'off'):
                vStatus = 0
            elif(vStatus == 1 or vStatus == '1' or vStatus == 'on'):
                vStatus = 1

            editId = request.POST.get('editId')
            
            if request.FILES.get('vImage', None) != None:
                vImage = request.FILES['vImage']

                fs = FileSystemStorage()
                fs.delete(request.POST.get('allReadyImage'))
                cat = VFCategory.objects.get(catId = vCatId)
                if(cat.catName == 'Fruits'):
                    vi = fs.save('fruits/' + vImage.name, vImage)
                if(cat.catName == 'Vegis'):
                    vi = fs.save('vegis/' + vImage.name, vImage)
            else:
                vi = request.POST.get('allReadyImage')

            v = VegiFruits.objects.get(vegifruitId = editId)
            v.vegifruitName = vName
            v.vegifruitMarketPrice = vMPrice
            v.vegifruitOurPrice = vOPrice
            v.vegifruitTotalStock = vStock
            v.vegifruitPricePerWeight = vPPWeight
            v.vegifruitSKU = vSKU
            v.catId = vCatId
            v.vegifruitDescription = vDesc
            v.vegifruitStatus = vStatus
            v.vegifruitImage = vi
            v.save()

            request.session['success'] = True
            request.session['msg'] = "Vegi Updated Successfully."

            return redirect('/admin-site/vegis')
    else:
        return redirect('/')