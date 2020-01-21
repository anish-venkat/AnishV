from django.shortcuts import render
from signup.models import Signup
from signup.models import Search
from django.http import HttpResponseRedirect
from datetime import *
import mysql.connector 



# Create your views here.
pay=''
check=0
name='abc'
check=0    
name='abc'
p=[]
city ='abc'
order = ''
departure='bcd'
arrival='pdf'   
order='abc'
hotelid='shg'
hotelname='agd'
l=[]
hotelupdate='abc'        
datecheck=0
hotelidupdate='bcd'
hoteldateupdate=''
hoteldate2=''
rating=0

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
            con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
            mycursor= con.cursor()
            mycursor.execute("use sohan")
            mycursor.execute("select semail, suser from signup_signup")
            x=mycursor.fetchall()
            con.close()
            count=0
            for i in x:
                if email in i:
                    count= count + 1
                    
                    h=[]
                    d3={}
                    d3['wrong']="   This Email Is Already registered."
                    h.append(d3)
                    return render(request,'Signup1.html',{'wrong':h})
                elif name in i:
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


def dicti():
    global order
    global p
    global city
    global arrival
    global departure
    p=[]
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
    mycursor= con.cursor()
    mycursor.execute("use sohan")
    
    mycursor.execute("select * from hotels where hotelcity ='"+city+"' and odate<='"+arrival+"' and cdate>='"+departure+"' order by "+order+"")
    r = mycursor.fetchall()
    l=list(r)
    con.close()
    
    

    for i in l:
        
        d={}
        d['city']=i[1]
        d['name']=i[2]
        d['rating']=i[3]
        d['hotelid']=i[0]
        d['price']=i[8]
        p.append(d)
        print(d)
    
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
    if check==0:
        return HttpResponseRedirect('/login/')
    elif check==1:
        if request.method=="POST":
            hotelid=request.POST['hotid']
            hotelname=request.POST['bname']
            dict2()
        #mycursor.execute("update history delete * where (username='{}' and hotelid='{} and )").format(name,hotel,)
        con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
        mycursor= con.cursor()    
        mycursor.execute("insert into history values('{}','{}','{}','{}')".format(hotelid,arrival,departure,name))
    
        con.commit()
        con.close()

        return render(request,'confirmp.html',{'pay':l})

'''def account(request):
    global hotelid
    global hotelname
    global name
    global arrival
    global departure

    mycursor.execute("use sohan")'''
    

def account(request):
    global hotelupdate
    global check
    global name
    global datecheck
    global hotelidupdate
    global hoteldateupdate
    global hoteldate2
    if check==0:
        return HttpResponseRedirect('/login/')
    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
        mycursor= con.cursor()
        mycursor.execute("select history.hotelid, hotelname, arrival, departure from history,hotels where history.hotelid=hotels.hotelid and history.username='{}'".format(name))
        r = list(mycursor.fetchall())
        con.close()
        c=[]
        for i in r:
            
            d1={}
            d1['name']=name
            d1['arrival']=i[2]
            d1['departure']=i[3]
            d1['hotel']=i[1]
            d1['hotelid']=i[0]
            datecheck=i[2]
            #b= i[1].split('-')
            #for l in range(len(b)):
             #   b[l] = int(b[l])
            #m = date(b[0],b[1],b[2])
            #if i[1]>date.today():
                #d1['check']='y'
            #else:
                #d1['check']='n'
             #(,'%b. %d, %Y')
            sql2 = "select '{}'<(select curdate())".format(i[3])
            con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
            mycursor= con.cursor()  
            mycursor.execute(sql2)
            si = list(mycursor.fetchall())
            if si[0][0] == 1:
                d1['check'] = 'y'
            elif si[0][0]==0:
                d1['check'] = 'n'
            print(si[0])
    
            c.append(d1)
            
        con.close()
        print('hh',c)
        return render(request,"accounts.html",{'pay_l':c})
    #if request.method=="POST":
     #   hotelupdate=request.POST['bhotel']
      #  hotelidupdate=request.POST['bhotelid']
      #  hoteldateupdate=request.POST['barrival']
       # hoteldate2=request.POST['bdeparture']
       # mycursor.execute("delete from history where username='{}' and hotelid='{}' and arrival='{}' and departure='{}'").format(name,hotelidupdate,hoteldateupdate,hoteldate2)
       # return HttpResponseRedirect('/search/')
    
        
    

    
    
'''def update(request):
    global hotelupdate
    global datecheck
    global name
    global hotelidupdate
    global hoteldateupdate
    global hoteldate2

    if request.method=="POST":
        newrating=request.POST['crating']
        newarrival=request.POST['carrival']
        newdeparture=request.POST['cdeparture']
        newguests=request.POST['cguests']
        mycursor.execute("delete from history where username='{}' and hotelid='{}' and arrival='{}' and departure='{}'").format(name,hotelidupdate,hoteldateupdate,hoteldate2)
        

        return HttpResponseRedirect('/search/')
    
    
    #else:
        #return render(request,'update.html')'''
    
    
        
def cancel(request):
    global hotelupdate
    global datecheck
    global name
    global hotelidupdate
    global hoteldateupdate
    global hoteldate2

    hotelupdate=request.POST['bhotel']
    hotelidupdate=request.POST['bhotelid']
    hoteldateupdate=request.POST['barrival']
    hoteldate2=request.POST['bdeparture']
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
    mycursor= con.cursor()
    sql="delete from history where username='{}' and hotelid='{}' and arrival='{}' and departure='{}'".format(name,hotelidupdate,datetime.strptime(hoteldateupdate,'%b. %d, %Y'),datetime.strptime(hoteldate2, '%b. %d, %Y'))
    print('dd',sql)
    mycursor.execute(sql)
    con.commit()
    con.close()
    return HttpResponseRedirect('/accounts/')

def trial(request):
    global hotelupdate
    global datecheck
    global name
    global hotelidupdate
    global hoteldateupdate
    global hoteldate2

    hotelupdate=request.POST['bhotel']
    hotelidupdate=request.POST['bhotelid']
    hoteldateupdate=request.POST['barrival']
    hoteldate2=request.POST['bdeparture']
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
    mycursor= con.cursor()
    sql="delete from history where username='{}' and hotelid='{}' and arrival='{}' and departure='{}'".format(name,hotelidupdate,datetime.strptime(hoteldateupdate,'%b. %d, %Y'),datetime.strptime(hoteldate2, '%b. %d, %Y'))
    mycursor.execute(sql)
    con.commit()
    con.close()
    return HttpResponseRedirect('/accounts/')

def rating(request):
    global hotelupdate
    global datecheck
    global name
    global hotelidupdate
    global hoteldateupdate
    global hoteldate2
    global rating

    hotelupdate=request.POST['bhotel']
    hotelidupdate=request.POST['bhotelid']
    hoteldateupdate=request.POST['barrival']
    hoteldate2=request.POST['bdeparture']
    rating=request.POST['brating']
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="sohan")
    mycursor= con.cursor()
    sql="select ratings, No_rating from hotels where hotelid='{}' and hotelname='{}'".format(hotelidupdate,hotelupdate)
    mycursor.execute(sql)
    fetch_rating=mycursor.fetchone()
    rating1=int(fetch_rating[0])
    no_ratings=int(fetch_rating[1])
    newrating=((rating1*no_ratings)+int(rating))/(no_ratings+1)
    no_ratings+=1
    sql="update hotels set ratings={} and No_rating = {}".format(rating1,no_ratings)
    mycursor.execute(sql)
    con.commit()
    con.close()
    return HttpResponseRedirect('/accounts/')
    
    
    
def logout(request):
    global check
    global pay
    pay = ''
    pay2 = ''
    check = 0
    name=''
    return HttpResponseRedirect('/login/')

    
