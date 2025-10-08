from screeninfo import get_monitors

for m in get_monitors():
    print(f"Monitor: {m.name}, {m.width}x{m.height}, at ({m.x}, {m.y})")
