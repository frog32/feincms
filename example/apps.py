from django.apps import AppConfig


class ExampleAppConfig(AppConfig):
    name = 'example'
    verbose_name = "Example"

    def ready(self):
        from feincms.module.blog.models import Entry
        from feincms.module.page.models import Page
        from feincms.content.raw.models import RawContent
        from feincms.content.image.models import ImageContent
        from feincms.content.medialibrary.models import MediaFileContent
        from feincms.content.application.models import ApplicationContent

        from .models import get_admin_fields

        Page.create_content_type(RawContent)
        Page.create_content_type(
            MediaFileContent,
            TYPE_CHOICES=(
                ('default', 'Default position'),
            ),
        )
        Page.create_content_type(
            ImageContent,
            POSITION_CHOICES=(
                ('default', 'Default position'),
            ),
        )

        Page.create_content_type(ApplicationContent, APPLICATIONS=(
            ('blog_urls', 'Blog', {
                'admin_fields': get_admin_fields,
                'urls': 'example.blog_urls',
            }),
        ))

        Entry.register_regions(
            ('main', 'Main region'),
        )
        Entry.create_content_type(RawContent)
        Entry.create_content_type(
            ImageContent,
            POSITION_CHOICES=(
                ('default', 'Default position'),
            )
        )
