from django.urls import path
from . import views
urlpatterns = [
    path("",views.homedisp,name='home'),
    path("adminlogin/",views.logindisp,name='login'),
    path("logout/",views.logoutdisp,name='logout'),
    path("datas/",views.datasdisp,name='datas'),
    path("datascustomers/",views.datasdispcustomers,name='datascustomers'),
    path("add/",views.adddisp,name='add'),
    path("update/<myid>",views.updatedisp,name='update'),
    path("delete/<myid2>",views.deletedisp,name='delete'),
    path("signup/",views.signupdisp,name='signup'),
    path("customerlogin/",views.customerlogindisp,name='customerlogin'),
    path("customerlogout/",views.customerlogoutdisp,name='customerlogout'),
    path("search/",views.searchdisp,name='search'),

]
