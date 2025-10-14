from rest_framework import generics
from .models import Contact, Tanlov, QA, ContactMessage, FAQ
from .serializers import ContactSerializer, TanlovSerializer, QASerializer, ContactMessageSerializer, FAQSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TanlovListView(generics.ListAPIView):
    queryset = Tanlov.objects.all()
    serializer_class = TanlovSerializer


class QAListView(generics.ListAPIView):
    queryset = QA.objects.all()
    serializer_class = QASerializer



class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


# Contact detail
class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Tanlov detail
class TanlovDetailView(generics.RetrieveAPIView):
    queryset = Tanlov.objects.all()
    serializer_class = TanlovSerializer


# QA detail
class QADetailView(generics.RetrieveAPIView):
    queryset = QA.objects.all()
    serializer_class = QASerializer


# ContactMessage detail
class ContactMessageDetailView(generics.RetrieveAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


# FAQ detail
class FAQDetailView(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
