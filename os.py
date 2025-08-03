import os 
def find(path, dir):
    for item in os.listdir(path): 
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            if item == dir:
                print(os.path.abspath(full_path))
            find(full_path,dir)

find(r"C:\Users\E550\OneDrive\Desktop", "python")
