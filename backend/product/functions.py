import qrcode
from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings


def generate_qrcode(product):
    "Генерация qrcode"
    qr_code_data = f"{settings.T_BOT_URL}{product.id}"

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

    filename = f'{product.id}_{product.name}_qrcode.png'
    file = InMemoryUploadedFile(
            buffer,
            None,
            filename,
            'image/png',
            buffer.getbuffer().nbytes,
            None,
        )
    return filename, file
