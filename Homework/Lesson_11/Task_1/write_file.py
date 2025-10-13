#cтворюю файл myfile.txt

with open("myfile.txt", "w") as f:     # w - режим запису
    f.write("Hello file world!\n")     #запускає текст "Hello file world! у новому файлі  myfile.txt