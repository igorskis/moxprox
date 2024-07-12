from rest_framework.viewsets import ReadOnlyModelViewSet

from vm.models import VM
from vm.serializer import VMSerializer


class VMView(ReadOnlyModelViewSet):
    queryset = VM.objects.all()
    serializer_class = VMSerializer