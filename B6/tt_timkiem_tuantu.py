# Thuật toán tìm kiếm tuần tự: làm việc với dữ liệu không được sắp xếp
# Độ phức tạp: O(n)

# ham tra ve index cua phan tu can tim 
def linear_search(arr, target) -> int:
    # duyet qua tung phan tu cua mang
    for index, value in enumerate(arr):
        # neu phan tu can tim co trong mang (dang tim kiem)
        if value == target:
            print(f"Phan tu {target} co trong mang")
            return index
    # neu phan tu can tim khong co trong mang
    print(f"Phan tu {target} khong co trong mang")
    print("Phan tu " + str(target) + " khong co trong mang")
    print("Phan tu" ,target, "khong co trong mang")
    return -1
        
        

print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100))