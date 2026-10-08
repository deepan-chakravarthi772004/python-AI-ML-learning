def login_check(func):
    def wrapper():
        print("Checking login....")
        func()
        print("done")
    return wrapper
@login_check
def dashboard():
    print("welcome to dashboard Deepan ishu's hubby")

dashboard()