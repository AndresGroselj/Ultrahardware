from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
#views
from contact import views as contact_views
from api_products import views as api_products_views
from . import views
#urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'productcard', api_products_views.ProductCardViewSet)

urlpatterns = [
    path('', views.Index, name="home"),
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('location/', views.Location, name="location"),
    path('cart/', include("cart.urls")),
    path('product/', include("products.urls")),
    path('contact/', contact_views.Contact, name="contact"),
    path('socialAccounts/', include("allauth.urls")),
    path('accounts/', include("accounts.urls")),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)