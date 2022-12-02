class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def display(self):
    # lines, +_ = display_aux(self)
    lines, *_ = self.display_aux()
    for line in lines:
        print(line)


def display_aux(self):
    if self.right is None and self.left is None:
        line = '%s' % self.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], widht, height, middle
# Only left child
    if self.right is None:
        lines, width, height, middle = self.left.display_aux()
        self_value = '%s' % self.value
        len_self_value = len(self_value)
        first_line = (middle + 1) * ' ' + \
            (width - middle - 1) * '_' + self_value
        second_line = middle * ' ' + '/' + \
            (width - middle - 1 + len_self_value) * ' '
        shifted_lines = [line + len_self_value * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, width + len_self_value, height + 2, width + len_self_value // 2
# Only right child
    if self.left is None:
        lines, width, height, middle = self.right.display_aux()
        self_value = '%s' % self.value
        len_self_value = len(self_value)
        first_line = self_value + middle + 1 * '_' + (width - middle) * ' '
        second_line = (len_self_value + middle) * '_' + \
            '\\' + (width - middle - 1) * ' '
        shifted_lines = [line + self_value * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, width + len_self_value, height + 2, len_self_value // 2


# Two Children
left, left_width, left_height, left_middle = self.left.display_aux()
rigth, right_width, right_height, right_middle = self.right.display_aux()
self_value = '%s' % self.value
len_self_value = len(self_value)
first_line = (left_middle + 1) * ' ' + (
        left_width - left_middle - 1) * '_' + self_value + right_middle * '_' + (
                 right_width - right_middle) * ' '

second_line = left_middle * ' ' + '/' + (
         left_width - left_middle- 1 + len_self_value + right_middle * '' + '\\' + (
                   right_width - right_middle) - 1) * ' '

if left_height < right_height:
    left += [left_width * ' '] * (rigth_height - left_height)
elif right_height < left_height:
    right += [right_width * ' '] + (left_height - right_height)
zipped_lines = zip(left, rigth)
lines = [first_line, second_line] + [a + len_self_value * ' ' + b for a, b in zipped_lines]
return lines, left_width + right_width + len_self_value, max(left_height,
                                                             right_height) + 2, left_width + len_self_value // 2

def create_minimal_bst(arr, start, end):
    if start > end:
        return None

    mid=(start + end) // 2
    new_node=Node(arr[mid])
    new_node.left=create_minimal_bst(arr, start, mid - 1)
    new_node.right=create_minimal_bst(arr, mid + 1, end)
    return new_node


def create_minimal_bst(arr):
    return create_minimal_bst(arr, 0, len(arr) - 1)


if name == '_main_':
    root = create_minimal_bst[1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10]
    root.display()

    # def insert(self, data):
    #     if self.value == data:
    #         return False
    #     elif self.value > data:
    #         if self.left:
    #             return self.left.insert(data)
    #         else:
    #             self.left = Node(data)
    #             return True
    #     else:
    #         if self.right:
    #             return self.right.insert(data)
    #         else:
    #             self.right = Node(data)
    #             return True

    # def find(self, data):
    #     if self.value == data:
    #         return True
    #     elif self.value > data:
    #         if self.left:
    #             return self.left.find(data)
    #         else:
    #             return False
    #     else:
    #         if self.right:
    #             return self.right.find(data)
    #         else:
    #             return False

    # def preorder(self):
    #     if self:
    #         print(str(self.value))
    #         if self.left:
    #             self.left.preorder()
    #         if self.right:
    #             self.right.preorder()

    # def postorder(self):
    #     if self:
    #         if self.left:
    #             self.left.postorder()
    #         if self.right:
    #             self.right.postorder()
    #         print(str(self.value))

    # def inorder(self):
    #     if self:
    #         if self.left:
    #             self.left.inorder()
    #         print(str(self.value))
    #         if self.right:
    #             self.right.inorder()

    #     def insert(self, data):
    #         if self.value == data:
    #             return False
    #         elif self.value > data:
    #             if self.left:
    #                 return self.left.insert(data)
    #             else:
    #                 self.left = Node(data)
    #                 return True
    #         else:
    #             if self.right:
    #                 return self.right.insert(data)
    #             else:
    #                 self.right = Node(data)
    #                 return True

    #     def find(self, data):
    #         if self.value == data:
    #             return True
    #         elif self.value > data:
    #             if self.left:
    #                 return self.left.find(data)
    #             else:
    #                 return False
    #         else:
    #             if self.right:
    #                 return self.right.find(data)
    #             else:
    #                 return False

    #     def preorder(self):
    #         if self:
    #             print(str(self.value))
    #             if self.left:
    #                 self.left.preorder()
    #             if self.right:
    #                 self.right.preorder()

    #     def postorder(self):
    #         if self:
    #             if self.left:
    #                 self.left.postorder()
    #             if self.right:
    #                 self.right.postorder()
    #             print(str(self.value))

    #     def inorder(self):
    #         if self:
    #             if self.left:
    #                 self.left.inorder()
    #             print(str(self.value))
    #             if self.right:
    #                 self.right.inorder()
