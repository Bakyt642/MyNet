"""NetShoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar

from blog import views
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views
# from ckeditor_uploader import views
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
]

urlpatterns += i18n_patterns  (
    path('admin/', admin.site.urls),
    path('', include('blog.urls',)),
    path('account/', include('account.urls')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    # url(r'^upload/', login_required(views.upload), name='ckeditor_upload'),
    # url(r'^browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
    url(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
    # url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    # path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    # url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
)
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
