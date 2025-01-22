from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from polls.views import createPost_view, createUser_view, loginUser_view, logoutUser_view, post_update, post_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_create/', createPost_view , name="post_create"),
    path('register/', createUser_view, name="create_user"),
    path('login/', loginUser_view, name="login_user"),
    path('logout/', logoutUser_view, name="logout_user"),
    path('post/<int:id>/update/', post_update, name='post_update'),
    path('post/<int:id>/delete/', post_delete, name='post_delete'),
    path('', include('polls.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)