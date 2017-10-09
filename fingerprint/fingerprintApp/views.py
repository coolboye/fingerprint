# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
from fingerprintApp.models import LockUser, LockUse

from django.utils import timezone

import sqlite3

# Create your views here.

BASE_DIR = 'D:\\web\\fingerprint\\'

def appgetstate(request):
    #http://127.0.0.1:8000/fingerprint/appgetstate/?p1=lock_id
    lockId = request.GET.get('p1')
    conn = sqlite3.connect(BASE_DIR + 'db.sqlite3')
    cursor = conn.execute("SELECT lock_state,state from fingerprintApp_lockuse WHERE lock_id = ('%s')" % (lockId))
    for row in cursor:
        lock_state = row[0]
        state = row[1]
    conn.close()
    if state == '1':
        return HttpResponse(lock_state)
    else:
        return HttpResponse('error')

def getstate(request):
    #http://127.0.0.1:8000/fingerprint/getstate/?p1=lock_id
    lockId = request.GET.get('p1')
    conn = sqlite3.connect(BASE_DIR + 'db.sqlite3')
    cursor = conn.execute("SELECT lock_state from fingerprintApp_lockuse WHERE lock_id = ('%s')" % (lockId))
    for row in cursor:
        lock_state = row[0]
    conn.close()
    return HttpResponse(lock_state)

def updatestate(request):
    #http://127.0.0.1:8000/fingerprint/updatestate/?p1=lock_id&p2=state&p3=retrn
    lockUseTime = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    lockId = request.GET.get('p1')
    lockState = request.GET.get('p2')
    state = request.GET.get('p3')
    conn = sqlite3.connect(BASE_DIR + 'db.sqlite3')
    conn.execute("UPDATE fingerprintApp_lockuse set lock_state = ('%s'),state = ('%s'),last_use_time = ('%s') where lock_id=('%s')" % (lockState,state,lockUseTime,lockId))
    conn.commit()
    conn.close()
    return HttpResponse("updateok")

def login(request):
    #http://192.168.1.105:8000/fingerprint/login/?p1=user&p2=password
    user = request.GET.get('p1')
    password = request.GET.get('p2')
    conn = sqlite3.connect(BASE_DIR + 'db.sqlite3')
    cursor = conn.execute("SELECT user,password,lock_id from fingerprintApp_lockuser")
    for row in cursor:
        user_db = row[0]
        password_db = row[1]
        lock_id_db = row[2]
        if user_db == user and password_db == password:
            conn.close()
            return HttpResponse(lock_id_db)
    conn.close()
    return HttpResponse('no')

def register(request):
    #http://192.168.1.105:8000/fingerprint/register/?p1=user&p2=lock_id&p3=password
    user = request.GET.get('p1')
    lock_id = request.GET.get('p2')
    password = request.GET.get('p3')
    conn = sqlite3.connect(BASE_DIR + 'db.sqlite3')
    cursor = conn.execute("SELECT user from fingerprintApp_lockuser")
    for row in cursor:
        user_db = row[0]
        if user_db == user:
            conn.close()
            return HttpResponse('no')
    conn.execute("INSERT INTO fingerprintApp_lockuse (lock_id) VALUES ('%s')" % (lock_id));
    conn.execute("INSERT INTO fingerprintApp_lockuser (user,lock_id,password) VALUES ('%s', '%s', '%s')" % (user,lock_id,password));
    conn.commit()
    conn.close()
    return HttpResponse("ok")













    
