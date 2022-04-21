#!/usr/bin/env python3
import typing
import copy

from ..state import State


class MinimaxTreeNode:
    def __init__(self, state: State, maxing: bool, parent=None, depth=0, action: str = None,
                 alpha: float = float('-inf'), beta: float = float('inf')):
        self.state: State = state
        self.maxing: bool = maxing
        self.action: str = action
        self.depth: int = depth
        self.value: float = float('-inf') if maxing else float('inf')
        self.alpha: float = alpha
        self.beta: float = beta

        self.is_leaf: bool = state.is_terminal()
        self.parent: MinimaxTreeNode = parent
        self.untried: typing.List[str] = state.legal_moves
        self.pruned: typing.List[str] = []
        self.children: typing.Dict[str, MinimaxTreeNode] = {}

        if self.is_leaf:
            self.value = state.score()
            self.backpropagate()

    @property
    def fully_expanded(self):
        return len(self.untried) == 0

    def backpropagate(self):
        if self.parent is None:
            return
        if self.parent.maxing:
            self.parent.value = max(self.parent.value, self.value)
            self.parent.backpropagate()
        else:
            self.parent.value = min(self.parent.value, self.value)
            self.parent.backpropagate()

    def expand(self):
        while not self.fully_expanded:
            action = self.untried.pop(0)
            temp = copy.deepcopy(self.state)
            temp.move(action)
            self.children[action] = MinimaxTreeNode(
                state=temp,
                maxing=not self.maxing,
                parent=self,
                depth=self.depth + 1,
                action=action,
                alpha=self.alpha,
                beta=self.beta,
            )
            self.children[action].expand()
            del temp

    @property
    def best_child(self):
        for _, child in self.children.items():
            if child.value == self.value:
                return child
        return None

    @property
    def best_action(self):
        return self.best_child.action
