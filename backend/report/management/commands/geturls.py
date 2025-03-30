from django.core.management.base import BaseCommand
from django.urls import get_resolver
from django.conf import settings

import pprint
import csv
import os

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **kwargs):
        get_urls_namespace()



def get_urls_namespace():
    resolver = get_resolver()
    urls = []

    def extract_urls(patterns, namespace=None):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):  # Если это include
                ns = f"{namespace}:{pattern.namespace}" if namespace and pattern.namespace else pattern.namespace or namespace
                extract_urls(pattern.url_patterns, ns)
            elif hasattr(pattern, 'name'):
                full_name = f"{namespace}:{pattern.name}" if namespace else pattern.name
                urls.append({
                    'url': str(pattern.pattern),
                    'name': full_name,
                    'namespace': namespace,
                    'full_url': f'{namespace}/{str(pattern.pattern)}'
                })

    extract_urls(resolver.url_patterns)
    #pprint.pprint(urls)
    with open(os.path.join(settings.BASE_DIR, 'urls.csv'), mode='w') as file:
        fields = ['name', 'namespace', 'url', 'full_url']
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(urls)
