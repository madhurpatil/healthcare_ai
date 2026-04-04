from db import get_all_records

def generate_analytics():
    records = get_all_records()

    total_cases = len(records)
    emergency_cases = sum(1 for r in records if r["emergency"])

    keyword_count = {}

    for r in records:
        for alert in r["alerts"]:
            keyword_count[alert] = keyword_count.get(alert, 0) + 1

    return {
        "total_cases": total_cases,
        "emergency_cases": emergency_cases,
        "keyword_stats": keyword_count
    }