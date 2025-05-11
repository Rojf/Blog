from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from src.interface.controllers.post import PostController


class PostViewSet(ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    viewset_factory = None

    @property
    def controller(self) -> PostController:
        return self.viewset_factory.create()

    def get(self, request: Request, post_id: int) -> Response:
        payload, status = self.controller.get(request, post_id)
        return Response(data=payload, status=status)

    def update(self, request: Request, post_id: int) -> Response:
        payload, status = self.controller.update(request, post_id)
        return Response(data=payload, status=status)

    def delete(self, request: Request, post_id: int) -> Response:
        payload, status = self.controller.delete(post_id)
        return Response(data=payload, status=status)


class PostListViewSet(ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    viewset_factory = None
    pagination_class = PageNumberPagination

    @property
    def controller(self) -> PostController:
        return self.viewset_factory.create()

    def list(self, request: Request) -> Response:
        payload, status = self.controller.list(request, self.pagination_class())
        return Response(data=payload, status=status)


class PostCreateViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> PostController:
        return self.viewset_factory.create()

    def create(self, request: Request) -> Response:
        payload, status = self.controller.create(request)
        return Response(data=payload, status=status)
