from dataclasses import dataclass, field
from functools import cache
from typing import Literal

from fastapi import APIRouter, Body

router = APIRouter(tags=["2023 - Day 13: Point of Incidence"])


DOCUMENT_EXAMPLE = []


@cache
def differences(first: str, second: str) -> int:
    diffs = 0

    for first_char, second_char in zip(first, second):
        if first_char != second_char:
            diffs += 1

    return diffs


@dataclass
class Grid:
    smudges: int
    rows: list[str] = field(default_factory=list)
    columns: list[str] = field(default_factory=list)

    def add(self, row: str) -> None:
        self.rows.append(row)

        if not self.columns:
            self.columns = ["" for _ in range(len(row))]

        for index, character in enumerate(row):
            self.columns[index] += character

    def calculate_reflections(self, direction: Literal["rows", "columns"]) -> int:
        data: list[str] | None = None
        multiplier = 1

        if direction == "rows":
            data = self.rows.copy()
            multiplier = 100

        if direction == "columns":
            data = self.columns.copy()

        assert data is not None

        start_indexes: list[int] = []

        for index in range(len(data) - 1):
            if differences(data[index], data[index + 1]) < 2:
                start_indexes.append(index)

        for start_index in start_indexes:
            smudges_used = 0

            reflection_index = start_index + 1
            matching = True
            end_index = start_index + 1

            while matching and start_index >= 0 and end_index < len(data):
                if data[start_index] == data[end_index]:
                    start_index -= 1
                    end_index += 1

                elif (
                    differences(data[start_index], data[end_index]) == 1
                    and self.smudges - smudges_used > 0
                ):
                    smudges_used += 1
                    start_index -= 1
                    end_index += 1

                else:
                    matching = False

            if matching and smudges_used == self.smudges:
                return reflection_index * multiplier

        return 0


@router.post("/part-1")
async def year_2023_day_13_part_1(
    document: list[str] = Body(
        ...,
        embed=True,
        examples=[DOCUMENT_EXAMPLE],
    ),
) -> int:
    total = 0

    grid = Grid(smudges=0)

    for line in document:
        if not line:
            # Calculate reflections
            if row_count := grid.calculate_reflections("rows"):
                total += row_count
            else:
                total += grid.calculate_reflections("columns")

            # Reset grid
            grid = Grid(smudges=0)

        else:
            grid.add(line)

    # Last grid
    if row_count := grid.calculate_reflections("rows"):
        total += row_count
    else:
        total += grid.calculate_reflections("columns")

    return total


@router.post("/part-2")
async def year_2023_day_13_part_2(
    document: list[str] = Body(
        ...,
        embed=True,
        examples=[DOCUMENT_EXAMPLE],
    ),
) -> int:
    total = 0

    grid = Grid(smudges=1)

    for line in document:
        if not line:
            # Calculate reflections
            if row_count := grid.calculate_reflections("rows"):
                total += row_count
            else:
                total += grid.calculate_reflections("columns")

            # Reset grid
            grid = Grid(smudges=1)

        else:
            grid.add(line)

    # Last grid
    if row_count := grid.calculate_reflections("rows"):
        total += row_count
    else:
        total += grid.calculate_reflections("columns")

    return total
