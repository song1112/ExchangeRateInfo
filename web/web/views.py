# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):

    return render(request, 'index.html')
