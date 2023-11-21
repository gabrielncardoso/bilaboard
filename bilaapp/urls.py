from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

    path("signin/", views.signin, name="signin"),
    path("auth/", views.auth, name="auth"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup"),
    path("storesignup/", views.storesignup, name="storesignup"),
    
    path("dashboard/", views.dashboard, name="dashboard"),

    #group
    path("group/create/", views.creategroup, name="creategroup"),
    path("group/store/", views.storegroup, name="storegroup"),
    path("group/<int:group_id>/", views.groupdetail, name="groupdetail"),
    path("group/<int:group_id>/edit/", views.editgroup, name="editgroup"),
    path("group/<int:group_id>/update/", views.updategroup, name="updategroup"),
    path("group/<int:group_id>/destroy/", views.destroygroup, name="destroygroup"),
    path("group/<int:group_id>/addplayer/", views.addplayer, name="addplayer"),
    path("group/<int:group_id>/storeplayer/", views.storeplayer, name="storeplayer"),
    path("group/<int:group_id>/removeplayer/", views.removeplayer, name="removeplayer"),

    # match
    path("creatematch/", views.creatematch, name="creatematch"),
    path("storematch/", views.storematch, name="storematch"),
    path("match/<int:match_id>/editmatch/", views.editmatch, name="editmatch"),
    path("match/<int:match_id>/updatematch/", views.updatematch, name="updatematch"),
    path("match/<int:match_id>/destroymatch/", views.destroymatch, name="destroymatch"),

    #game
    path("game/<int:game_id>/", views.gamedetail, name="gamedetail"),

    #user
    path("userprofile/<int:user_id>/", views.userprofile, name="userprofie")
    
]
