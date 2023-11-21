from inertia import share
from django.conf import settings
from utilities.get_routes import get_routes

def inertia_share(get_response):
  def middleware(request):
    share(request,
      app_url=settings.APP_URL,
      routes=get_routes(),
    )

    return get_response(request)
  return middleware