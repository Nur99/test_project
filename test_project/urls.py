"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

API_TITLE = 'API title'
API_DESCRIPTION = '...'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls')),
    url(r'^api/docs/', include_docs_urls(
        title='marketplace 1fit',
        authentication_classes=[],
        permission_classes=[]))]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)