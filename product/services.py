import os

from django.conf import settings
from PIL import Image

from product.models import Product


def get_list_product():
    return Product.objects.all()


def get_image_path(path):
    return path.split('.')[0]


def convert_image(image_name):
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    image_type = image_name.split('.')[-1]
    if image_type.upper() == 'PNG' or 'JPG':
        img = Image.open(image_path)
        img.convert('RGB')
        new_img_name = image_name.split('.')[0]
        new_img_path = os.path.join(settings.MEDIA_ROOT, new_img_name)
        img.save(f'{new_img_path}.webp', 'webp')


def get_list_format_for_image(image_name):
    format_images = []
    name_image = image_name.split('/')[-1].split('.')[0]
    path_directory = os.path.join(settings.MEDIA_ROOT, 'images') 
    for _,_, filenames in os.walk(path_directory):
        for filename in filenames:
            if (filename.startswith(name_image)):
                image_format = filename.split('.')[-1]
                format_images.append(image_format)
    return format_images
