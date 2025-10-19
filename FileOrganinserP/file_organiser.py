import os
import shutil
import time








file_types = {
    'images': ['.jpg','.jpeg', '.png', '.gif'],
    'documents': ['.txt', '.pdf','.docx','.pptx'],
    'videos': ['.mp4','.mkv','.flv'],
    'audio': ['.mp3','.wav'],
    'archive' :['.zip','.tar','.rar'],
    'spreedsheet': ['.xls','xlsx','csv']
}

def path_folder():
    print()
    while True:
        try:
            path = input("Enter folder path: ")
            
            if os.path.isdir(path):
                if os.path.exists(path) and not os.path.isfile(path):
                    if not os.listdir(path):
                        print("Folder is empty!, try again")
                    else:
                        break
                
            elif path == "":
                raise TypeError
            elif os.path.exists(path) == False:
                raise TypeError
            
            

        except TypeError:
            print("Please Enter a valid path file to scan\n")
        except FileNotFoundError:
            print("File Not Found")
            print("Please Enter an appropriate file path\n")        

    with open('Stored.txt', 'w') as f:
        f.write(path)
        f.close()
    print()
    print("\033[1:33mFolder Path Saved\n\033[0m")
    return path    


def scan_folder():
    print()
    while True:
        try:
            scan = input("Enter folder path to scan: ")
            
            if os.path.isdir(scan):
                if os.path.exists(scan) and not os.path.isfile(scan):
                    if not os.listdir(scan):
                        print("Folder is empty!, try again")
                    else:
                        break
                
            elif scan == "":
                raise TypeError
            elif os.path.exists(scan) == False:
                raise TypeError
            

        except TypeError:
            print("Please Enter a valid path file to scan\n")
        except FileNotFoundError:
            print("File Not Found")
            print("Please Enter an appropriate file path\n")        

    with open('Stored.txt', 'w') as f:
        f.write(scan)
        f.close()

    print("\nScanning",end="")

    for _ in range(4):
        time.sleep(0.5)
        print(".",end='',flush=True)
        
    print()    

    

    print("\n--- Files Found ---")
    with os.scandir(path = scan) as d:
        for f in d:
            for key, myfile in enumerate(d,1):
                print(f"\033[1;31m[{key}] \033[1;33m{myfile.name}\033[0m")  
    print("\n\033[1:33mFolder Path Saved\033[0m")
    input("\nPress Enter to continue...")
    print()
    return scan


def create_Nfolders(current_dir,folders):
    created = []
    for folder in folders:
        new_folder_path = os.path.join(current_dir,folder)
        if not os.path.exists(new_folder_path): 
            os.makedirs(new_folder_path)
            created.append(folder)
    if len(created) > 0:
        print("\nCreating folders",end="")
        for _ in range(4):
            time.sleep(0.4)
            print(".",end='',flush=True)        
        
    print()    
    for i, name in enumerate(created,1):
        print(f"\033[1;31m[{i}]\033[1;33m {name}/ \033[0mCreated")        
                
    print()        


def organise_file(current_dir,file_types):
    to_orgainse = None
    while True:
        try:
            to_orgainse = input("Orgainse files into subfolders by type? (Yes/No): ").capitalize()
            if to_orgainse in ("Yes", "No"):
                break
            else:
                raise ValueError
        except ValueError:
            print("\033[1;31mPlease Enter (Yes/No)\033[0m\n")
        
      
    if to_orgainse == "Yes":
        cout_moved = 0
        create_Nfolders(current_dir,file_types.keys()) 
        has_file_to_move = False    
        for filename in os.listdir(current_dir):
            file_path = os.path.join(current_dir,filename)

            if os.path.isdir(file_path):
                continue
           
            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder,extension in file_types.items():       
                if file_ext in extension:
                    has_file_to_move = True
                    break

            if has_file_to_move:
                break
            
        if has_file_to_move:
            print("Moving files", end="")
            for _ in range(4):
                time.sleep(0.45)
                print(".", end='', flush=True)
            print()

        for filename in os.listdir(current_dir):
            file_path = os.path.join(current_dir, filename)
            if os.path.isdir(file_path):
                continue
            
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extension in file_types.items():
                if file_ext in extension:
                    target_folder = os.path.join(current_dir, folder)
                    shutil.move(file_path, target_folder)
                    cout_moved += 1
                    print(f"\033[1;31m[{cout_moved}]\033[0m Moved \033[1;33m{filename}\033[0m to {folder}/")
                    break           

        if cout_moved ==0:
            print("\n\033[1;31mFiles are already moved!")
            print("\033[1;31mFolder is organised!\033[0m")        
        input("\nPress Enter to continue...")
        print()            

    elif to_orgainse == "No":
        input("\nPress Enter to continue...")
        print()            
                        

def move_file(current_dir):
    
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
    if not files:
        print("\033[1;31mNo files to move\033[0m")
    
    else:
        print(f"--- Files Found in {os.path.basename(current_dir)} ---\n")
        for key, filename in enumerate(files, 1):
            print(f"\033[1;31m[{key}] \033[1;33m{filename}\033[0m")

        while True:
            try:
                file_num = int(input("\nEnter number of file to move: "))
                if not (1 <= file_num <= len(files)):
                    raise ValueError
                break
            except ValueError:
                print("\n\033[1;31mInvalid number\033[0m")
                print("\033[1;31mPlease try again!\033[0m")

        while True:
            try:
                dest = input("Enter destination folder: ")
                if dest == "":
                    raise TypeError
                elif not os.path.isdir(dest):
                    raise ValueError
                elif not os.path.exists(dest):
                    raise ValueError
                break
            except TypeError:
                print("\n\033[1;31mPlease Enter a folder path\033\n[0m")
                
            except ValueError:
                print("\n\033[1;31mInvalid Path\033[0m")
                print("\033[1;31mPlease try again!\033\n[0m")

        chosen_file = files[file_num-1]
        src = os.path.join(current_dir,chosen_file)
        if not os.path.exists(src):
            print(f"File Not found: {src}")
            return

        shutil.move(src,dest)
        print(f"\n\033[1;33mFile {chosen_file} Moved to {os.path.basename(dest)}\033[0m")

    input("\nPress Enter to continue...")
    print()    

               


def delete_emptyf(base_dir):
    print()
    deleted = set()
    count_del = 0

    for current_dir, subdirs,files  in os.walk(base_dir,topdown=False):
        still_has_subdirs = False
        for subdir in subdirs:
            if os.path.join(current_dir,subdir) not in deleted:
                still_has_subdirs = True
                break

        if not any(files) and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted.add(current_dir)
            count_del +=1
    if count_del > 0:
        print("Currently Deleting empty folders",end="")
        for _ in range(4):
            time.sleep(0.45)
            print(".",end= "",flush=True)
        print()
    else:
        print("\033[1;31mAll folders has been deleted!\033[0m")
        print("\033[1;31mYour folder is clean👍\033[0m")
                
    
    if count_del > 0:
        print(f"\n\033[1;31m{count_del} folders has been deleted!\033[0m")

    print()
    
    while True:
        try:
            check = input("Do you wish to delete all setup files(.exe)? (Yes/No): ").capitalize()
            if check in ("Yes","No"):
                break
            else:
                raise ValueError
        except ValueError:
            print()
            print("\033[1;31mPlease type (Yes/No)\033[0m\n")

    if check == "Yes":
        exe_to_delete = 0

        for filename in os.listdir(base_dir):
            file_path = os.path.join(base_dir,filename)
                
            if os.path.isdir(file_path):
                continue
                
            file_ext = os.path.splitext(filename)[1]

            if file_ext == ".exe":
                exe_to_delete+= 1
                os.remove(file_path)
                print(f"\n\033[1;31m{filename} has been deleted\033[0m")
                
        if  exe_to_delete == 0:
            print("\n\033[1;31mNo setup files!\033[0m")
        
        input("\nPress Enter to continue...")
        print()             
    else:            
        input("\nPress Enter to continue...")
        print()

         

               


def main():
    options = {"\033[1;35mA)" : "\033[1;33mScan a folder",
               "\033[1;35mB)" : "\033[1;33mOrganise files by type",
               "\033[1;35mC)" : "\033[1;33mMove a file",
               "\033[1;35mD)" : "\033[1;33mDelete an empty folder",
               "\033[1;35mE)": "\033[1;33mSave log & Exit\033[0m"}
    print("="*40)
    print("            🗂️  \033[0;33mFile \033[0;37mOrganizer\033[0m")
    print("="*40)
    print()

    
    

       
    while True:
        
        print("Choose an action:")
        for key,value in options.items():
            print(f"{key} {value}")
        print()
        while True:    
            try:
                action = input("> ").upper()
                if action is not None and action.isalpha() and action in("A","B","C","D","E"):
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Please Enter a choice (A-E)")
            
        if action == "A":
            scan_folder()
        elif action == "B":
            with open('Stored.txt','r') as f:
                content = f.read().strip()
                if not content:
                    current_dir = path_folder()
                else:
                    current_dir = content
                    print()
                    print(current_dir)
                    while True:
                        try:
                            check = input("Is this the correct path to folder? (Yes/No): ").capitalize()
                            if check in ("Yes","No"):
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print()
                            print(current_dir)
                            print("\033[1;31mPlease type (Yes/No)\033[0m\n")
                    if check == "No":
                        current_dir = path_folder()
                        
                    else:
                        print()
                        pass           
                            
                    
            organise_file(current_dir,file_types)

        elif action =="C":
            with open('Stored.txt','r') as f:
                content = f.read().strip()
                if not content:
                    current_dir = path_folder()
                else:
                    current_dir = content
                    print()
                    print(current_dir)
                    while True:
                        try:
                            check = input("Do you wish to change the folder path (Yes/No): ").capitalize()
                            if check in ("Yes","No"):
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print()
                            print(current_dir)
                            print("\033[1;31mPlease type (Yes/No)\033[0m\n")
                    if check == "Yes":
                        current_dir = path_folder()
                        
                    else:
                        print()
                        pass          
            move_file(current_dir)   

        elif action == "D":
            with open('Stored.txt', 'r') as f:
                content = f.read().strip()
                if not content:
                     current_dir = path_folder()
                else:
                    current_dir = content
            delete_emptyf(current_dir)            

        elif action == "E":
            print("Saving action log",end="")
            for _ in range(4):
                time.sleep(0.45)
                print(".",end= "",flush=True)
            print("\nGoodBye!👋")    
            break  

        


 
       
    
                 

if __name__ == '__main__':
    main()    