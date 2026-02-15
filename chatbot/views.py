from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


from chatbot.models import Book, BookChunk
from chatbot.serializers import BookSimpleSerializer, BookChunkSimpleSerializer
from drf_spectacular.utils import extend_schema


def home(request):
    return HttpResponse("Hello, Chat!")


class BookViewSet(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer

    @extend_schema(
        description='Retrieve all chunks belonging to a specific book.'
    )

    @action(detail=True, methods=['get'])
    def chunks(self, request, pk=None):
        book = self.get_object()
        chunks = BookChunk.objects.filter(book=book)
        serializer = BookChunkSimpleSerializer(chunks, many=True)
        return Response(serializer.data)