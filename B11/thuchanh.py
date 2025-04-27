class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None
        
    # quay lai trang truoc do
    def back(self):
        # **: neu back rong => in: Khong co trang de quay ve => out ham

        # 1. them trang hien tai vao danh sach forward
        
        # 2. doi trang hien tai
        
        # 3. xoa trang hien tai trong danh sach back
        
    
    # di toi trang gan nhat
    def forward(self):
        pass
    
    # chuyen trang
    def visit_page(self, url):
        # 2. xoa forward
        
        # 3. them trang quay ve cho back  
    
        # 1. cap nhat gia tri current page
# ----------------------------
browser = Browser()

browser.visit_page("google.com")
browser.visit_page("facebook.com")
browser.visit_page("youtube.com")

browser.back()     # về facebook.com
browser.back()     # về google.com
browser.forward()  # tới facebook.com
browser.visit_page("wikipedia.org")  # forward_stack sẽ bị xoá
browser.forward()  # không đi tiếp được