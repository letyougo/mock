"""hire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin,auth
from django.contrib.auth import urls as auth_urls

import mock.views as mock
urlpatterns = [
    url(r'^accounts/', include(auth_urls, namespace='accounts')),
    url(r'^admin/', admin.site.urls),


    url(r'^database/$', mock.database_list, name='database_list'),
    url(r'^database/(\d+)/$', mock.database_item, name='database_item'),

    url(r'^table/$', mock.table_list, name='table_list'),
    url(r'^table/(\d+)/$', mock.table_item, name='table_item'),
]
