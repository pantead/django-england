from django.conf.urls import url
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.views import LoginView, LogoutView, PasswordResetCompleteView, PasswordResetDoneView
from accounts import views




urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$', LoginView.as_view(template_name='accounts/loginview.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logoutview.html'), name='logout'), 
    url(r'^register/$',views.register, name ='register'),
    # url(r'^profile/$',views.view_profile, name ='view_profile'),
    # url(r'^profile/edit/$',views.edit_profile , name ='edit profile'),
    url(r'^change-password/$',views.change_password, name ='change_password')

    # url(r'^reset-password/$', PasswordResetForm, {'template_name':
    # 'accounts/reset_password.html', 'post_reset_redirect':
    # 'accounts: password_reset_done', 'email_template_name':
    # 'accounts/reset_password_email.html'},name ='reset_password'),


    # url(r'^reset-password/done/$', PasswordResetDoneView, {'template_name':
    # 'accounts/reset_password_done.html'},name ='reset_password_done'),

    # url(r'^reset-password/complete/$',PasswordResetCompleteView,{'template_name':
    # 'accounts/reset_password_complete.html'},name ='password_reset_complete')
  

    
]


