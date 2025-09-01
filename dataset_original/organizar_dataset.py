import os
import shutil
import random


base_dir = r"C:\Users\Jeide\OneDrive - ucatolica.edu.co\DECIMO SEMESTRE\TRABAJO DE GRADO II\TRABAJO DE GRADO\DESARROLLO DEL TRABAJO DE GRADO\Imagenes Tizon Tardio"


dataset_destino = os.path.join(base_dir, "dataset_organizado")

clases = [
    d for d in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, d)) 
    and d not in [".git", "dataset_organizado"]
]


train_split = 0.7
val_split = 0.2
test_split = 0.1


for split in ["train", "val", "test"]:
    for clase in clases:
        path = os.path.join(dataset_destino, split, clase.replace(" ", "_"))
        os.makedirs(path, exist_ok=True)


for clase in clases:
    class_path = os.path.join(base_dir, clase)
    
    images = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]
    random.shuffle(images)
    
    total = len(images)
    train_end = int(train_split * total)
    val_end = int((train_split + val_split) * total)
    
    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]
    
 
    def copiar(files, split):
        for idx, f in enumerate(files, start=1):
            src = os.path.join(class_path, f)
            ext = os.path.splitext(f)[1] 
            new_name = f"img_{idx:04d}{ext}"  
            dst = os.path.join(dataset_destino, split, clase.replace(" ", "_"), new_name)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    
    copiar(train_files, "train")
    copiar(val_files, "val")
    copiar(test_files, "test")
    
    print(f"Clase {clase}: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test")

print("Dataset organizado ")
