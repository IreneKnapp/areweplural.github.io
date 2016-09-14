# Generates favicon.svg

from functools import reduce
from fractions import Fraction
import operator
import fractions

STROKE_WIDTH_RATIO = Fraction(1, 40)
CIRCLE_RADIUS_RATIO = Fraction(3, 10)

# Ratios viewport will need to support.
# Viewport needs to be divisible by two.
# Stroke width needs to be divisible by two.
RATIOS = [Fraction(1, 2), STROKE_WIDTH_RATIO * Fraction(1, 2), CIRCLE_RADIUS_RATIO]
VIEWPORT = reduce(lambda s, r: s * r.denominator // fractions.gcd(s, r.denominator), RATIOS, 1)

STROKE_WIDTH = int(STROKE_WIDTH_RATIO * VIEWPORT)
CIRCLE_RADIUS = int(CIRCLE_RADIUS_RATIO * VIEWPORT)

print('<svg viewBox="0 0 {viewport_height} {viewport_width}" version="1.1" xmlns="http://www.w3.org/2000/svg">'.format(
    viewport_height=VIEWPORT,
    viewport_width=VIEWPORT))

def print_circle(cx, cy):
    print('<circle cx="{cx}" cy="{cy}" r="{r}" stroke="black" stroke-width="{stroke_width}" fill-opacity="0"/>'.format(
        cx=cx,
        cy=cy,
        r=CIRCLE_RADIUS,
        stroke_width=STROKE_WIDTH))

HALF = VIEWPORT // 2
CIRCLE_CENTER = (STROKE_WIDTH // 2) + CIRCLE_RADIUS
CIRCLE_CENTER_COMPLEMENT = VIEWPORT - CIRCLE_CENTER

# Top circle.
print_circle(cx=HALF, cy=CIRCLE_CENTER)

# Right circle.
print_circle(cx=CIRCLE_CENTER_COMPLEMENT, cy=HALF)

# Bottom circle.
print_circle(cx=HALF, cy=CIRCLE_CENTER_COMPLEMENT)

# Left circle.
print_circle(cx=CIRCLE_CENTER, cy=HALF)

print('</svg>')
