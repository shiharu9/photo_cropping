from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import os


def cropping(file_url):
    input_path = file_url[1:]
    output_path = input_path[:-3]
    fixed_width = 480

    img = Image.open(input_path)
    width_percent = (fixed_width / float(img.size[0]))
    height_size = int((float(img.size[1]) * float(width_percent)))
    new_image = img.resize((fixed_width, height_size))
    new_image.save(output_path+"png")

    f = np.fromfile(output_path+"png")
    result = remove(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path+"png")

    try:
        os.remove(input_path)
    except OSError as e:
        print("Error: %s : %s" % (input_path, e.strerror))


def home_page(request):

    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        cropping(file_url)

        return render(request, 'crop/page.html', {
            'file_url': file_url[:-3]+"png"
        })
    return render(request, 'crop/index.html')
