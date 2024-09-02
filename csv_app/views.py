import csv
import io

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Visiter
from .serializers import EmployeeSerializer, VisitorSerializer
from .task import parse_csv


class UploadCSVView(APIView):

    def post(self, request):

        csv_file = request.FILES.get('file')
        num = request.query_params.get('num')
        print(num)
        if num :
            parse_csv.delay(int(num))
        if not csv_file.name.endswith('.csv'):
            return Response({"error": "Invalid file format. Please upload a CSV file."}, status=status.HTTP_400_BAD_REQUEST)

        file_data = csv_file.read().decode('utf-8')
        csv_reader = csv.DictReader(io.StringIO(file_data))

        for row in csv_reader:
            name = row.get("name")
            email = row.get("email")
            role = row.get("role")

            if role == "visitor":
                data = {"name": name, "email": email, "role": role}
                serializer = VisitorSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

            if role == "employee":
                data = {"name": name, "email": email, "role": role}
                serializer = EmployeeSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

        return Response(
            {"message": "Users value added based on the fields in csv file"},
            status=status.HTTP_200_OK,
        )

    def get(self, request):

        queryset_v = Visiter.objects.all()
        queryset_e = Employee.objects.all()
        serializer_v = VisitorSerializer(queryset_v, many=True)
        serializer_e = EmployeeSerializer(queryset_e, many=True)

        return Response(
            {"employees": serializer_e.data, "visitors": serializer_v.data},
            status=status.HTTP_200_OK,
        )
    
    def delete(self, request) :

        queryset_v = Visiter.objects.all()
        queryset_e = Employee.objects.all()
        queryset_e.delete()
        queryset_v.delete()

        return Response({
            'message' : "All users deleted successfully"
        })
