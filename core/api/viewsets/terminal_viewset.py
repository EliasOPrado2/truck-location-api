import datetime
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from rest_framework import views
from core.models import Route
from rest_framework.response import Response
from core.api.serializers import TerminalSerializer


class TerminalViewSet(views.APIView):


    def get(self, request, format=None):

        data =  {}

        # add date format YYYY-MM-DD.
        trucks_per_day = request.query_params.get('trucks_per_day')

        # add date format YYYY-MM-DD.
        trucks_per_week = request.query_params.get('trucks_per_week')

        # add date format M
        trucks_per_month = request.query_params.get('trucks_per_month')

        if trucks_per_day:
            # add try/catch ValidationError.
            route_per_day = Route.objects.filter(created_at__date=trucks_per_day).count()
            data['route_per_day'] = route_per_day
            return Response(data)

        if trucks_per_week:
            formatted_date = trucks_per_week.split('-')
            year = int(formatted_date[0])
            month = int(formatted_date[1])
            day = int(formatted_date[2])

            # get the week number.
            week = datetime.date(year, month, day).isocalendar()[1]

            route_per_week = Route.objects.filter(created_at__week=week).count()

            data['route_per_week'] = route_per_week
            return Response(data)

        if trucks_per_month:
            print(trucks_per_month)
            route_per_month = Route.objects.filter(created_at__month=trucks_per_month).count()

            data['route_per_month'] = route_per_month
            return Response(data)

        
        print(trucks_per_day.split('-'))

        return Response({"Some data"})