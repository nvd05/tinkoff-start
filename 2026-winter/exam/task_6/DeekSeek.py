'''
Не верный результат, но близко.
'''


class PersistentNode:
	__slots__ = ('left', 'right', 'size', 'value')

	def __init__(self, value=None, left=None, right=None):
		self.left = left
		self.right = right
		self.size = 0
		self.value = value

		if left is not None:
			self.size += left.size
		if right is not None:
			self.size += right.size
		if value is not None:
			self.size = 1

def build_tree(arr, l, r):
	if l == r:
		return PersistentNode(value=arr[l])

	mid = (l + r) // 2
	left = build_tree(arr, l, mid)
	right = build_tree(arr, mid + 1, r)
	return PersistentNode(left=left, right=right)

def get_char(node, index):
	if node.value is not None:
		return node.value
	
	if node.left is not None and index < node.left.size:
		return get_char(node.left, index)
	else:
		return get_char(node.right, index - (node.left.size if node.left else 0))

def concatenate(left, right):
	if left is None:
		return right
	if right is None:
		return left
	return PersistentNode(left=left, right=right)

def copy_subtree(node, l, r, start, end):
	'''Копирует поддерево с индексами [l, r] в исходной строке'''
	if start > end or node is None:
		return None
	
	if start == l and end == r:
		return node
	
	if node.value is not None:
		if start <= l <= r <= end:
			return PersistentNode(value=node.value)
		return None
	
	left_size = node.left.size if node.left else 0
	res_left = None
	res_right = None
	
	if start < left_size:
		left_end = min(end, left_size - 1)
		res_left = copy_subtree(node.left, l, min(r, left_size - 1), start, left_end)
	
	if end >= left_size:
		right_start = max(start - left_size, 0)
		right_end = end - left_size
		res_right = copy_subtree(node.right, max(l - left_size, 0), r - left_size, 
								right_start, right_end)
	
	return concatenate(res_left, res_right)

def task_6(n, q, s, arr):
	# Инициализируем корень дерева
	root = build_tree(list(s), 0, n - 1)
	result = []
	
	for query in arr:
		if query['action'] == 1:
			l, r = query['l'], query['r']
			# Копируем подстроку [l-1, r-1] (индексация с 0)
			copied = copy_subtree(root, 0, n - 1, l - 1, r - 1)
			# Разделяем дерево на три части: до l-1, [l-1, r-1], после r-1
			left_part = copy_subtree(root, 0, n - 1, 0, l - 2) if l > 1 else None
			middle_part = copy_subtree(root, 0, n - 1, l - 1, r - 1)
			right_part = copy_subtree(root, 0, n - 1, r, n - 1) if r < n else None
			
			# Склеиваем: left + middle + copied + right
			root = concatenate(concatenate(left_part, middle_part), 
							  concatenate(copied, right_part))
			n += (r - l + 1)
		else:
			i = query['i']
			result.append(get_char(root, i - 1))
	
	return '\n'.join(result)

if __name__ == '__main__':
	n, q = [int(value) for value in input().strip().split()]
	s = input().strip()

	arr = []
	for _ in range(q):
		line = input().strip().split()

		if line[0] == '1':
			arr.append({
				'action': 1,
				'l': int(line[1]),
				'r': int(line[2])
			})

		if line[0] == '2':
			arr.append({
				'action': 2,
				'i': int(line[1])
			})

	res = task_6(n, q, s, arr)
	print(res)
