# -*- coding: utf-8 -*-


class ImageSerializerMixin:

    def build_absolute_image_url(self, url):
        if not url.startswith('http'):
            request = self.context.get('request')
            return request.build_absolute_uri(url)
        return url
