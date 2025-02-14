result = []
def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("I located... ZeroDivisionError!")
        return 0
    except ValueError:
        print("I located... ValueError!")
        return 0
    except TypeError:
        print("I located... TypeError!")
        return 0



data = {10: 2, 2: 5, "123": 4, 18: 0,8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)
print(result)