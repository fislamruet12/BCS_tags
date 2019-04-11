from django.shortcuts import render, redirect
from .models import subjects, subcatagory, contcatagory,contentelement
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
import logging
from django.http import JsonResponse
from .serializers import Inforserializer
import simplejson
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def homeviews(request):
    value = subjects.objects.all()
    ids = 1
    subcat = subcatagory.objects.filter(subject_id=ids)
    context = {
        'value': value,
        'subcat': subcat,
        'ids': ids,
    }
    return render(request, 'Subinfo/home.html', context)


def tempviews(request, userid):

    rendervalue = subjects.objects.get(pk=userid)
    subcat = rendervalue.subcatagory_set.all().first()
    content=subcat.contcatagory_set.all().first()
    catid=content.id
    context = {
        'rendervalue': rendervalue,
        'userid': userid,
        'catid':catid


    }
    return render(request, 'Subinfo/testing.html', context)


def catalogviews(request, userid, catid):
    value = subjects.objects.all()
    rendervalue = subjects.objects.get(pk=userid)
    catalogs = contcatagory.objects.get(pk=catid)

    split = []
    besplit = catalogs.contentelement_set.all()

    for sp in besplit:
        split.append(sp.content.split('.'))

    context = {
        'value': value,
        'rendervalue': rendervalue,
        'catalogs': catalogs,
        'userid': userid,
        'split': split,
        'catid':catid
    }
    return render(request, 'Subinfo/index.html', context)


def registerviews(request):
    c_u = request.POST.get("next")
    if request.user.is_authenticated:
        return redirect(c_u)
    form = RegisterForm
    context = {
        'form': form,
    }

    if request.method == "POST":
        user = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password != re_password:
            raise ValueError('Password did not match')
        else:
            CreateUser = User.objects.create(username=user, email=email)
            CreateUser.set_password(password)
            CreateUser.save()
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect(c_u)
    return render(request, 'Subinfo/register.html', context)


def LoginViews(request):
    form = LoginForm
    context = {
        'form': form,
    }

    c_u = request.POST.get("next")
    if request.user.is_authenticated:
        return redirect(c_u)
    else:
        if request.method == "POST":
            user = request.POST.get("user")
            password = request.POST.get("password")
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect(c_u)
    return render(request, 'Subinfo/login.html', context)


def DoLogout(request):
    logout(request)
    return redirect('/info/home/')


def testings(request, userid, catid):

    rendervalue = subjects.objects.get(pk=userid)
    context = {
        'rendervalue': rendervalue,
        'userid': userid,
        'catid':catid
    }
    return render(request, 'Subinfo/testing.html', context)


def questions(request):
    return render(request, 'Subinfo/questions.html', {})



def information(request, userid, catid):
    if request.method == 'GET':
        pt=contcatagory.objects.get(pk=catid)
        dt = pt.contentelement_set.all()
        serializer = Inforserializer(dt, many=True)
        return JsonResponse(serializer.data, safe=False)

def playit(request):
    return render(request, 'Subinfo/playit.html', {})

