def warehouse(*items, **info):
    print("Артикули:")
    for i, item in enumerate(items, 1):
        print(f'{i}. {item}')

    print("Информация:") 
    for key, value in info.items():
        print(f"{key}: {value}")

# Извикване на функцията
warehouse("ябълки", "круши", склад="софия", капацитет=500)
