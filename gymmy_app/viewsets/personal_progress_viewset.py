from rest_framework import viewsets
from rest_framework_extensions import mixins
from gymmy_app.models import PersonalProgress
from gymmy_app.serializers.personal_progress_serializer import PersonalProgressSerializer


class PersonalProgressViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = PersonalProgress.objects.all()
    serializer_class = PersonalProgressSerializer
