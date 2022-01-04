def primo(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

def run():
    for i in range(1,1001):
        if primo(i):
            print(i)

if __name__ == "__main__":
    run()