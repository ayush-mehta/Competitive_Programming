def designerPdfViewer(h, word):
    ascii = list()
    out = list()
    for char in word:
        num = int(ord(char)) - 97
        out.append(h[num])
    out = int(max(out))*len(word)
    print(out)

h = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
h = h.split()
word = 'abc'
designerPdfViewer(h, word)