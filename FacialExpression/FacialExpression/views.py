from django.http import HttpResponse
from django.shortcuts import render, redirect
from Project import TestData
from django.urls import reverse
import os
import random

def home(request):
    return render(request, "home.html")

def match(request):
    det_emo = TestData.Test()
    return redirect('/emotion?emo=' +  det_emo)

def emotion(request):
    emo = request.GET.get('emo')

    path= "\\" + emo
    files=os.listdir(".\\static"+path)
    d=random.choice(files)
    song_url = path + "\\" + d
    
    return render(request, "Emotion.html",{"emo": emo, "song_url": song_url})
