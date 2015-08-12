# -*- coding: utf-8 -*-

import numpy as np


def percentile_ranking(a, score):
    """
    The percentile rank of a score relative to a list of scores.
    A `percentile_ranking` of, for example, 80% means that 80% of the
    scores in `a` are below the given score.
    @param array a:
        Array of scores to which `score` is compared.
    @param float score:
        Score that is compared to the elements in `a`
    @Return float
        percentile_ranking of score (0.0~1.0) relative to `a`
    """
    a = np.array(a)
    n = len(a)
    if not np.any(a == score):
        a = np.append(a, score)
        a_len = np.array(list(range(len(a))))
    else:
        a_len = np.array(list(range(len(a)))) + 1.0
    a = np.sort(a)
    idx = [a == score]
    pct = np.mean(a_len[idx]) / n
    return 1.0 - pct