from django.shortcuts import render
from signup.models import Signup
from signup.models import Search
from django.http import HttpResponseRedirect
from datetime import *
import mysql.connector 
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
mycursor= con.cursor()


# Create your views here.
pay=''
check=0
name='abc'
def home(request):
    global pay
    global check
    global name
    if check == 0:
        
        return render(request,'home.html')
    else:
        h=[]
        d3={}
        d3['name']="Welcome, "+ name
        h.append(d3)
       
        return render(request,"home.html",{'pay':h})
    

    

def sign(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST["cpassword"]
        if cpassword==password:
            mycursor.execute("use sohan")
            mycursor.execute("select semail, suser from signup_signup")
            x=mycursor.fetchall()
            count=0
            for i in x:
                if email in i:
                    count= count + 1
                    
                    h=[]
                    d3={}
                    d3['wrong']="   This Email Is Already registered."
                    h.append(d3)
                    return render(request,'Signup1.html',{'wrong':h})
                elif user in i:
                    count= count + 1
                    
                    h1=[]
                    d4={}
                    d4['wrong']="   This Username Is Already registered."
                    h1.append(d4)
                    return render(request,'Signup1.html',{'wrong':h1})
                    
                    
            if count==0:
                lst=Signup()
                lst.suser=name
                lst.semail=email
                lst.spassword=password
                lst.save()
                return HttpResponseRedirect('/login/')
    else:
        return render(request,'Signup1.html')
           # return render(request,'login.html')
        
    #else:
       # return render(request,'Signup1.html')
check=0    
name='abc'
def login(request):
    global name
    global check
    
    if request.method=="POST":
        name=request.POST['username']
        password=request.POST['password']
        post=Signup.objects.get(suser=name)
        d3={}
        d3['passwrong']='Wrong Username or Password'
        k=[]
        k.append(d3)
        if (post):
            if (post.spassword==password):
                check=1
                return HttpResponseRedirect('/home/')
            
            
            else:
                
                return render(request,"login.html",{'pay2':k})
                '''lst=Login()
        lst.user=username
        lst.pwd=password
    
        lst.save()
        return render(request,'offers.html')'''
    else:
        
        return render(request,"login.html")

#creating a function to check the city entered by user and displaying hotels#
p=[]
city ='abc'
order = ''

def dicti():
    global order
    global p
    global city
    global arrival
    global departure
    p=[]
    mycursor.execute("use sohan")
    
    mycursor.execute("select * from hotels where hotelcity ='"+city+"' and odate<='"+arrival+"' and cdate>='"+departure+"' order by "+order+"")
    r = mycursor.fetchall()
    l=list(r)
    
    

    for i in l:
        
        d={}
        d['city']=i[1]
        d['name']=i[2]
        d['rating']=i[3]
        d['hotelid']=i[0]
        p.append(d)
departure='bcd'
arrival='pdf'   
order='abc'     
def search(request):
    global city
    global order
    global departure
    global arrival
    global order
    if request.method=="POST":
        city=request.POST['city']
        guests=request.POST['guests']
        arrival=request.POST['arrival']
        departure=request.POST['departure']
        order=request.POST['preference']
        if order == 'Price':
            order = "price asc"
        else:
            order = "ratings desc"
        lst2=Search()
        lst2.lcity=city
        lst2.lguests=guests
        lst2.larrival=arrival
        lst2.ldeparture=departure
        lst2.save()
        dicti()
        return render(request,"result1.html",{'pay_l':p})
    
    
    
    else:
        return render(request,"search.html")

#Priting out a confirmation page.

hotelid='shg'
hotelname='agd'
l=[]

def dict2():
    global name
    global hotelid
    global arrival
    global departure
    global l
    global hotelname
    l=[]
    d1={}
    d1['name']=name
    d1['arrival']=arrival
    d1['departure']=departure
    d1['hotel']=hotelname
    l.append(d1)


def book(request):
    global hotelid
    global hotelname
    global name
    if request.method=="POST":
        hotelid=request.POST['hotid']
        hotelname=request.POST['bname']
        dict2()
    mycursor.execute("update history delete * where (username='{}' and hotelid='{} and )").format(name,hotel,)
    mycursor.execute("insert into history values('{}','{}','{}','{}')".format(hotelid,arrival,departure,name))
    
    con.commit()

    return render(request,'confirm1.html',{'pay':l})

'''def account(request):
    global hotelid
    global hotelname
    global name
    global arrival
    global departure

    mycursor.execute("use sohan")'''
    
hotelupdate='abc'        
datecheck=0
def account(request):
    global hotelupdate
    global check
    global name
    global datecheck
    if check==0:
        return HttpResponseRedirect('/login/')
    else:
        mycursor.execute("select hotelname, arrival, departure from history,hotels where history.hotelid=hotels.hotelid and history.username='{}'".format(name))
        r = list(mycursor.fetchall())
        c=[]
        for i in r:
            
            d1={}
            d1['name']=name
            d1['arrival']=i[1]
            d1['departure']=i[2]
            d1['hotel']=i[0]
            datecheck=i[1]
            #b= i[1].split('-')
            #for l in range(len(b)):
             #   b[l] = int(b[l])
            #m = date(b[0],b[1],b[2])
            #if i[1]>date.today():
                #d1['check']='y'
            #else:
                #d1['check']='n'
            
            
            c.append(d1)
            
        
        
        return render(request,"accounts.html",{'pay_l':c})
    if request.method=="POST":
        hotelupdate=request.POST['bhotel']
        return HttpResponseRedirect('/search/')
    
        
    

    
    
'''def update(request):
    global hotelupdate
    global datecheck
    global name

    if request.method=="POST":
        newrating=request.POST['crating']
        newarrival=request.POST['carrival']
        newdeparture=request.POST['cdeparture']
        newguests=request.POST['cguests']

    s="update table''' 
        
        
    
        
        
        
    
        
        
        
        
        
    
    
    
def logout(request):
    global check
    global pay
    pay = ''
    check = 0
    name=''
    return HttpResponseRedirect('/login/')

    
