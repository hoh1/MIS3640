
def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        
        for word in line.split():
            word = word.lower() #make the word lowercase

            #update the histogram
            hist[word] = hist.get(word, 0) + 1
                    
    return hist

print(process_file('test_file.txt', skip_header=False))