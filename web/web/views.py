# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from dbhandle import handle


@csrf_exempt
def index(request):
    if request.method == 'GET':
        type = ''
        usd = ''
        try:
            type = request.GET.get('type')
            h = handle()
            h.getToday()
            if type == 'cashsell':
                type = '現金賣出'
                usd = h.usdco
                hkd = h.hkdco
                gbp = h.gbpco
                aud = h.audco
                cad = h.cadco
                sgd = h.sgdco
                jpy = h.jpyco
                eur = h.eurco
                cny = h.cnyco
            elif type == 'spotsell':
                type = '即期賣出'
                usd = h.usdso
                hkd = h.hkdso
                gbp = h.gbpso
                aud = h.audso
                cad = h.cadso
                sgd = h.sgdso
                jpy = h.jpyso
                eur = h.eurso
                cny = h.cnyso
            elif type == 'spotbuy':
                type = '即期買入'
                usd = h.usdsi
                hkd = h.hkdsi
                gbp = h.gbpsi
                aud = h.audsi
                cad = h.cadsi
                sgd = h.sgdsi
                jpy = h.jpysi
                eur = h.eursi
                cny = h.cnysi
            elif not type: 
                type = '現金買入'
                usd = h.usdci
                hkd = h.hkdci
                gbp = h.gbpci
                aud = h.audci
                cad = h.cadci
                sgd = h.sgdci
                jpy = h.jpyci
                eur = h.eurci
                cny = h.cnyci
            elif type == 'cashbuy':
                type = '現金買入'
                usd = h.usdci
                hkd = h.hkdci
                gbp = h.gbpci
                aud = h.audci
                cad = h.cadci
                sgd = h.sgdci
                jpy = h.jpyci
                eur = h.eurci
                cny = h.cnyci
            else:
                type = '現金買入'
                usd = h.usdci
                hkd = h.hkdci
                gbp = h.gbpci
                aud = h.audci
                cad = h.cadci
                sgd = h.sgdci
                jpy = h.jpyci
                eur = h.eurci
                cny = h.cnyci
        except Exception, ex:
            print 'here error:', ex.message
    return render(request, 'index.html', locals())
