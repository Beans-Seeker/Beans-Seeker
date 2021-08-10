from django.contrib import admin
from django.urls import path, include
from beans.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('cafes/', cafes, name="cafes"),
    path('account/', include('accounts.urls')),
    path('profile/', profile, name="profile"),

]


# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path, include
# from account.views import register_view
# from webstagram.views import feed

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', register_view, name="first"),
#     path('feed/', feed, name="feed"),
#     path('account/', include('account.urls')),
#     path('webstagram/', include('webstagram.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
