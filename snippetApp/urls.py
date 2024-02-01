from django.contrib import admin
from django.urls import path
from snippetApp import views


urlpatterns = [
    path('',views.add_codeSnippet,name="add_codeSnippet"),
    path('add_codeSnippet/',views.add_codeSnippet,name="add_codeSnippet"),
    path('readFull/<id>',views.readFull,name="readFull"),
    path('delete_codeSnippet/<id>/',views.delete_codeSnippet,name="delete_codeSnippet"),
    path('update_codeSnippet/<id>/',views.update_codeSnippet,name="update_codeSnippet"),
    path('login/',views.login_page,name="login_page"),
    path('logout/',views.logout_page,name="logout_page"),
    path('myProfile/',views.myProfile,name="myProfile"),
    path('register/',views.register_page,name="register_page"),
    path('aboutUs/',views.aboutUs,name="aboutUs"),
    path('terms/',views.terms,name="terms"),
    path('contactUs/',views.contactUs,name="contactUs"),

]
