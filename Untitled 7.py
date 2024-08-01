
import matplotlib.pyplot as plt
import os
import cv2
import pandas as pd



glioma="dataset/Training/glioma/"
image_files = os.listdir(glioma)

plt.figure(figsize=(10, 10))

for i in range(25):
    img_path = os.path.join(glioma, image_files[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(5, 5, i + 1)
    plt.imshow(img)
    plt.axis('off')

plt.suptitle('Sample Glioma Images', fontsize=16)
plt.tight_layout()
plt.show()


meningioma_dir="dataset/Training/meningioma/"
image_files = os.listdir(meningioma_dir)

plt.figure(figsize=(10, 10))

for i in range(25):
    img_path = os.path.join(meningioma_dir, image_files[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(5, 5, i + 1)
    plt.imshow(img)
    plt.axis('off')

plt.suptitle('Sample Meningioma Images', fontsize=16)
plt.tight_layout()
plt.show()





notumor_dir="dataset/Training/notumor/"
image_files = os.listdir(notumor_dir)

plt.figure(figsize=(10, 10))

for i in range(25):
    img_path = os.path.join(notumor_dir, image_files[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(5, 5, i + 1)
    plt.imshow(img)
    plt.axis('off')

plt.suptitle('Sample Images without Tumor', fontsize=16)
plt.tight_layout()
plt.show()





pituitary_dir="dataset/Training/pituitary/"
image_files = os.listdir(pituitary_dir)

plt.figure(figsize=(10, 10))

for i in range(25):
    img_path = os.path.join(pituitary_dir, image_files[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.subplot(5, 5, i + 1)
    plt.imshow(img)
    plt.axis('off')

plt.suptitle('Sample Pituitary Tumor Images', fontsize=16)
plt.tight_layout()
plt.show()


train_data="dataset/Training"
test_data="dataset/Testing"
valid_data="dataset/Testing"


filepath=[]
label=[]
image_folder=os.listdir(train_data)
for folder in image_folder:
    folder_path=os.path.join(train_data,folder)
    filelist=os.listdir(folder_path)
    for file in filelist:
        new_path=os.path.join(folder_path,file)
        filepath.append(new_path)
        label.append(folder)


image_data=pd.Series(filepath,name="image_data")
label_data=pd.Series(label,name="label")
train_dataset=pd.concat([image_data,label_data],axis=1)
print(train_dataset.head())


print(train_dataset.shape)


print(train_dataset.isnull().sum())


print(train_dataset["label"].value_counts())


filepath=[]
label=[]
image_folder=os.listdir(test_data)
for folder in image_folder:
    folder_path=os.path.join(test_data,folder)
    filelist=os.listdir(folder_path)
    for file in filelist:
        new_path=os.path.join(folder_path,file)
        filepath.append(new_path)
        label.append(folder)


image_data=pd.Series(filepath,name="image_data")
label_data=pd.Series(label,name="label")
test_dataset=pd.concat([image_data,label_data],axis=1)
test_dataset.head()


print(test_dataset.shape)


print(test_dataset.isnull().sum())


print(test_dataset["label"].value_counts())


filepath=[]
label=[]
image_folder=os.listdir(valid_data)
for folder in image_folder:
    folder_path=os.path.join(valid_data,folder)
    filelist=os.listdir(folder_path)
    for file in filelist:
        new_path=os.path.join(folder_path,file)
        filepath.append(new_path)
        label.append(folder)


image_data=pd.Series(filepath,name="image_data")
label_data=pd.Series(label,name="label")
valid_dataset=pd.concat([image_data,label_data],axis=1)
print(valid_dataset.head())


print(valid_dataset.shape)

print(valid_dataset["label"].value_counts())
