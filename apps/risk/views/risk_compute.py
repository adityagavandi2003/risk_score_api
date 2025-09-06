from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.risk.serializers import RiskInputSerializer
from apps.risk.services.risk_service import compute_risk

class RiskScoreView(APIView):
    def post(self, request):
        serializer = RiskInputSerializer(data=request.data)
        if serializer.is_valid():
            result = compute_risk(serializer.validated_data)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
