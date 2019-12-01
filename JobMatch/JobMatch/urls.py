
# Applicatons main url configuration

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('company-users/', include('company_users.urls'))


] 

# configures the path for where images will be updated to
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




