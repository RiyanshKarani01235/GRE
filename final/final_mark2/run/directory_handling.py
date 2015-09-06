import os

def directory_crawler(directory) : 
    dir_path = []
    dir_name = []
    file_name = []

    for (dirpath,dirname,filename) in os.walk(directory) :
        dir_path.append(dirpath)
        dir_name.append(dirname)
        file_name.append(filename)
    return[dir_path,dir_name,file_name]

def is_file_in_directory(file,directory) :

    [dir_path,dir_name,file_name] = directory_crawler(directory)

    if(file in os.listdir()) :
        return directory+'/'+file

    for (dirpath,dirname,filename) in os.walk(directory) :
        dir_path.append(dirpath)
        dir_name.append(dirname)
        file_name.append(filename)

    if ([file] in file_name) :
        index = file_name.index([file])
        _file_  = dir_path[index] + '/' + file
        print(_file_)
        return(_file_)
    
    else:
        for file_names in file_name :
            if(file in file_names) :
                index = file_name.index(file_names)
                _file_ = dir_path[index] + '/' + file
                return(_file_)

    return False
