from django import forms
from mainapp.models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = [
            'brand', 'price', 'processor', 'graphics_card', 'ram', 
            'storage', 'display', 'battery_life', 'operating_system', 
            'ports', 'wireless_connectivity', 'keyboard', 'touchpad', 
            'webcam', 'audio', 'build_material', 'weight', 'dimensions', 
            'cooling_system', 'security_features', 'optical_drive', 
            'color_options', 'warranty'
        ]
