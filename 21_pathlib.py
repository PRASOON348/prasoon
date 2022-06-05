from pathlib import Path

path = Path("projects")
print(path.exists()) #it prints if path projects exist in ths PC then it return TRUE otherwise FALSE


path = Path("projects")
print(path.exists())

print("**********************")

path = Path()        #Here this program prints all directories or folders in this PC
for path in path.glob("*"):
    print(path)