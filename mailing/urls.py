from django.conf.urls import url
from mailing.views import UserList

urlpatterns = [
    
    url(r'^users/singup/$',UserList.as_view(), name="createuser"),
]