#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    def fun_(kv): return (kv[1], kv[0])
    l_ = sorted(a_dictionary.items(), reverse=True, key=fun_)

    return (l_[0][1])
