from django.conf.urls import url

from django.contrib.auth import views as auth_views

from .import views




urlpatterns=[
    
    url(r'^$',views.login,name='login'),
    url(r'login',views.login,name='login'),
    url(r'forgotpassword',views.forgotpassword,name='forgotpassword'),

   

    url(r'Logout', views.Logout, name='Logout'),
    
    url(r'data',views.data,name='data'),
    
    url(r'AllPatient',views.AllPatient,name='AllPatient'),


    url(r'NewPatient',views.NewPatient,name='NewPatient'),

    url(r'Old_Patient/(?P<id>[0-9]+)',views.Old_Patient,name='Old_Patient'),

    url(r'Old_Patient2',views.Old_Patient2,name='Old_Patient2'),  

    
    url(r'OldPatient',views.OldPatient,name='OldPatient'),

    
    url(r'InsertRow',views.InsertRow,name='InsertRow'),

   

    

    url(r'edit/(?P<id>[0-9]+)',views.edit_patient,name='edit_patient'),

    url(r'update/(?P<id>[0-9]+)',views.update,name='update'),

    url(r'delete/(?P<id>[0-9]+)',views.delete_patient,name='delete_patient'),
    

    url(r'All_detail/(?P<id>[0-9]+)',views.All_detail,name='All_detail'),


    url(r'newform',views.newform,name='newform'),

    
    


    url(r'editnew/(?P<id>[0-9]+)',views.edit_patient,name='edit_patient'),

    url(r'PrintAny',views.PrintAny,name='PrintAny'),



    url(r'Print_for_all/(?P<id>[0-9]+)',views.Print_for_all,name='Print_for_all'),


    # for Old patients CRUD

    url(r'edit_oldpatient/(?P<id>[0-9]+)',views.edit_oldpatient,name='edit_oldpatient'),
    url(r'update_old/(?P<id>[0-9]+)',views.update_old,name='update_old'),
    

    url(r'All_detail',views.All_detail,name='All_detail'),

    url(r'All_detail2/(?P<id>[0-9]+)',views.All_detail2,name='All_detail2'),

    url(r'Print_for_all_2/(?P<id>[0-9]+)',views.Print_for_all_2,name='Print_for_all_2'),

    # for password reset through email


    # url('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),

    # url('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    # url('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    # url('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),




    



]


