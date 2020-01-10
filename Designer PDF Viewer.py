#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    z=len(word)
    l=[]
    for i in range(97,123):
        l.append(chr(i))
    maxi=0
    for i in word:
        for j in range(26):
            if i==l[j]:
                if maxi<h[j]:
                    maxi=h[j]
    print(maxi*z)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designerPdfViewer(h, word)


