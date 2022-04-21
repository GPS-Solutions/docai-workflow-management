"""
  UJ10 - E2E tests for checking
  HITL endpoint for Pending documents table
"""

import requests
from endpoint_proxy import get_baseurl


def test_pending_queue():
  base_url = get_baseurl("hitl-service")
  status="pending"
  res = requests.post(base_url + f"/hitl_service/v1/get_queue?"\
    f"hitl_status={status}")
  assert res.status_code == 200
