from dataclasses import dataclass

import numpy as np
from fastapi import APIRouter, Body

router = APIRouter(tags=["2023 - Day 18: Title"])


DOCUMENT_EXAMPLE = []


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


OFFSET: dict[str, tuple[int, int]] = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


@dataclass
class BigGrid:
    current: Coordinate
    path: list[Coordinate]

    perimiter: int = 0

    @property
    def enclosed_area(self) -> int:
        x_coordinates = [position.x for position in self.path[:-1]]
        y_coordinates = [position.y for position in self.path[:-1]]

        # Calculates the area within
        area = abs(np.trapz(y_coordinates, x=x_coordinates))

        return area + self.perimiter + 1

    def move(self, x: int, y: int) -> None:
        # One of these is always zero, just add both
        self.perimiter += (abs(x) + abs(y)) / 2

        self.current = Coordinate(
            x=self.current.x + x,
            y=self.current.y + y,
        )
        self.path.append(self.current)


@router.post("/part-1")
async def year_2023_day_18_part_1(
    document: list[str] = Body(
        ...,
        embed=True,
        examples=[DOCUMENT_EXAMPLE],
    ),
) -> int:
    grid = BigGrid(
        current=Coordinate(x=0, y=0),
        path=[Coordinate(x=0, y=0)],
    )

    for line in document:
        direction, distance, _ = line.split(" ")

        x_offset, y_offset = OFFSET[direction]
        grid.move(x_offset * int(distance), y_offset * int(distance))

    return grid.enclosed_area


@router.post("/part-2")
async def year_2023_day_18_part_2(
    document: list[str] = Body(
        ...,
        embed=True,
        examples=[DOCUMENT_EXAMPLE],
    ),
) -> int:
    grid = BigGrid(
        current=Coordinate(x=0, y=0),
        path=[Coordinate(x=0, y=0)],
    )

    direction_map: dict[str, str] = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U",
    }

    for line in document:
        _, __, color = line.split(" ")

        # Convert from hex to decimal
        distance = int(color[2:7], 16)
        direction = direction_map[color[7]]

        x_offset, y_offset = OFFSET[direction]
        grid.move(x_offset * distance, y_offset * distance)

    return grid.enclosed_area
