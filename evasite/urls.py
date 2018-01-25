"""evasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [

	path('', include('home.urls')),	
    path('cart/', include('cart.urls')),
	path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('orders/', include('orders.urls')),   
	path('tinymce/', include('tinymce.urls')),

	# Old url style
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # this works i think? new pathign is confusing at the moment
    re_path(r'media/(?P<path>.*)?$', serve, {'document_root': settings.MEDIA_ROOT}),
    
    path('admin/', admin.site.urls),

    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns