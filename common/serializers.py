from rest_framework import serializers


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None

        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class ConfigSerializer(serializers.Serializer):
    main_phone_number = serializers.CharField(max_length=20)
    main_email_address = serializers.CharField()
    main_banner_image = MediaURLSerializer()
    main_text = serializers.CharField()
    main_bottom_image = MediaURLSerializer()
    main_delivery_text = serializers.CharField()