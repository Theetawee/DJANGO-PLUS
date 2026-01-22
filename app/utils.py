from typing import Any, Tuple

from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_page_number(),
                "previous": self.get_previous_page_number(),
                "count": self.page.paginator.count,
                "results": data,
            }
        )

    def get_next_page_number(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_page_number(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()


class APIPaginatedView(APIView):
    pagination_class = CustomPageNumberPagination

    def paginate_queryset(
        self, queryset: Any, request: Request
    ) -> Tuple[Any, PageNumberPagination]:
        """
        Paginate a queryset using the specified pagination class.

        Args:
            queryset (Any): The queryset or list of objects to paginate.
            request (Request): The HTTP request object.

        Returns:
            Tuple[Any, PageNumberPagination]: A tuple containing the paginated page and the paginator instance.
        """
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        return page, paginator
