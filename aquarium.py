#!/usr/bin/env python3


class Aquarium:
    MIN_NUMBER = 20
    MAX_NUMBER = 100

    def __init__(self):
        # Как аквариум может знать хищная рыба это или нет? ето не его отвественность
        self.dwellers = []
