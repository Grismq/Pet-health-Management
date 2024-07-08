from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import PetHealthMonitoring,PetAdoption
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        last=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        psw=request.POST['psw']
        psw1=request.POST['psw1']
        if psw==psw1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=first,
                last_name=last,email=email,username=uname,password=psw)
                user.save()
                return HttpResponseRedirect('login')
        else:
            messages.info(request,"Password not matching")
            return render(request,"register.html")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        psw=request.POST['psw']
        user=auth.authenticate(username=username,password=psw)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def pethealth(request):
    if request.method=="POST":
        animal=request.POST['animal']
        sym1=request.POST['sym1']
        sym2=request.POST['sym2']
        sym3=request.POST['sym3']
        sym4=request.POST['sym4']
        sym5=request.POST['sym5']
        from sklearn.preprocessing import LabelEncoder
        l=LabelEncoder()
        animal1=l.fit_transform([animal])
        sym11=l.fit_transform([sym1])
        sym12=l.fit_transform([sym2])
        sym13=l.fit_transform([sym3])
        sym14=l.fit_transform([sym4])
        sym15=l.fit_transform([sym5])

        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import plotly.express as px
        
        import warnings
        df=pd.read_csv(r'static/data-2.csv')
        print(df.head())
        print(df.info())
        dup_value = df.duplicated().sum()
        null_value = df.isnull().sum().sum()
        nan_value = df.isna().sum().sum()
        print(f'Total rows: {df.shape[0]}, Total columns: {df.shape[1]}')
        print(f'Total duplicate data: {dup_value} data')
        print(f'Total null values: {null_value} data')
        print(f'Total NaN values: {nan_value} data')
        print(df.describe(include='all'))
        print(df['Dangerous'].unique())
        df = df.dropna() # --> Drop all NaN values
        df = df.reset_index(drop=True) # --> mengurutkan nomor index
        df['Dangerous'].unique()
        dup_value = df.duplicated().sum()
        null_value = df.isnull().sum().sum()
        nan_value = df.isna().sum().sum()
        print(f'Total rows: {df.shape[0]}, Total columns: {df.shape[1]}')
        print(f'Total duplicate data: {dup_value} data')
        print(f'Total null values: {null_value} data')
        print(f'Total NaN values: {nan_value} data')
        print(df.loc[df.duplicated(keep=False)])
        df = df.drop_duplicates(keep=False)
        dup_value = df.duplicated().sum()
        null_value = df.isnull().sum().sum()
        nan_value = df.isna().sum().sum()
        print(f'Total rows: {df.shape[0]}, Total columns: {df.shape[1]}')
        print(f'Total duplicate data: {dup_value} data')
        print(f'Total null values: {null_value} data')
        print(f'Total NaN values: {nan_value} data')
        animalName = df["AnimalName"].value_counts().sort_values(ascending=False).head(5)
        fig = px.pie(animalName,
                    values='count',
                    names=animalName.index,
                    title="Animal Name Distribution",
                    width = 650, hole=0.45)
        fig.update_traces(textfont_size=14, textposition="outside")
        fig.show()
        symptoms1 = df["symptoms1"].value_counts().sort_values(ascending=False).head(5)
        fig = px.pie(symptoms1,
                    values='count',
                    names=symptoms1.index,
                    title="Symptoms 1 Distribution",
                    width = 650, hole=0.45)
        fig.update_traces(textfont_size=14, textposition="outside")
        fig.show()
        symptoms2 = df["symptoms2"].value_counts().sort_values(ascending=False).head(5)
        fig = px.pie(symptoms2,
                    values='count',
                    names=symptoms2.index,
                    title="Symptoms 2 Distribution",
                    width = 650, hole=0.45)
        fig.update_traces(textfont_size=14, textposition="outside")
        fig.show()
        symptoms3 = df["symptoms3"].value_counts().sort_values(ascending=False).head(5)
        fig = px.pie(symptoms3,
                    values='count',
                    names=symptoms3.index,
                    title="Symptoms 3 Distribution",
                    width = 650, hole=0.45)
        fig.update_traces(textfont_size=14, textposition="outside")
        fig.show()
        symptoms4 = df["symptoms4"].value_counts().sort_values(ascending=False).head(5)
        fig = px.pie(symptoms4,
                    values='count',
                    names=symptoms4.index,
                    title="Symptoms 4 Distribution",
                    width = 650, hole=0.45)
        fig.update_traces(textfont_size=14, textposition="outside")
        fig.show()
        top5Animals = df['AnimalName'].value_counts().head(5)
        fig = px.bar(top5Animals, y='count', x=top5Animals.index, text_auto='.2s',
                    title="Top 5 Animals Name by Count",
                    width=650, height=750)
        fig.update_traces(textfont_size=16, textangle=0, textposition="outside", cliponaxis=False)
        fig.show()
        animal_list = df[(df['AnimalName'] == 'Buffaloes') |
                 (df['AnimalName'] == 'Sheep') |
                 (df['AnimalName'] == 'Pig') |
                 (df['AnimalName'] == 'Fowl') |
                 (df['AnimalName'] == 'Elephant')]
        df=pd.read_csv(r"static/data-2.csv")
        print(df[0:3])
        print(df.isnull().sum())
        print(df.dropna(inplace=True))
        from sklearn.preprocessing import LabelEncoder
        l=LabelEncoder()
        animal_1=l.fit_transform(df["AnimalName"])
        sym_1=l.fit_transform(df["symptoms1"])
        sym_2=l.fit_transform(df["symptoms2"])
        sym_3=l.fit_transform(df["symptoms3"])
        sym_4=l.fit_transform(df["symptoms4"])
        sym_5=l.fit_transform(df["symptoms5"])
        df=df.drop(["AnimalName","symptoms1","symptoms2","symptoms3","symptoms4","symptoms5"],axis=1)
        print(df[0:3])
        df["Animal_Name"]=animal_1
        df["Symptoms_1"]=sym_1
        df["Symptoms_2"]=sym_2
        df["Symptoms_3"]=sym_3
        df["Symptoms_4"]=sym_4 
        df["Symptoms_5"]=sym_5


        X=df.drop("Dangerous",axis=1)
        print(X[0:2])
        y=df["Dangerous"]
        print(y[0:2])
        from sklearn.linear_model import LogisticRegression
        log=LogisticRegression()
        log.fit(X,y)
        import numpy as np 
        pred_x=pd.DataFrame(np.array([animal1,sym11,sym12,sym13,sym14,sym15]).reshape(1,-1),
        columns=["Animal_Name","Symptoms_1","Symptoms_2","Symptoms_3","Symptoms_4","Symptoms_5"])
        #data=np.array([[animal1,sym11,sym12,sym13,sym14,sym15]],dtype=object)
        prediction=log.predict(pred_x)
        print(prediction)
        pet=PetHealthMonitoring.objects.create(AnimalName=animal,
        Symptoms_1=sym1,Symptoms_2=sym2,Symptoms_3=sym3,Symptoms_4=sym4,
        Symptoms_5=sym5,Dangerous=prediction)
        pet.save()
        if (sym1=="Good" or sym2 =="Normal" or sym1=="Normal" or sym2=="Good"):
            pred1="No"
            recommend='''1.Provide Enrich Environment
                   2. Never Give Pets People Medication'''
            location=''''''
        elif (sym3=="Good" or sym4 =="Normal" or sym3=="Normal" or sym4=="Good"):
            pred1="No"
            recommend='''1.Provide Enrich Environment
                   2. Never Give Pets People Medication'''
            location=''''''
        elif (sym5=="Good" or sym5=="Normal"):
            pred1="No"
            recommend='''1.Provide Enrich Environment
                   2. Never Give Pets People Medication'''
            location=''''''
        else:
            pred1="Yes"
            recommend='''1.Maintain a Healthy Weight
                        2.Get Regular Vaccine
                        3. Prevent Parasites'''
            location='''https://maps.app.goo.gl/wNnLCW5NCpQ5VutL9'''
            print (location)
        print("Symptoms Data: ",pred1)
        return render(request,"predict.html",{"animal":animal,"sym1":sym1,"sym2":sym2,
        "sym3":sym3,"sym4":sym4,"sym5":sym5,"prediction":pred1,"recommend":recommend,"location":location})
    return render(request,"pethealth.html")

def predict(request):
    return render(request,"predict.html")

def adoption(request):
    pet=PetAdoption.objects.all()
    return render(request,"adoption.html",{"pet":pet})

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phn=request.POST['phn']
        en=request.POST['enquiry']
        em=request.POST['email']
        #user=User.objects.get(email=em)
        from redmail import outlook
        outlook.user_name = "techcitiforyou@outlook.com"
        outlook.password = "techcititech@1234"
        outlook.send(
            receivers="grismaangel82@gmail.com",
            subject="Enquiry Information",
                #text="Hi, this is an example."
            text = """\
                    Hi,
                Enquiry Details
                Name: {0}, 
                Email :{1},
                Phone No: {2},
                Message:{3}
                
                'admin@no-reply.com',
                    


                        \
                    """.format( name,em,phn,en))
        return render(request,"contact.html")
    return render(request,"contact.html")
def breeds(request):
    return render(request,"breeds.html")
def news(request):
    return render(request,"news.html")
def parameters(request):
    return render(request,"parameters.html")
def precautions(request):
    return render(request,"precautions.html")
def reviews(request):
    return render(request,"reviews.html")
def about(request):
    return render(request,"about.html")
