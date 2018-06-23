from django.conf.urls import url
from . import views

app_name= 'companies'

urlpatterns =[
    url(r'^login/$',views.login_view,name="login")
]
