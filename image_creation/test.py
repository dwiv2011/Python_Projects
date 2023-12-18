user={"name":"Joe","age":30,"access":"guest"}

def get_admin_password():
    return 1234

def secure_function(func):
    def make_secure():
        if user["access"]=="admin":
            return func()
        else:
            return "User does not have access"
    return make_secure


print(get_admin_password())

get_admin_password=secure_function(get_admin_password())

