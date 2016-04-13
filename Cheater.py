def suffixArray(s):
    """ Given T return suffix array SA(T).  We use Python's sorted
    function here for simplicity, but we can do better. """
    # Empty suffix '' plays role of $.
    satups = sorted([(s[i:], i) for i in xrange(0, len(s)+1)])
    # Extract and return just the offsets
    return map(lambda x: x[1], satups)

print suffixArray("ACGGTGCTTATGCT")
