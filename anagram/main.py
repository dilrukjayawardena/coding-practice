s = 'eet'
t = 'tte'

#Bf solution
def anagram_bf(s,t):
    if len(s) != len(t):
        return False
    for ch in s:
        if ch not in t or s.count(ch) != t.count(ch):
            return False
    return True

print(anagram_bf(s,t))

#optimal solution

def anamgram_opti(s,t):
    if sorted(s)==sorted(t):
        return True
    return False

print(anamgram_opti(s,t))

# if character in s adds 1 if same avail in t removes one
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26  # assuming lowercase letters only
    for ch1, ch2 in zip(s, t):
        # ord(ch) get the unicode point starts with 97 upto 122 so ord('a')=97
        count[ord(ch1) - ord('a')] += 1
        count[ord(ch2) - ord('a')] -= 1
    return all(c == 0 for c in count)


    