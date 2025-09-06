from django.urls import path
from .views import RiskScoreView

urlpatterns = [
    path('v1/risk-score', RiskScoreView.as_view(),name="risk_score"),
]
