"""Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('api/films/',views.ManageFilm.as_view(),name='films'),
    # path('api/category/',views.ManageCategory.as_view(),name='catgs'),
    path('api/catg/',views.categoy,name='catg'),
    path('f/<int:videoid>/',views.watch_video,name='watch_film'),
    # path('test/',views.test,name='test'),
    path('films/catg/',views.get_film_by_catg,name='gbc'),
    path('static/',serve,{'document_root': settings.STATIC_ROOT})

]


handler404 = 'app.views.Pagehandler404'


# urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
