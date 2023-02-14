from django.shortcuts import render,redirect
from .models import *

def asosiy(request):
    qidiruv_sozi=request.GET.get('qidiruv')
    t_s = Togri.objects.filter(soz=qidiruv_sozi)
    if len(t_s)==1:
        n_s=Xato.objects.filter(stogri_fk=t_s[0])
    else:
        n_s=[]
        n=Xato.objects.filter(notogri=qidiruv_sozi)
        if len(n)==1:
            t_s=Togri.objects.filter(id=n[0].stogri_fk.id)
            n_s=Xato.objects.filter(stogri_fk=t_s[0])
        data={
            'togrisi':t_s,
            'notogri':n_s
        }
        return render(request,'result.html',data)




