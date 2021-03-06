
# Applicatons main url configuration

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # where users register and login
    path('users/', include('users.urls')),

    # where company users can join a company or create a company
    path('company-users/', include('company_users.urls')),

    # where candidate users fill out their information after registering
    path('candidate-users/', include('candidate_users.urls')),

    # company users main dashboard
    path('company-account/', include('company_account.urls')),

    # candidate users main dashboard
    path('candidate-account/', include('candidate_account.urls')),

    # CRUD for job posts
    path('job-posts/', include('job_posts.urls')),

    # this app handles the logic for adding and finding skills
    path('skills/', include('skills.urls')),

    # candidate users can CRUD their past projects
    path('projects/', include('projects.urls')),

    # candidate users can CRUD their past experience
    path('experience/', include('experience.urls')),

    # this app handles the logic for job post matches
    path('matches/', include('matches.urls')),

    # text editor package
    path('tinymce/', include('tinymce.urls')),
]  

# configures path for static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# configures the path for where images will be updated to
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]





