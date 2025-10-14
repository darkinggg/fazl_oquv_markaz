from rest_framework import serializers
from .models import Contact, Tanlov, QA, ContactMessage, FAQ

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
class TanlovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlov
        fields = '__all__'


class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
