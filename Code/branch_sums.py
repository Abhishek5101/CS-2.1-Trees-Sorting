# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums
	
def calculateBranchSums(node, runningSum, sums):
	if node is None:
		return
	
	runningSum += node.value
	if node.left is None and node.right is None:
		sums.append(runningSum)
		return
	
	calculateBranchSums(node.left, runningSum, sums)
	calculateBranchSums(node.right, runningSum, sums)


def is_palindrome(s):
	print(s[1:len(s)-1])
	return is_palindrome(s[1:len(s)-1])


# is_palindrome("nayan")

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

ispalindrome("nayan")