#!/usr/bin/env python3
import typing


class State:

    """
    you may need to create different states for different colors
    """

    def __init__(self) -> None:
        pass

    @property
    def legal_moves(self) -> typing.List[str]:
        pass

    def move(self, action: str):
        pass

    def is_terminal(self) -> bool:
        pass

    def score(self) -> float:
        pass
