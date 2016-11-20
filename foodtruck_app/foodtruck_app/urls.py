"""foodtruck_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cart_data.views import MainPageView, cart_db_data_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPageView.as_view()),
    #url(r'^cart_db_data/(?P<lat>)/(?P<lng>)', cart_db_data_view, name='cart_db_data'),
    url(r'^cart_db_data/', cart_db_data_view, name='cart_db_data')
]
