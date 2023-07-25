from django.urls import path
from .views import *
urlpatterns = [
    path("get-silder/", get_silder_view),
    path("category/", Category_view),
    path("about/", About_view),
    path("info/", Info_view),
    path("why-choose/", WhyChoose_view),
    path("product/", Product_view),
    path("client-feedback/", Client_Feedback_view),
]


