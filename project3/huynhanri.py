{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c3472c03-73be-4d2b-8fb2-5fbe717c2cac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Files have been sorted and moved successfully.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "# Define file types and corresponding folders\n",
    "file_types = {\n",
    "    'Images': ['.jpg', '.png'],\n",
    "    'Documents': ['.tsv','.pdf', '.csv', '.doc', '.txt', '.xls'],\n",
    "    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],\n",
    "    'Compressed': ['.zip', '.rar', '.tar', '.gz'],\n",
    "    'Audio': ['.m4a', '.mp3', '.wav', '.aac'],\n",
    "    'Executables': ['.exe', '.bat', '.sh']\n",
    "}\n",
    "\n",
    "\n",
    "source_dir = r'C:\\Users\\lehoa\\OneDrive\\Desktop\\An Ri\\Python_Project3\\Source_dir'  \n",
    "\n",
    "\n",
    "dest_dir = r\"C:\\Users\\lehoa\\OneDrive\\Desktop\\An Ri\\Python_Project3\\Dest_dir\"  \n",
    "\n",
    "# Create folders if they don't exist\n",
    "for folder in file_types.keys():\n",
    "    folder_path = os.path.join(dest_dir, folder)\n",
    "    if not os.path.exists(folder_path):\n",
    "        os.makedirs(folder_path)\n",
    "\n",
    "# Function to move files to respective folders\n",
    "def move_files():\n",
    "    for file_name in os.listdir(source_dir):\n",
    "        file_path = os.path.join(source_dir, file_name)\n",
    "        \n",
    "        # Ensure it's a file and not a directory\n",
    "        if os.path.isfile(file_path):\n",
    "            moved = False\n",
    "            for folder, extensions in file_types.items():\n",
    "                if any(file_name.lower().endswith(ext) for ext in extensions):\n",
    "                    shutil.move(file_path, os.path.join(dest_dir, folder, file_name))\n",
    "                    moved = True\n",
    "                    break\n",
    "            \n",
    "            # If file type is not recognized, move to 'Others' folder\n",
    "            if not moved:\n",
    "                others_folder = os.path.join(dest_dir, 'Others')\n",
    "                if not os.path.exists(others_folder):\n",
    "                    os.makedirs(others_folder)\n",
    "                shutil.move(file_path, os.path.join(others_folder, file_name))\n",
    "\n",
    "# Execute the function to move files\n",
    "move_files()\n",
    "\n",
    "print(\"Files have been sorted and moved successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac7f08d7-eb1e-4a66-a567-9417dc2faa54",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

#Please check your submission carefully next time.