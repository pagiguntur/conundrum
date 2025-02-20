class Solution(object):
    def checkTree(self, root):
	# assumsion jika root dikurangi kiri dan kanan tidak nol maka False
	# more simple return root.val == root.left.val + root.right.val
        return 0 == root.val - root.left.val - root.right.val