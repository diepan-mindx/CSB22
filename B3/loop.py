# vòng lặp hữu hạn (for) - lặp với số lần biết trước
name = "Diep"
for char in name: 
    # duyệt qua từng phần tử trong chuỗi
    print(char)
    
# range(stop): range(10) => 0->9
# range(start, stop): range(1, 5) => 1->4
# range(start, stop, step): range(1, 10, 2) => 1, 3, 5, 7, 9
for index in range(len(name)):
    # truy cập vào phần tử: <list>[index]
    print(index, name[index])
    
# vòng lặp vô hạn (while) - lặp với số lần không biết trước 
# condition: giá trị có thể trả về false => kết thúc vòng lặp
count = 0
while(count > 5):
    print(count)
    count+=1 # cộng dồn giá trị