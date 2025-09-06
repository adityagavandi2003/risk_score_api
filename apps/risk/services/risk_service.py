from apps.core.utils.logger import risk_logger

def compute_risk(data):
    risk_logger.info(f"Computing risk for data: {data}")
    risk_logger.debug(f"Input data details: {data}")

    score = 0
    breakdown = {}

    if data['region'].upper() == "EU" and data['data_sensitivity'].lower() == "high":
        score += 30
        breakdown['eu_high_sensitivity'] = 30
        risk_logger.debug("EU region with high sensitivity detected: +30")

    if data['processor_name'] == "UnknownVendor":
        score += 20
        breakdown['unknown_vendor'] = 20
        risk_logger.debug("Unknown vendor detected: +20")

    if data['purpose'].lower() == "marketing":
        score += 15
        breakdown['purpose_marketing'] = 15
        risk_logger.debug("Purpose is marketing: +15")

    result = {"risk_score": min(score, 100), "breakdown": breakdown}
    risk_logger.info(f"Computed risk result: {result}")
    risk_logger.debug(f"Risk computation complete: {result}")

    return result
