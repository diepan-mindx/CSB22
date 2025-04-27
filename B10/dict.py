# khai bao
dictionary = {
    "hello": "xin chao",
    "goodbye": ['bye', 'tam biet'],
}

cach_2 = dict(hello="xin chao")

# truy cap gia tri thuoc tinh
print(dictionary["hello"])
print(dictionary.get("goodbye"))

# them thuoc tinh
dictionary["hi"] = "chao ban"
print(dictionary)

# chinh sua gia tri thuoc tinh
dictionary["hi"] = "chao ban moi"
print(dictionary)

# xoa thuoc tinh
del dictionary["hi"]
# print(dictionary["hi"]) # KeyError: 'hi'