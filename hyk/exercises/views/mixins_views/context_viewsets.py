from hyk.users.models import Profile

class context_views():
    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'profile':Profile.objects.get(user=self.request.user),
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }