# Kiem tra danh sach co phan tu lap 
def kiemtra_lap(danhsach):
    # loc qua tung phan tu
    for i in range(len(danhsach)- 1):
        # tao them vong lap con de kiem tra phan tu lap
        for j in range (i + 1, len(danhsach)):
            # kiem tra gia tri thu i va thu j
            if danhsach[i] == danhsach[j]:
                return True
    return False

print(kiemtra_lap([1, 2, 3, 4, 5, 10])) # False
print(kiemtra_lap([1, 2, 3, 9, 10, 1])) # True
