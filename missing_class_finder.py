import os

# Extract known classes from the directory
known_classes = os.listdir(r'C:\Users\armaa\OneDrive\Desktop\VLG recruitment\Data\train')
known_classes = [entry.replace('+', '') for entry in known_classes]
print("Known Classes: \n")
print(known_classes)



print("\n\n")
# Extract unknown classes from the txt file
all_classes = []

with open(r'C:\Users\armaa\OneDrive\Desktop\VLG recruitment\Data\classes.txt') as file_name:
    for line in file_name:
        word = ''.join([i for i in line if i.isalpha()])
        if word:
            all_classes.append(word)

print("All Classes: \n")
print(all_classes)
file_name.close()



missing_classes = []
condition = 1
for tester in all_classes:
    condition = 1
    for classes in known_classes:
        
        if classes == tester:
            condition = 0
            break
        
    if condition:
        missing_classes.append(tester)
        
   
        
        
print("Unknown Classes:")
print(missing_classes)

with open(r'C:\Users\armaa\OneDrive\Desktop\VLG recruitment\missingclasses.txt', 'w') as file:
    for classes in missing_classes:
        print(classes)
        file.write(classes + '\n')
        
        
file.close()
print("file exported successfully")