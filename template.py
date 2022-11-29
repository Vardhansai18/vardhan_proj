import os 
dir = [
    os.path.join("data","raw") , 
    os.path.join("data","proccessed") ,
    "data_given",
     "Notebooks" , 
     "savedmodels",
      "src"
] 
for i in dir:
    os.makedirs(i,exist_ok=True)
    with open(os.path.join(i,".gitkeep"),'w') as f:
        pass

files = ["dvc.yaml","parms.yaml",".gitignore",os.path.join("src","__init__.py")] 

for i in files:
    with open(i,'w') as f:
        pass 