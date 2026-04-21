import sys

def cat(filename):
    try:
        with open(filename, "rb") as f:
            sys.stdout.buffer.write(f.read())
    except FileNotFoundError:
        sys.stderr.write(f"cat: {filename}: No such file or directory\n")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stdout.buffer.write(sys.stdin.buffer.read())
    else:
        for name in sys.argv[1:]:
            cat(name)
