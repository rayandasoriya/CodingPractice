from collections import defaultdict
def word_break(s, wordDict):
    n = len(s)
    memo = defaultdict(list)
    def word_helper(start):
        if start == n:
            return [[""]]
        if start in memo:
            print(start, memo)
            return memo[start]
        result = []
        for i in range(start, len(s)):
            curr_word = s[start:i+1]
            print(curr_word)
            if curr_word in wordDict:
                list_of_words = word_helper(i+1)
                #print(curr_word, list_of_words)
                result+=[[curr_word]+w for w in list_of_words]
        memo[start].extend(result)
        return result

    words = word_helper(0)
    word = [" ".join(word).strip() for word in words]
    return word

print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))