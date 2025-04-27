import csv

company_count = dict()
email_list = set()
# mo file bang with open
with open('./lab10/data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        name = row[0]
        company = row[1]
        email = row[2]
        
        # email khong trung lap => them vao danh sach
        if email not in email_list:
            email_list.add(email)
            # dem so luong nguoi trong cong ty
            if company not in company_count:
                # chua co cong ty trong danh sach
                company_count[company] = 1
            else:
                # da co ten cong ty => cong don 
                company_count[company] += 1            
        
# Output: danh sach cong ty: so luong nguoi (dict)
print(f"So luong dai bieu: {len(email_list)}")
for company, count in company_count.items():
    print(f"{company}: {count}")