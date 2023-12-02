from pathlib import Path

import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "filename,total",
    [
        ("part-1.txt", 24000),
        ("input.txt", 67450),
    ],
)
def test_part_1(filename: str, total: int, test_client: TestClient) -> None:
    with open(Path(__file__).with_name(filename), "rb") as file:
        response = test_client.post(
            "2022/day-1/part-1",
            files={"document": file},
        )

        assert response.status_code == 200
        assert response.json() == total


@pytest.mark.parametrize(
    "filename,total",
    [
        ("part-2.txt", 45000),
        ("input.txt", 199357),
    ],
)
def test_part_2(filename: str, total: int, test_client: TestClient) -> None:
    with open(Path(__file__).with_name(filename), "rb") as file:
        response = test_client.post(
            "2022/day-1/part-2",
            files={"document": file},
        )

        assert response.status_code == 200
        assert response.json() == total