import time


def make_readable(seconds):
    time.gmtime(seconds)
    print(f"{time.struct_time[3]}:{time.struct_time[4]}:{time.struct_time[5]}")


make_readable(60)
make_readable(86399)
