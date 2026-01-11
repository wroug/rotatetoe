def drawboard(height, width, data, compact=False):
    #nonlocal row, col
    if compact:
        board = []

        tmp = "╔═"
        for i in range(width - 1):  # top border
            tmp += "╤═"
        tmp += "╗"
        board.append(tmp)

        for i in range(height):
            tmp = f"┊{data[i][0]}"
            for j in range(width - 1):
                tmp += f"│{data[i][j+1]}"
            tmp += "┊"
            board.append(tmp)

            tmp = "╟─"
            for j in range(width - 1):  # top border
                tmp += "┼─"
            tmp += "╢"
            board.append(tmp)

        board.pop()

        tmp = "╚═"
        for i in range(width - 1):  # top border
            tmp += "╧═"
        tmp += "╝"
        board.append(tmp)

        return board

    elif not compact:
        board = []

        tmp = "╔═══"
        for i in range(width - 1):  # top border
            tmp += "╤═══"
        tmp += "╗"
        board.append(tmp)

        for i in range(height):
            tmp = f"┊ {data[i][0]}"
            for j in range(width - 1):
                tmp += f" │  {data[i][j + 1]}"
            tmp += " ┊"
            board.append(tmp)

            tmp = "╟───"
            for j in range(width - 1):  # top border
                tmp += "┼───"
            tmp += "╢"
            board.append(tmp)

        board.pop()

        tmp = "╚═══"
        for i in range(width - 1):  # top border
            tmp += "╧═══"
        tmp += "╝"
        board.append(tmp)

        return board


