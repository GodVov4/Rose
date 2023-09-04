def config(extent: float, cycles=2000) -> tuple:
    return extent, cycles


CONSTANTS = {
    'star': lambda: config(30),
    'lotus': lambda: config(40),
    'some flower': lambda: config(70),
    'propeller': lambda: config(81),
    'web': lambda: config(140),
    'hurt-flower': lambda: config(200),
    'clover': lambda: config(200, 14),
}


# star - extent = 30, cycles = 2000
# lotus - extent = 40, cycles = 2000
# some flower - extent = 70, cycles = 2000
# propeller - extent = 81, cycles = 2000
# web - extent = 140, cycles = 2000
# hurt-flower - extent = 200, cycles = 2000
# clover - extent = 200, cycles = 14
