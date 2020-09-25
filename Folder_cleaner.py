import os

source_dir = '...'
target_dir = '...'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    try:
        if file_name != "Stuff":
            extension = str(os.path.splitext(source_dir + '/' + file_name)[1])
            i = 1
            old_name = source_dir + "/" + file_name
            file_exist = os.path.isfile(target_dir + "/" + file_name)

            while file_exist == True:
                i = i + 1
                split = os.path.split(target_dir + "/" + file_name)
                new_name = source_dir + "/" + split[1][0] + str(i) + '.txt'
                file_name = split[1][0] + str(i) + '.txt'
                file_exist = os.path.isfile(target_dir + "/" + file_name)
                os.rename(old_name, new_name)

            source = source_dir + "/" + file_name
            
            #Use your own folders
            if extension == ".txt":
                destination = target_dir + "/.../" + file_name
            elif extension == ".py":
                destination = target_dir + "/.../" + file_name
            else:
                destination = target_dir + "/.../" + file_name
            
            os.rename(source, destination)
  except Exception:
    print(file_name)
