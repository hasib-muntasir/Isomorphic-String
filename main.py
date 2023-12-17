def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    shash = {}
    thash = {}
    for letter in range(len(s)):
        if s[letter] not in shash:
            shash.update({s[letter]: t[letter]})
        else:
            if shash[s[letter]] != t[letter]:
                return False

        if t[letter] not in thash:
            thash.update({t[letter]: s[letter]})
        else:
            if thash[t[letter]] != s[letter]:
                return False
    return True

print(isIsomorphic(s="abcdf",t="pqrst"))