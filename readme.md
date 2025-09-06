# RiskScore API

A Django REST API to compute risk scores based on input data. This project is ready for local development and testing, and can be extended for cloud deployment using Docker, Celery, and Redis.

## Features

- Compute risk scores based on rules:
    - **EU + High sensitivity:** +30
    - **Unknown Vendor:** +20
    - **Marketing purpose:** +15
- Logging enabled for risk computation and API activity
- Ready for Docker, Celery, and Redis for async tasks

## Technology Stack

- Python 3.11
- Django 5.x
- Django REST Framework
- SQLite (default, lightweight DB for local dev)
- Logging: `logs/risk_score.log` & `logs/django.log`

## Code Repository

- [GitHub Repository](https://github.com/adityagavandi2003/risk_score_api)  

- [Download ZIP](https://github.com/adityagavandi2003/risk_score_api/archive/refs/heads/main.zip)

## Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd VERICYAI-GOA

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

API available at: [http://127.0.0.1:8000/api/v1/risk-score/](http://127.0.0.1:8000/api/v1/risk-score/)

## Design Decisions

- **Modular Django app:** Clean separation of API logic, risk computation, and logging.
- **Extensible risk rules:** Rules are defined in code for easy modification.
- **API key authentication:** Basic security for API endpoints.
- **Logging:** Detailed logs for both risk computation and Django activity.

## Example Risk Inputs & Outputs

| Example | Input | Output |
|---------|-------|--------|
| **1 – Very High Risk** | <pre>{ "region":"EU", "data_sensitivity":"high", "processor_name":"UnknownVendor", "purpose":"marketing" }</pre> | <pre>{"risk_score":65,"breakdown":{"eu_high_sensitivity":30,"unknown_vendor":20,"purpose_marketing":15}}</pre> |
| **2 – High Sensitivity in EU** | <pre>{ "region":"EU", "data_sensitivity":"high", "processor_name":"TrustedVendor", "purpose":"operations" }</pre> | <pre>{"risk_score":30,"breakdown":{"eu_high_sensitivity":30}}</pre> |
| **3 – Marketing Only** | <pre>{ "region":"Asia", "data_sensitivity":"low", "processor_name":"SafeVendor", "purpose":"marketing" }</pre> | <pre>{"risk_score":15,"breakdown":{"purpose_marketing":15}}</pre> |
| **4 – Unknown Vendor Only** | <pre>{ "region":"US", "data_sensitivity":"medium", "processor_name":"UnknownVendor", "purpose":"analytics" }</pre> | <pre>{"risk_score":20,"breakdown":{"unknown_vendor":20}}</pre> |
| **5 – No Risk** | <pre>{ "region":"India", "data_sensitivity":"low", "processor_name":"TrustedVendor", "purpose":"hr" }</pre> | <pre>{"risk_score":0,"breakdown":{}}</pre> |

## Example API Requests/Responses

**Request:**
```http
POST /api/v1/risk-score/
Content-Type: application/json
x-api-key: secreat123

{
    "region": "EU",
    "data_sensitivity": "high",
    "processor_name": "UnknownVendor",
    "purpose": "marketing"
}
```

**Response:**
```json
{
    "risk_score": 65,
    "breakdown": {
        "eu_high_sensitivity": 30,
        "unknown_vendor": 20,
        "purpose_marketing": 15
    }
}
```

## Testing API with cURL

```bash
curl -X POST http://127.0.0.1:8000/api/v1/risk-score/ \
-H "Content-Type: application/json" \
-H "x-api-key: secreat123" \
-d '{"region":"EU","data_sensitivity":"high","processor_name":"UnknownVendor","purpose":"marketing"}'
```

## Testing API with Postman

1. Open Postman and create a new `POST` request.
2. Set the request URL to: `http://127.0.0.1:8000/api/v1/risk-score/`
3. In the **Headers** tab, add:
    - `Content-Type: application/json`
    - `x-api-key: secreat123`
4. In the **Body** tab, select `raw` and choose `JSON`, then enter:
    ```json
    {
      "region": "EU",
      "data_sensitivity": "high",
      "processor_name": "UnknownVendor",
      "purpose": "marketing"
    }
    ```
5. Click **Send** to view the response.

## Logging

- Risk logs: `logs/risk_score.log`
- Django logs: `logs/django.log`
- Logs INFO and DEBUG for detailed tracking.

## Ready for Deployment (Optional)

This project can be extended for cloud deployment using:

- **Docker:** Containerize Django + SQLite/Postgres.
- **Celery + Redis:** Handle async risk computation tasks.
- **Nginx + Gunicorn:** Serve Django efficiently in production.

Once Docker, Redis, and Celery are added, the project will support background task processing and scalable deployment.

## Feedback & Queries

If you have any feedback or suggestions to improve the RiskScore API, or if you have any queries regarding setup, usage, or extending the project, please feel free to open an issue or contact the maintainers.

We welcome contributions and questions!


## Walkthrough Video (Optional)

- [Loom Walkthrough](https://youtu.be/YHXppnD8AhU)  
