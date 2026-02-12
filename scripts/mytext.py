import asyncio

from electrolux_group_developer_sdk.auth.token_manager import (
    TokenManager,  # type: ignore[import-untyped]
)
from electrolux_group_developer_sdk.client.appliance_client import (
    ApplianceClient,  # type: ignore[import-untyped]
)

async def main():
    access_token = "eyJraWQiOiIxMGZhMWQwOWY4YjM2OGFjYmE4YmRiNDYxOTFmZmVhODE1MmZiM2YzZjQ5N2RhZjk1OWFjNWIzNDM5ZDI3OGY0IiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJpYXQiOjE3NzA4MTQzODksImlzcyI6Imh0dHBzOi8vYXBpLm9jcC5lbGVjdHJvbHV4Lm9uZS9vbmUtYWNjb3VudC1hdXRob3JpemF0aW9uIiwiYXVkIjpbImVsZWN0cm9sdXhfb2NwIiwiaHR0cHM6Ly9hcGkub2NwLmVsZWN0cm9sdXgub25lIl0sImV4cCI6MTc3MDg1NzU4OSwic3ViIjoiNDRiOTFjZWRmNGY4NGNiOTlhMTQxYjM0ZTIyNzBiYjUiLCJhenAiOiJIZWlPcGVuQXBpIiwic2NvcGUiOiJlbWFpbCBvZmZsaW5lX2FjY2VzcyIsIm9jYyI6IkJSIn0.EmdkWQ4LKDUNN4PaAVQG0vURLhd6PdR8Afa5SObyOJ0usN_dyghSyPUMDCOV9IDjR3EGX7przOI7uPpq-eK3p8BhsV60etzOEc29UC1tsVXSuSnEOr4T6Ui5CAIoeY3jFdYIWQkKmxOBWUEzKZ4e1DgHADwaacOaaxRiZ8s-AWT2--LQqkS_FbdazaseL5UYKg73J5OO-_tt2uhZDA5eYDGgNZtC7vVDtVRylefPb6yE2QipTuF1jm_V5luzdAOp7rPrS2HRLdnEJZ-AMUuEVuMAx-hCsle2uBZua5A0IjRUtME9lFHN13hj-oultTFob-rO0WG13G_6VeWuoS8zcA"
    refresh_token = "lS4fKn7U7SMxm4crXqt7aMuhwxj40Fzg0IKBQ56MXzc9ydGCMR2fT1Scuaw8032BkHmQWs1T6eKaG8cxxtCOmFKVboEyNmBKSJYSMNsFq99CMvBjbBRvv8kp3LQ5F68m"
    api_key = "a_b722225a-f720-4e53-a947-26abb2024851"
    _token_manager = TokenManager(access_token, refresh_token, api_key)
    _client = ApplianceClient(_token_manager)
    appliances = await _client.get_appliances()
    for appliance in appliances:
        print(appliances)

asyncio.run(main())
