from rest_framework import pagination


class CustomPaginationClass(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'p'  # p dara ekhane page numberke bujhano hocche
    page_size_query_param = 'count'  # count dara ekhane per page a koyta item thakbe seta bujhacche
    max_page_size = 100
