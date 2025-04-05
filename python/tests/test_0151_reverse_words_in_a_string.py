import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.string.0151_reverse_words_in_a_string")
Solution = module.Solution

def test():
    s = Solution()
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world!  ") == "world! hello"
    assert s.reverseWords("a good   example") == "example good a"
    assert s.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
