
from django.contrib import admin
from django.urls import path,include

import members

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('myapp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'))
]
