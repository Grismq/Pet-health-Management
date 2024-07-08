from django.urls import path
from .import views 

urlpatterns=[ 
    path('',views.index,name='index'),
    path('register',views.register,name='reg'),
    path('login',views.login,name='log'),
    path('logout',views.logout,name='logout'),
    path('pethealth',views.pethealth,name='pethealth'),
    path('predict',views.predict,name='predict'),
    path('contact',views.contact,name='contact'),
    path('adoption',views.adoption,name='adoption'),
    path('breeds',views.breeds,name='breeds'),
    path('news',views.news,name='news'),
    path('parameters',views.parameters,name='parameters'),
    path('precautions',views.precautions,name='precautions'),
    path('reviews',views.reviews,name='reviews'),
    path('about',views.about,name='about'),
    
]