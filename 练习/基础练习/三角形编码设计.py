a = int(input("请输入数字A："))
b = int(input("请输入数字B："))
c = int(input("请输入数字C："))

if a > 0 and b > 0 and c > 0 :
    if a + b > c or a + c > b or b + c > a :
        if a == b or b == c or a == c :
            if a == b == c :
                print("等边三角形")
            else:
                print("等腰三角形")
        else:
            print("普通三角形")
    else:
        print("不是三角形")
else:
    print("请输入合法的边长")
