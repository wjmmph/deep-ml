def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    lst = []
    result = []
    total = len(samples)
    for i in samples:
        if i not in lst:
            n = samples.count(i)
            tpl = (i, n/total)
            result.append(tpl)
            lst.append(i)
        else:
            pass
    
    return result