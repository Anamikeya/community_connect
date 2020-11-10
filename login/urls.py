from django.urls import path
from . import views
urlpatterns = [
    path("",views.start,name = "start"),
    path("register",views.register,name = "register"),
    path("login",views.login,name = "login"),
    path("post",views.post,name = "post"),
    path("logout",views.logout,name="logout"),
    path("public",views.public,name="public"),
    path("topics",views.topics,name="topics"),
    path("childMarriage",views.childMarriage,name="childMarriage"),
    path("DesparityinEducation",views.DesparityinEducation,name="DesparityinEducation"),
    path("DomesticVoilence",views.DomesticVoilence,name="DomesticVoilence"),
    path("DowryandBride",views.DowryandBride,name="DowryandBride"),
    path("FemaleInfanticide",views.FemaleInfanticide,name="FemaleInfanticide"),
    path("Inferiority",views.Inferiority,name="Inferiority"),
    path("LowStatusInFamily",views.LowStatusInFamily,name="LowStatusInFamily"),
    path("SexualHarrasment",views.SexualHarrasment,name="SexualHarrasment"),
    path("StatusOfWidow",views.StatusOfWidow,name="StatusOfWidow"),
    path("InadequateNutrition",views.InadequateNutrition,name="InadequateNutrition"),

]
