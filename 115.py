import numpy as np
def freq_of_chars(str) :

    n = len(str)

    freq = np.zeros(26, dtype = np.int)

    for i in range(0, n) :
        freq[ord(str[i]) – ord(‘a’)] += 1

    for i in range(0, n) :

        if (freq[ord(str[i])- ord(‘a’)] != 0) :

        print (str[i], freq[ord(str[i]) – ord(‘a’)],
        end = ” \n”)

    freq[ord(str[i]) – ord(‘a’)] = 0


str = input(“Enter the string : “)
freq_of_chars(str)
