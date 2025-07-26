from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            my_qr = qrcode.make(url)
            print(my_qr)
            file_name = res_name.replace(" ","_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT , file_name)
            
            my_qr.save(file_path)

            img_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'name':res_name,
                'image_url':img_url,
                'file_name':file_name
            }
            return render(request, 'result.html',context)

    else:
        form = QRCodeForm()
        context = {
            'form':form
        }
        return render(request,'gen.html',context)
    return render(request,'gen.html')
