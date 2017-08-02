
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    elif n == 0:
        return str[1:len(str)]
    elif n == len(str) - 1:
        return str[:len(str) - 1]
    else:
        pre = str[:n]
        post = str[n+1: len(str)]
        return pre + post
