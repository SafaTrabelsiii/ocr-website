#from django.urls import path 
#from .views import ocr

#urlpatterns = [
#    path('', ocr, name='ocr_view')
#]

from django.urls import path
from .views import ocr, download_text

urlpatterns = [
    path('', ocr, name='ocr_view'),  # OCR form and result page
    path('download/<str:filename>/<str:format>/', download_text, name='download_text'),  # Download links
]
