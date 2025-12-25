import requests


def check_backend_data(url, headers=None, timeout=10):
    response = requests.get(url, headers=headers, timeout=timeout)

    # 🔍 DEBUG INFO (keep this)
    print("BACKEND STATUS:", response.status_code)
    print("BACKEND HEADERS:", response.headers.get("Content-Type"))
    print("BACKEND BODY (first 200 chars):", response.text[:200])

    # ❌ If backend is not OK → FAIL GRACEFULLY
    if response.status_code != 200:
        return {
            "status": "ERROR",
            "reason": f"HTTP {response.status_code}",
            "raw": response.text
        }

    # ❌ If response is NOT JSON → FAIL GRACEFULLY
    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        return {
            "status": "ERROR",
            "reason": "Response is not JSON",
            "raw": response.text
        }

    try:
        return response.json()
    except ValueError:
        return {
            "status": "ERROR",
            "reason": "JSON parse failed",
            "raw": response.text
        }
