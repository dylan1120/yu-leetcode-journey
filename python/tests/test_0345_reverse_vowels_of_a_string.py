import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.string.0345_reverse_vowels_of_a_string")
Solution = module.Solution

def test():
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels("aA") == "Aa"
    assert s.reverseVowels(" ") == " "
    assert s.reverseVowels(".,") == ".,"
    assert s.reverseVowels("aeiou") == "uoiea"
    assert s.reverseVowels("AEIOU") == "UOIEA"
    assert s.reverseVowels("12345") == "12345"
    assert s.reverseVowels("hello world") == "hollo werld"
    assert s.reverseVowels("h@ll0") == "h@ll0"
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
