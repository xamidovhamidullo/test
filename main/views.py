from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import *
from .models import *
from .serializer import *
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny



@api_view(['GET'])
def get_Information_view(request):
    info = Information.objects.last()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request):
        return Response(InformationSerializer(self.info).data)


@api_view(['GET'])
def get_silder_view(request):
    slider = Slider.objects.all()
    query = SliderSerializer(slider).data
    return Response(query)


@api_view(['GET'])
def Category_view(request):
    category = Category.objects.all()
    query = CategorySerializer(category, many=True).data
    return Response(query)


@api_view(['GET'])
def About_view(request):
    about = About.objects.last()
    query = AboutSerializer(about).data
    return Response(query)


@api_view(['GET'])
def Info_view(request):
    info = Info.objects.all()
    query = InfoSerializer(info, many=True).data
    return Response(query)


@api_view(['GET'])
def WhyChoose_view(request):
    why_choose = WhyChoose.objects.all()
    query = WhyChooseSerializer(why_choose, many=True)
    return Response(query)


@api_view(['GET'])
def Product_view(request):
    product = Product.objects.all()
    query = ProductSerializer(product, many=True).data
    return Response(query)


@api_view(['GET'])
def Client_Feedback_view(request):
    client_feedback = ClientFeedback.objects.all()
    query = ClientFeedbackSerializer(client_feedback, many=True).data
    return Response(query)

