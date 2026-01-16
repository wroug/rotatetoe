from opensimplex import OpenSimplex


def generatenoise(w, h, scale=20, seed=0, octaves=1):
    shades = [' ', '░', '▒', '▓', '█']
    gen = OpenSimplex(seed)

    def octave_noise(xx, yy):
        value = 0
        amp = 1
        freq = 1
        norm = 0
        for _ in range(octaves):
            value += gen.noise2(xx * freq, yy * freq) * amp
            norm += amp
            amp *= 0.5
            freq *= 2
        return value / norm

    rows = []
    for y in range(h):
        row = ''
        for x in range(w):
            n = octave_noise(x / scale, y / scale)
            n = ((n + 1) / 2) ** 1.3
            idx = min(4, int(n * 5))
            row += shades[idx]
        rows.append(row)
    return rows

