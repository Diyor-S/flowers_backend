from django.db import models
from .utils import validate_phone_number
# Create your models here.

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")

    file = models.FileField(upload_to='media/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'webp', 'mpeg'])])

    file_type = models.CharField(max_length=10, verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        # E:\Azamat Python\1 month\1 lesson\main.py
        element = r"""[\]"""
        return f'Id: {self.id}|Name: {self.file.name.split(element)[-1]}'

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'mpeg']:
                raise ValidationError(_("Invalid Video File"))


class CommonSettings(models.Model):
    main_phone_number = models.CharField(max_length=20,
                                         verbose_name=_("Main Phone Number"), validators=[validate_phone_number])
    main_email_address = models.EmailField(verbose_name=_("Main Phone Address"))
    main_banner_image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("Main Banner Image"),
                                          related_name="main_banner_image")
    main_text = models.TextField(verbose_name=_("main text"))
    main_bottom_image = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("Main Bottom Image"),
                                          related_name="main_bottom_image")
    main_delivery_text = models.TextField(verbose_name=_("main delivery text"))

    def __str__(self):
        return self.main_phone_number

    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")
