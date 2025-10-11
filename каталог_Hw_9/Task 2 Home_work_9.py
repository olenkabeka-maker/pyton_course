import sys
print(sys.path)

sys.path.append("/шлях/до/моїх/модулів")      # нова папкау в списку шляхів

print(sys.path)

import sys
sys.path.append("/tmp/my_modules")   # додаємо новий каталог

import fibonacci
print(fibonacci)