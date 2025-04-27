# Bai1: kiem tra bieu thuc (phan mo - dong ngoac)
def is_valid_parentheses(f:list) -> bool:
    # tao danh sach da kiem tra
    clone = f
    # kiem tra: neu co dong ngoac => tim mo ngoac gan nhat => xoa cap ngoac
    if (len(clone) == 0):
        return True # xoa het ngoac 
    else:
        last = clone.pop()
        if (last in ['}', ')', ']']):
            # duyet danh sach => tim ngoac 
            for index, value in enumerate(clone):
                if last == '}' and value == '{':
                    clone.remove('{')
                elif last == ']' and value == '[':
                    clone.remove('[')
                elif last == ')' and value == '(':
                    clone.remove('(')                
        else:
            # truong hop mo ngoac nam sau dong ngoac
            return False
        # neu danh sach con phan tu => du 1 ngoac 
        return len(clone) == 0
print(is_valid_parentheses(['[','{', "}", ']', '(', ')'])) # false