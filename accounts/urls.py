from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
#this is urls.py of accounts
urlpatterns = [
    path("register/",register, name="register"),
    path("login/",login_view, name="login"),
    path("logout/",logout_view, name="logout"),
    path("profile/",profile, name="profile"),
    path('deposit/',deposit, name='deposit'),
    path('borrow/<int:book_id>/',borrow_book, name='borrow_book'),
    path('return/<int:history_id>/',return_book, name='return_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
