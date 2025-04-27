# Thuật toán nhị phân: dữ liệu bắt buộc phải được sắp xếp trước
# Độ phức tạp: O(log2(n))
# Cách thức hoạt động: chia mảng thành 2 phần, so sánh giá trị tại vị trí giữa với giá trị cần tìm

# ham binh thuong (vong lap)
def binary_search(arr, target):
    # khai bao bien dau va cuoi
    left = 0
    right = len(arr) - 1
    # khai bao bien mid (cot giua de so sanh)
    mid = 0
    # vong lap while
    while left <= right: # neu danh sach con phan tu de xet
        mid = (left + right) // 2 # lay cot giua
        # neu gia tri mid = target
        if arr[mid] == target:
            return mid
        # neu gia tri mid < target
        elif arr[mid] < target:
            left = mid + 1
        # neu gia tri mid > target
        else:
            right = mid - 1
    # neu khong tim thay
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # 4

# ----------------------------
# ham de quy
def binary_search_dequy(arr, target, left, right):
    # neu danh sach con phan tu de xet
    if left <= right:
        mid = (left + right) // 2
        # neu gia tri mid = target
        if arr[mid] == target:
            return mid
        # neu gia tri mid < target
        elif arr[mid] < target:
            return binary_search_dequy(arr, target, mid + 1, right)
        # neu gia tri mid > target
        else:
            return binary_search_dequy(arr, target, left, mid - 1)
    # neu khong tim thay
    return -1
    
print(binary_search_dequy(arr=[1, 2, 3, 4, 9, 10], target=5, left=0, right=9)) # -1