import requests

API_URL = "http://103.204.95.212:7001/api/facilityTrail/simulate-reallocation"

def run_simulation_backend(
    source_facility,
    destination_facility,
    part,
    quantity
):
    payload = {
        "part_id": part,
        "source_facility_id": source_facility,          # FULL VALUE
        "destination_facility_id": destination_facility,
        "quantity": str(quantity)                       # STRING
    }

    resp = requests.post(API_URL, json=payload, timeout=30)

    if resp.status_code != 200:
        raise Exception(
            f"Simulation API failed: {resp.status_code} | {resp.text}"
        )

    return resp.json()
