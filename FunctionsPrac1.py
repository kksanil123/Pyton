def sport(name, /, *props, **rules):
    print(f"sport is {name}")
    print(f"{name} properties-------------")
    for i in props:
        print(i)
    print(f"{name} rules *********")
    for i in rules:
        print(i, ":", rules[i])


sport("swimming", "Kicking", "Swimming", "Floating", a="don't panic", b="swim deep", c="don't stop breathing")
