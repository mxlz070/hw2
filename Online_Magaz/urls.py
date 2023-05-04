
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from Online_Magaz import settings
from products.views import products_view, main_view, product_detail_view,product_create_view
from users.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_view),
    path('', main_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', product_create_view),
    path('users/', include('users.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
