def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    pass


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


if __name__ == '__main__':
    string = read_file('emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)