# STACK: Last in (phai) First out (trai) (LIFO)
# khai bao stack

# peek: lấy phần tử cuối cùng trong danh sách (KHÔNG XÓA)

# push: thêm phần tử vào cuối (đỉnh stack) - O(1)

# pop

# kiểm tra rỗng
def is_empty(stack):
# cach 1: 
#  return len(stack) == 0

# cach 2: 
#   if len(stack) == 0:
#       return True
#   return False

# cach 3: 
  return True if len(stack) == 0 else False
