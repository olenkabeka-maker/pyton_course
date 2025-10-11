# читає вміст файлу myfile.txt та відтворює його

with open("myfile.txt", "r") as f:          # r - режим читання
    content = f.read()
    print(content)