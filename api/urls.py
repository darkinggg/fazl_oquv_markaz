from django.urls import path
from .views import ContactCreateView,TanlovListView, QAListView, ContactMessageCreateView, FAQListView,  ContactDetailView,\
TanlovDetailView,\
QADetailView,\
ContactMessageDetailView,\
FAQDetailView

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('tanlov/', TanlovListView.as_view(), name='tanlov'),
    path('qa/', QAListView.as_view(), name='qa'),
    path('contactmessage/', ContactMessageCreateView.as_view(), name='contact'),
    path('faq/', FAQListView.as_view(), name = 'faq'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('tanlov/<int:pk>/', TanlovDetailView.as_view(), name='tanlov-detail'),
    path('qa/<int:pk>/', QADetailView.as_view(), name='qa-detail'),
    path('contact-message/<int:pk>/', ContactMessageDetailView.as_view(), name='contact-message-detail'),
    path('faq/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]
