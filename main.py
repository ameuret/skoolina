#!/usr/bin/env python
"""Skoolina - A screen cleaner game."""

from random import randint
import pyxel

class App:

    def __init__(self):
        self.palette = [0x000000, 0x1B2119, 0x232C21, 0x292C2D,
                        0x2E3044, 0x3A503C, 0x454758, 0x556F57,
                        0x626573, 0x67A9C2, 0x7AA07F, 0x85878B,
                        0xACAFAF, 0xCACDCD, 0xE6E8E7, 0xFFFFFF]

        self.titlePos = (32 + randint(0, 180), 32 + randint(0, 190))

        pyxel.init(320, 240, title="Skoolina", fps=60),
        pyxel.colors.from_list(self.palette)
        pyxel.image(1).load(0, 0, "3310-256.png")

        self.grime = pyxel.Image(320, 240)
        self.grime.rect(0, 0, 320, 240, 9)
        for i in range(64):
            self.grime.blt(randint(0, 320-32), randint(0, 240-32), 1, 160, 0, 64, 64, 9)

        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(5)
        pyxel.text(self.titlePos[0], self.titlePos[1], "SKOOLINA - A 46 lines game\n       by Arnaud", 7)
        pyxel.blt(0, 0, self.grime, 0, 0, 320, 240, 9)
        pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, 9)
        pyxel.blt(0, 0, 1, 0, 0, 160, 120, 10)
        pyxel.blt(160, 0, 1, 0, 0, -160, 120, 10)
        pyxel.blt(0, 120, 1, 0, 0, 160, -120, 10)
        pyxel.blt(160, 120, 1, 0, 0, -160, -120, 10)

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            for i in range(8):
                s = randint(1, 16)
                x = randint(0, 64-s)
                y = randint(0, 64-s)
                self.grime.blt(pyxel.mouse_x + x - 32, pyxel.mouse_y + y - 32, 1, 160 + x, 64 + y, s, s, 0)

App()
