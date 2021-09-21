from django.contrib import admin
from django.urls import path, include
from apps.common.views import HomeView, SignUpView  # , DashboardView#, TablesView
from django.contrib.auth import views as auth_views

from apps.userprofile.views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='common/home.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),
         name='logout'),
    path('dashboard/', include('apps.dashboard.urls')),
    path('clients/', include('apps.contacts.urls')),
    path('companies/', include('apps.companies.urls')),
    path('projects/', include('apps.projects.urls')),
    #path('calendar/', include('apps.calendars.urls')),
    # path('tables/', TablesView.as_view(), name='tables'),
    path('change-password', auth_views.PasswordChangeView.as_view(
        template_name='common/change-password.html',
        success_url='/'), name='change-password'),
    path('profile/', ProfileView.as_view(
        template_name='common/profile.html',
        ), name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(
        template_name='common/profile-update.html',
        ), name='profile-update'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
