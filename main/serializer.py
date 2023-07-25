from rest_framework import serializers
from .models import *


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class WhyChooseOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseOption
        fields = "__all__"


class WhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = "__all__"


class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class TimeRemindSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeRemind
        fields = "__all__"


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"
