
# sequence: a sorted or unsorted list of doubles or integers
# Output: an increasing subsequence that is of longest possible length
def longestIncreasingSubsequence(sequence):
    subsequenceLengths = [1]*len(sequence)
    for i in range(len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                subsequenceLengths[i] = max(subsequenceLengths[i], 1+subsequenceLengths[j])
    maximum = max(subsequenceLengths)
    subsequence = []
    for i in range(len(subsequenceLengths)-1, -1, -1):
        if subsequenceLengths[i] == maximum:
            subsequence.append(sequence[i])
            maximum -= 1
    subsequence.reverse()
    return subsequence


# sequence: a sorted or unsorted list of doubles or integers
# Output: an increasing subsequence that is of longest possible length
# runtime is O(n*log(n)), using binary search
def longest_increasing_subsequence(sequence):
    sequenceLength = len(sequence)
    P = [0]*sequenceLength
    M = [0]*(sequenceLength+1)
    L = 0
    for i in range(sequenceLength):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (sequence[M[mid]] < sequence[i]):
               lo = mid+1
           else:
               hi = mid-1
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
       if newL > L:
           L = newL
    subsequence = []
    k = M[L]
    for i in range(L-1, -1, -1):
        subsequence.append(sequence[k])
        k = P[k]
    return subsequence[::-1]