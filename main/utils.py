from django.conf import settings


static_path=settings.STATIC_URL


def seo(title=None, og_title=None, description=None, image_name=None, og_type=None):
    title = title or "Redo Developers Inc. WebApp"
    og_title = og_title or title
    description = description or "Redo Developers Inc. WebApp Description"
    image_url = f'{static_path}image/{image_name}' or "https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type = og_type or "website"

    context = {
        'title': title,
        'description': description,
        'og_title': og_title,
        'image': image_url,
        'og_type': og_type,
    }

    return context
