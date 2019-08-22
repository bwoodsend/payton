"""Payton Lights.

Support for scene lights.
"""

import numpy as np  # type: ignore
from typing import Any, List, Optional


class Light(object):
    """Main Light object
    """

    def __init__(
        self,
        position: Optional[List[float]] = None,
        color: Optional[List[float]] = None,
        **args: Any,
    ):
        """Initialize Payton Light

        Args:
          position: Position of the light in global coordinates
          default position is [10, 7, 6]
          color: Color of the light source.
        """
        self._position: List[float] = [
            10.0,
            7.0,
            6.0,
        ] if position is None else position
        self._color: List[float] = [1.0, 1.0, 1.0] if color is None else color
        self._position_np: np.ndarray = np.array(
            self._position, dtype=np.float32
        )
        self._color_np: np.ndarray = np.array(self._color, dtype=np.float32)

        self.active: bool = True

    @property
    def position(self) -> List[float]:
        return self._position

    @position.setter
    def position(self, position: List[float]) -> None:
        self._position = position
        self._position_np = np.array(self.position, dtype=np.float32)

    @property
    def color(self) -> List[float]:
        return self._color

    @color.setter
    def color(self, color: List[float]) -> None:
        self._color = color
        self._color_np = np.array(self._color, dtype=np.float32)
