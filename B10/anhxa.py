# Bai 1: doi GPA he 10/ 4
danh_sach_diem = [5.0, 6.5, 7.0, 8.0, 9.0, 10.0]
# def doi_gpa_he_10_4(danh_sach_diem):
#     for index in range(len(danh_sach_diem)):
#         # chuyen doi => gan lai gia tri moi cho phan tu
#         danh_sach_diem[index] = 4 * danh_sach_diem[index] / 10
#     return danh_sach_diem
# print(doi_gpa_he_10_4(danh_sach_diem))


# su dung map
def doi_gpa_he_10_4(diem):
    return 4 * diem / 10

danh_sach_diem_map = map(doi_gpa_he_10_4, danh_sach_diem)
print(list(danh_sach_diem_map))