class User:
    """foydalanuvchi haqida ma'lumotlarni tuzish"""
    def __init__(self, user, name, last_name, email, password):
        self.user = user
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
    def get_info(self):
        """foydalanuvchining ma'lumotlari"""
        return (f"foydalanuvchi: {self.user},\n"
                f" ismi {self.name} {self.last_name},\n"
                f" elektron pochtasi {self.email}, va paroli {self.password}")
qwe = User("alivaliyev530", "ali", "valiyev", "alivaliyev1@gmail.com", "qwerty123")
qwe1 = User("rajabboy1", "Rajabboy", "Adilbekov", "700_umidbekovich", "12345678")
print(qwe.get_info())
print(qwe1.get_info())