from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now


class SetLastVisitMiddleware(MiddlewareMixin):
    @staticmethod
    def process_response(request, response):
        if request.user.is_authenticated:
            # Update last activity time after request finished processing.
            get_user_model().objects.filter(pk=request.user.pk).update(
                last_activity=now()
            )
        return response
