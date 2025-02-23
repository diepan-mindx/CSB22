import random
# tạo file
with open('./B4/students_score.txt', 'w') as file:
    file.write('Hello \n') # ghi lai file

# ghi danh sách điểm vào file
for i in range(5):
    # ghi tiep cho file
    with open('./B4/students_score.txt', 'a') as file:
        grade = random.randint(0, 10)
        file.write(str(grade) + '\n')
        
# đọc file (đọc 1 dòng)
with open('./B4/students_score.txt', 'r') as file:
    print(file.readline())

# đọc file (đọc hết file)
with open('./B4/students_score.txt', 'r') as file:
    print(file.read()) # return a string
    
# đọc file (đọc hết file cách 2)
with open('./B4/students_score.txt', 'r') as file:
    print(file.readlines()) # return an array (mỗi hàng là 1 phần tử)