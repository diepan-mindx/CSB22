doanvan = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..', comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from 'de Finibus Bonorum et Malorum' by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."
# 1. xoa dau cau
doanvan = doanvan.replace(".", " ")
doanvan = doanvan.replace(",", " ")
doanvan = doanvan.replace(";", " ")
doanvan = doanvan.replace(":", " ")
doanvan = doanvan.replace("!", " ")
doanvan = doanvan.replace("?", " ")
doanvan = doanvan.replace("-", " ")
doanvan = doanvan.replace("'", " ")
doanvan = doanvan.replace('"', " ")
doanvan = doanvan.replace("(", " ")
doanvan = doanvan.replace(")", " ")
doanvan = doanvan.replace("[", " ")
doanvan = doanvan.replace("]", " ")
doanvan = doanvan.replace("{", " ")
doanvan = doanvan.replace("}", " ")

# 2. Cat tu cach nhau bang khoang trang => list
doanvan = doanvan.split()

# 3. chuyen het cac tu ve chu thuong
doanvan_set = map(str.lower, set(doanvan)) # set: bo cac tu trung lap

# 4. dem tan suat cac tu
# su dung dict de luu tan suat cac tu
tansuat = {}
for word in doanvan_set:
    tansuat[word] = doanvan.count(word) + 1
    # tansuat[word]: them key vao dict tansuat
    # doanvan.count(word): dem so lan xuat hien cua tu word trong doanvan

print(tansuat)