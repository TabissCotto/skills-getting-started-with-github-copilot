import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def activities_snapshot():
    snapshot = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(snapshot)
