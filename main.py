from math import ceil, log2, pow


J = 2  # base, cannot be changed here


# estimate of the conditional pmf
def p(x, given):
    return (given.count(x) + 1) / (J + len(given))



def encode(u):
    if not u:
        return "empty string"
    lower_bound, interval_size = encode0([], u[0], u[1:], 0, 1)
    mid_point = lower_bound + interval_size/2
    L = ceil(-log2(interval_size))+1
    return ("{0:0" + str(L) + "b}").format(int(mid_point * pow(2, L)))


def encode0(encoded, x, to_encode, lower_bound, interval_size):
    next_interval_size = interval_size * p(x, encoded)
    next_lower_bound = lower_bound
    if x == '1':
        next_lower_bound = lower_bound + interval_size - next_interval_size
    # else it stays the same (only possible base is 2)

    # print("[" + str(lower_bound) + ", " + str(lower_bound + interval_size) + "] -> ["
    #       + str(next_lower_bound) + ", " + str(next_lower_bound + next_interval_size) + "]")

    if to_encode:
        return encode0(encoded + [x], to_encode[0], to_encode[1:], next_lower_bound, next_interval_size)
    else:
        return next_lower_bound, next_interval_size

print(encode("0001100010"))