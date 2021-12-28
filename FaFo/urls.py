from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('news/', include('news.urls')),
    path('team/', include('team.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
