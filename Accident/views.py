import datetime
import smtplib
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def loginn(request):
    return render(request,"index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = Login.objects.filter(username = username,password = password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"

        if data.type == 'admin':
            return redirect('/admin_home')
        elif data.type == 'hospital':
            return redirect('/hospital_home')
        elif data.type == 'pending':
            return HttpResponse("<script>alert('wait for authentication');window.location='/'</script>")
        elif data.type == 'policestation':
            return redirect('/policestation_home')
    else:
        return HttpResponse("<script>alert('Invalid User');window.location='/'</script>")

def admin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"admin/index.html")

def hospital_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"hospital/index.html")

def policestation_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    return render(request,"police station/index.html")


def logout(request):
    request.session["lg"]=""
    return redirect('/')


def view_registered_hospital(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Hospital.objects.filter(LOGIN__type='pending')
    return render(request,"admin/view_registered_hospital.html",{"data":data})

def registered_hospital_approve(request,id,email):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Login.objects.filter(id=id).update(type='hospital')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Accident Detection")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))
    return redirect('/view_registered_hospital#aa')

def registered_hospital_reject(request,id,email):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Login.objects.filter(id=id).update(type='reject')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Accident Detection")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))
    return redirect('/view_registered_hospital#aa')

def view_approved_hospital(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Hospital.objects.filter(LOGIN__type='hospital')
    return render(request,"admin/view_approved_hospital.html",{"data":data})

def view_doctorin_hospital(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Doctor.objects.all()
    return render(request,"admin/view_doctor.html",{"data":data})

def view_registered_policestation(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Police_station.objects.filter(LOGIN__type='pending')
    return render(request,"admin/view_registered_policestation.html",{"data":data})

def registered_policestation_approve(request,id,email):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Login.objects.filter(id=id).update(type='policestation')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Accident Detection")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))

    return redirect('/view_registered_policestation#aa')



def registered_policestation_reject(request,id,email):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Login.objects.filter(id=id).update(type='reject')
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("Accident Detection")
    msg['Subject'] = 'Verification'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))
    return redirect('/view_registered_policestation#aa')

def view_approved_policestation(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Police_station.objects.filter(LOGIN__type='policestation')
    return render(request,"admin/view_approved_policestation.html",{"data":data})

def view_registered_user(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = User.objects.all()
    return render(request,"admin/view_registered_user.html",{"data":data})

def view_accident_detection(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Accident.objects.all()
    return render(request,"admin/view_accident_detection.html",{"data":data})

#############################################################################################

# Hospital Module

def register(request):
    return render(request,"hospital/register.html")

def register_post(request):
    name = request.POST['textfield']
    photo = request.FILES['fileField']          # Image field
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Accident_Detection\Accident\static\\"+d+'.jpg',photo)
    photo='/static/'+d+'.jpg'
    place = request.POST['textfield2']
    post = request.POST['textfield9']
    pin = request.POST['textfield4']
    lattitude = request.POST['textfield5']
    longitude = request.POST['textfield6']
    email = request.POST['textfield7']
    phone_no = request.POST['textfield8']
    password = request.POST['textfield10']

    log = Login.objects.filter(username=email)
    if log.exists():
        return HttpResponse("<script>alert('already exists');window.location='/'</script>")
    else:
        log_obj = Login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'pending'
        log_obj.save()
        obj = Hospital()
        obj.name = name
        obj.photo = photo
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.lattitude = lattitude
        obj.longitude = longitude
        obj.email = email
        obj.phone_no = phone_no
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('Registered successfully');window.location='/register'</script>")

# Doctor Managment

def add_doctor(request):
    return render(request,"hospital/add_doctor.html")

def add_doctor_post(request):
    name = request.POST['textfield']
    designation = request.POST['textfield2']
    email = request.POST['textfield3']
    phone_no = request.POST['textfield4']
    obj = Doctor()
    obj.name = name
    obj.designation = designation
    obj.email = email
    obj.phone_no = phone_no
    obj.HOSPITAL = Hospital.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/view_doctor#aa'</script>")

def view_doctor(request):
    data = Doctor.objects.filter(HOSPITAL=Hospital.objects.get(LOGIN=request.session['lid']))
    return render(request,"hospital/view_doctor.html",{"data":data})

def update_doctor(request,id):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Doctor.objects.get(id=id)
    return render(request,"hospital/update_doctor.html",{"data":data})

def update_doctor_post(request,id):
    name = request.POST['textfield']
    designation = request.POST['textfield2']
    email = request.POST['textfield3']
    phone_no = request.POST['textfield4']
    Doctor.objects.filter(id=id).update(name = name,designation=designation,email=email,phone_no=phone_no)
    return HttpResponse("<script>alert('updated successfully');window.location='/view_doctor#aa'</script>")

def delete_doctor(request,id):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Doctor.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/add_doctor'</script>")


# Fecility Management

def fecility_add(request):
    return render(request,"hospital/add_fecility.html")

def fecility_add_post(request):
    fecility_type = request.POST['textfield']
    details = request.POST['textfield2']
    obj = Fecility()
    obj.fecility_type = fecility_type
    obj.details = details
    obj.HOSPITAL = Hospital.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('added successfully');window.location='/feciity_view#aa'</script>")

def feciity_view(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Fecility.objects.filter(HOSPITAL=Hospital.objects.get(LOGIN=request.session['lid']))
    return render(request,"hospital/view_fecility.html",{"data":data})

def fecility_update(request,id):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Fecility.objects.get(id=id)
    return render(request,"hospital/update_fecility.html",{"data":data})

def fecility_update_post(request,id):
    fecilities = request.POST['textfield']
    details = request.POST['textfield2']
    Fecility.objects.filter(id=id).update(fecility_type = fecilities,details =details)
    return HttpResponse("<script>alert('Updated successfully');window.location='/feciity_view#aa'</script>")

def fecility_delete(request,id):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    Fecility.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/feciity_view'</script>")

def update_accident_report(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    hid = Hospital.objects.get(LOGIN= request.session['lid'])
    data = Report.objects.filter(status='pending',HOSPITAL=hid)

    return render(request,"hospital/update_accident_report.html",{"data":data})

def update_report(request,id,aid):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")

    Accident.objects.filter(id=aid).update(status='reported')
    Report.objects.filter(id=id).update(status='reported')
    hid = Hospital.objects.get(LOGIN= request.session['lid'])

    data1 = Report.objects.filter(~Q(HOSPITAL= hid),ACCIDENT=aid)
    print(data1)
    for i in data1:
        rid = i.id          # report id
        Report.objects.get(id=rid).delete()
    return redirect('/update_accident_report')

def view_accident_detections(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Report.objects.filter(HOSPITAL=Hospital.objects.get(LOGIN=request.session['lid']))
    return render(request,"hospital/view_accident_detection.html",{"data":data})


def view_policestation(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Police_station.objects.all()
    return render(request,"hospital/view_policestation.html",{"data":data})

#########################################################################################################


# Police station module

def police_registration(request):
    return render(request,"police station/police_register.html")

def police_registration_post(request):
    station_name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    phone_no = request.POST['textfield6']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Accident_Detection\Accident\static\\" + d + '.jpg', photo)
    photo = '/static/' + d + '.jpg'
    password = request.POST['textfield7']
    lattitude = request.POST['textfield8']
    longitude = request.POST['textfield9']

    lob = Login.objects.filter(username=email)
    if lob.exists():
        return HttpResponse("<script>alert('already exists');window.location='/police_registration'</script>")
    else:
        log_obj = Login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'pending'
        log_obj.save()
        obj = Police_station()
        obj.station_name = station_name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.phone_no = phone_no
        obj.photo = photo
        obj.lattitude = lattitude
        obj.longitude = longitude
        obj.LOGIN =log_obj
        obj.save()
        return HttpResponse("<script>alert('Registered successfully');window.location='/police_registration'</script>")

def view_nearby_hospital(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    data = Hospital.objects.filter(LOGIN__type='hospital')
    return render(request, "police station/view_nearby_hospital.html",{"data":data})

def view_accidents(request):
    if request.session['lg'] == '':                 # Can be used the page without page refereshment
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    # data = Report.objects.filter(ACCIDENT=id).update(status='pending')
    data = Accident.objects.filter(status='pending')
    return render(request,"police station/view_accident_detection.html",{"data":data})

def Notitfication_to_hospital(request,lattitude,longitude):
    data = Hospital.objects.all()
    return render(request,"police station/view_hospitals.html",{"data":data,"data1":lattitude,"data2":longitude})

def send_email(request,email,lattitude,longitude):
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('riss.princytv@gmail.com', 'vile vivc hvnh xdgs')           # creating an dummy email and create app code
    except Exception as e:
        print("Couldn't setup email!!" + str(e))
    msg = MIMEText("accident, unexpected event, typically sudden in nature and associated with injury-Accident Detected"+"\n"+"https://www.google.com/maps/?q='"+lattitude+"','"+longitude+"'")
    msg['Subject'] = 'Accident Information'
    msg['To'] = email
    msg['From'] = 'riss.princytv@gmail.com'
    try:
        gmail.send_message(msg)
    except Exception as e:
        print("COULDN'T SEND EMAIL", str(e))
    return HttpResponse("<script>alert('successfully sended');window.location='/view_accidents#aa'</script>")
    # return redirect('/view_accidents#aa')

#######################################################################################################################

# Android user module

def android_login(request):
    username = request.POST['name']
    password = request.POST['password']
    data = Login.objects.filter(username = username,password = password)
    if data.exists():
        lid = data[0].id
        print(lid)
        logininstance = Login.objects.get(id = lid)
        res = User.objects.get(LOGIN=lid)
        type = data[0].type
        name = res.name
        email = res.email
        photo = res.photo
        print(photo)
        return JsonResponse({'status':"ok",'lid':lid,'type':type,'name':name,'email':email,'photo':photo})
    else:
        return JsonResponse({"status":None})

def android_user_registration(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    house_name = request.POST['house_name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    photo = request.FILES['pic']            #Image field
    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Accident_Detection\Accident\static\\" + d + '.jpg', photo)
    photo = '/static/' + d + '.jpg'
    password = request.POST['password']

    data = Login.objects.filter(username=email)
    if data.exists():
        return JsonResponse({"status":None})
    else:

        log_obj = Login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'user'
        log_obj.save()

        obj = User()
        obj.name = name
        obj.gender = gender
        obj.dob = dob
        obj.house_name = house_name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.phone_no = contact
        obj.photo = photo
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({'status': "ok"})

def android_view_nearby_hospital(request):
    qry = Hospital.objects.filter(LOGIN__type='hospital')
    lati = request.POST['lati']
    longi = request.POST['longi']

    latitude = str(lati)
    longitude = str(longi)
    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"

    ar = []
    for i in qry:
        qs = Hospital.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.lattitude, i.longitude, i.lattitude))).order_by('distance')
        ar.append(
            {
                "hid": i.id,
                "name": i.name,
                "place": i.place,
                "post": i.post,
                "pin": i.pin,
                "email": i.email,
                "phone_no": i.phone_no,
                "photo": i.photo,
                "lattitude": i.lattitude,
                "longitude": i.longitude,
                "hospital_distance": qs[0].distance
            }
        )

    def Hospital_nearby_sort(e):
        return e['hospital_distance']
    ar.sort(key=Hospital_nearby_sort)

    return JsonResponse({"status": "ok", "data": ar})

def android_view_doctor(request):
    hid = request.POST['hid']
    res = Doctor.objects.filter(HOSPITAL=hid)
    ar =[]
    for i in res:
        ar.append(
            {
                "did":i.id,
                "name":i.name,
                "designation":i.designation,
                "email":i.email,
                "phone_no":i.phone_no
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_fecility(request):
    hid = request.POST['hid']
    res = Fecility.objects.filter(HOSPITAL=hid)
    ar = []
    for i in res:
        ar.append(
            {
                "fid":i.id,
                "fecility_type":i.fecility_type,
                "details":i.details
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_nearby_policestation(request):
    lati = request.POST['lati']
    longi = request.POST['longi']

    latitude = str(lati)
    longitude = str(longi)
    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"


    res = Police_station.objects.filter(LOGIN__type='policestation')
    ar =[]
    for i in res:
        qs = Police_station.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.lattitude, i.longitude, i.lattitude))).order_by('distance')
        ar.append(
            {
                "pid": i.id,
                "station_name": i.station_name,
                "place": i.place,
                "post": i.place,
                "pin": i.pin,
                "email": i.email,
                "phone_no": i.phone_no,
                "photo": i.photo,
                "police_distance": qs[0].distance

            }
        )

    def police_nearby_sort(e):
        return e['police_distance']
    ar.sort(key=police_nearby_sort)

    return  JsonResponse({"status":"ok","data":ar})

def android_view_accident_detection(request):
    aid = request.POST['lid']

    logininstance = Login.objects.get(id=aid)
    res = Accident.objects.filter(USER__LOGIN=logininstance)
    ar =[]
    for i in res:
        ar.append(
            {
                "aid":i.id,
                "lattitude":i.lattitude,
                "longitude":i.longitude,
                "place":i.place,
                "date":i.date,
                "time":i.time,
                "status":i.status
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_delete_accident(request):
    aid = request.POST['aid']
    Accident.objects.get(id=aid).delete()
    return JsonResponse({"status": "ok"})

# ====================================================================



#################### Technical Part ###########################

def accident_detection(request):
    lid = request.POST['lid']
    lati = request.POST['lati']
    longi = request.POST['longi']
    place = request.POST['place']
    # print("lattttttttttt",lati)
    date =datetime.datetime.now().strftime("%Y-%m-%d")

    latitude = str(lati)
    longitude = str(longi)

    ###### NEAR-BY code

    gcd_formula = "6371 * acos(least(greatest(cos(radians(%s)) * cos(radians('" + latitude + "')) * cos(radians('" + longitude + "') - radians(%s)) + sin(radians(%s)) * sin(radians('" + latitude + "')), -1), 1))"
    print(gcd_formula)
    # distance_raw_sql = RawSQL(
    #     gcd_formula, (latitude, longitude, latitude)
    # )
    qry = Hospital.objects.filter(LOGIN__type="hospital")
    li=[]
    for i in qry:
        qs = Hospital.objects.filter(id=i.id).annotate(
            distance=RawSQL(gcd_formula, (i.lattitude, i.longitude, i.lattitude))).order_by('distance')
        li.append({
            "hospital_id":i.id,
            "Hospital_distance":qs[0].distance

        })

    #### Distance arranging.........................

    def hospital_nearby_sort(e):
        return e['Hospital_distance']
    li.sort(key=hospital_nearby_sort)
    # print("hhhhh",li[0:6])
    # for i in li[0:6]:
    #     print(i)

    ####### Accident code...................


    data = Accident.objects.filter(USER=User.objects.get(LOGIN=lid),place=place,date=date)
    print("dataaaaa",data)
    if data.exists():
        aid = data[0].id
        Accident.objects.filter(id=aid).update(place=place)
        return JsonResponse({"status":"ok"})
    else:
        obj = Accident()
        obj.lattitude = lati
        obj.longitude = longi
        obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
        obj.time = datetime.datetime.now().strftime("%H:%M:%S")
        obj.place = place
        obj.status="pending"
        obj.USER = User.objects.get(LOGIN=lid)
        obj.save()
        for j in li[0:6]:
            hid=j['hospital_id']
            obj1=Report()
            obj1.ACCIDENT=obj
            obj1.HOSPITAL_id=hid
            obj1.date=date
            obj1.status="pending"
            obj1.save()

    return JsonResponse({"status":"ok"})