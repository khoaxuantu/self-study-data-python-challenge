import os

folder_path_name = os.path.join(os.getcwd(), 'challenge_3')

guide_dict = {}

def combine_path(a, *args)->list:
    return [os.path.join(a, item) for item in args]

def create_split_guidance(cur_folder) ->  None:
    '''
    1. Tao list cac path to filename
    2. Tach cac extension
    3. Tao dict dang ten extension : cac filename tuong ung
    '''
    path_list = None
    for dirpath, dirnames, filenames in os.walk(folder_path_name):
        path_list = combine_path(dirpath, *filenames)
    
    textname = None
    for item in path_list:
        res_list = []
        ext_name = (os.path.splitext(item)[1]).lower().replace(".","")
        textname = os.path.basename(item)
        if (ext_name not in guide_dict):
            res_list.append(textname)
            guide_dict[ext_name] = res_list
        else:
            guide_dict[ext_name].append(textname)
    # Sort luon ket qua trong dict:
    for key, values in guide_dict.items():
        guide_dict[key] = sorted(values)
    return True

def make_folder(in_dict) -> None:
    '''
    1. Bien doi cac key trong dict (form: ext+"Folder")
    2. Tao cac folder tuong ung
    '''
    path_to_make = os.getcwd()
    key_name = [item + "Folder" for item in list(guide_dict.keys())]
    for item_ in key_name:
        folder_path = os.path.join(path_to_make, item_)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def move_file_to_folder(guide_dict) -> None:
    goal_folders = []
    for dirname in os.walk(os.getcwd()):
        for item_path in dirname[1]:
            if (item_path.endswith("Folder")):
                goal_folders.append(item_path)
    
    key_list = sorted([item for item in list(guide_dict.keys())])
    goal_folders = sorted(goal_folders, key = lambda x: x[0])

    # Move file:
    ind = 0
    upper_bound = len(key_list)

    while(ind < upper_bound):
        des_path = os.path.join(os.getcwd(), goal_folders[ind])
        list_move_file = [os.path.join(folder_path_name, item) for item in guide_dict[key_list[ind]]]
        list_new_file = [os.path.join(des_path, item) for item in guide_dict[key_list[ind]]]
        
        sub_ind = 0
        max_upper = len(list_move_file)
        while(sub_ind < max_upper):
            os.rename(list_move_file[sub_ind], list_new_file[sub_ind])
            sub_ind += 1
        
        ind += 1

def solve():
    create_split_guidance(folder_path_name)
    make_folder(guide_dict)
    move_file_to_folder(guide_dict)

if __name__ == "__main__":
    solve()