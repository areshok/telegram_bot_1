import qrcode
from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode.constants

from .models import Product

@receiver(post_save, sender=Product)
def generate_qr_code(sender, instance, created, **kwargs):
    if created:
        qr_code_data = 'test'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(qr_code_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', black_color='white')
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        filename = f'{instance.id}_{instance.name}_qrcode.png'
        file = InMemoryUploadedFile(
            buffer,
            None,
            filename,
            'image/png',
            buffer.getbuffer().nbytes,
            None,
        )
        instance.qrcode.save(filename, file, save=True)
