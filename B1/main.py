# Input/ output --------------------------------
# input: là hàm có trả về kiểu dữ liệu string
# age = input("How old are you? ")
# print(type(age))  # str

# print(params): in ra man hinh du lieu ghi trong (...)
# print("Hello", "world", 3, 14.2, True)


# variable --------------------------------
# constant (hằng số)
PI = 3.14
print(PI)

# variable (biến số)
# 1. không có kí tự đặc biệt
# a* = 1
# 2. không có khoảng trắng
# your name = "John"
# 3. không có số ở đầu tên biến
# 1cau = 10
# 4. không đặt biến trùng keyword của ngôn ngữ
# try = 1

# style đặt tên
# 1. camel case
yourFullName = "Au Ngoc Diep"
# 2. snake case
your_full_name = "Au Ngoc Diep"

# Data type ------------------------------------
# type(): trả về kiểu dữ liệu của biến
print(type("hello")) # str

# string (str) kiểu dữ liệu chuỗi (dựa vào bảng ASCII)
# chuỗi có thể được viết bằng dấu ' ' hoặc " "
name = "Au Ngoc Diep"

# integer (int) kiểu dữ liệu số nguyên
age = 20

# float kiểu dữ liệu số thực
weight = 45.9

# boolean kiểu dữ liệu logic
is_admin = True

# Type casting -------------------------------------
# 1. int() 
# string -> int
# str = int("12.5") # lỗi
# float -> int
fl = int(12.5) # 12 - làm tròn xuống - chỉ lấy phần nguyên
# boolean -> int
is_admin = int(True) # 1 - True

# 2. float()
# string -> float
str = float("123.5") # 123.5
# int -> float
int = float(123) # 123.0
# boolean -> float
bool = float(True) # 1.0

# 3. boolean()
# string -> boolean

# int -> boolean

# float -> boolean


