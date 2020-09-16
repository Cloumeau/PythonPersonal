#python program that is able to reverse a string each word


class py_reverse:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_reverse().reverse_words('chris loumeau'))