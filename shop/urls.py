from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('shopadmin/', include('adminapp.urls', namespace='shopadmin')),
    path('social/', include('social_django.urls', namespace='social')),
    path('order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
