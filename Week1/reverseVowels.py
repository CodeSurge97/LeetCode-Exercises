def reverseVowels(self, s: str) -> str:
        VOWELS = set('aeiouAEIOU')
        string = list(s)
        vowels = []
        indexes = []
        for index, letter in enumerate(string):
            if letter in VOWELS:
                vowels.append(letter)
                indexes.append(index)
        for i, char in zip(indexes, reversed(vowels)):
            string[i] = char

        return ''.join(string)