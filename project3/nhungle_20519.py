{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4885e3ef-a37a-4cd9-b685-edc019606b4e",
   "metadata": {},
   "source": [
    "Putet the path of the test project 3 folder to parent_directo\n",
    "\n",
    "PutSet the folder containing unclassified files to the test folder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "5e28cc70-e389-4af0-9eb8-78182ab41e30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Successful!!!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "# Please put your parent directory here\n",
    "parent_directory = r'D:\\Challenge Python\\PYTHON TUTORIAL\\Project 3'\n",
    "\n",
    "# Create Folder CSV ('.csv')\n",
    "csv_path = os.path.join(parent_directory, 'CSV FOLDER')\n",
    "os.makedirs(csv_path, exist_ok=True)\n",
    "\n",
    "# Create Folder Document ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')\n",
    "document_path = os.path.join(parent_directory, 'DOCUMENT FOLDER')\n",
    "os.makedirs(document_path, exist_ok=True)\n",
    "\n",
    "# Create Folder Image ('.jpg', '.jpeg', '.png', '.gif')\n",
    "image_path = os.path.join(parent_directory, 'IMAGE FOLDER')\n",
    "os.makedirs(image_path, exist_ok=True)\n",
    "\n",
    "# Create Folder Audio ('.mp3')\n",
    "audio_path = os.path.join(parent_directory, 'AUDIO FOLDER')\n",
    "os.makedirs(audio_path, exist_ok=True)\n",
    "\n",
    "# Create Folder Compressed ('.zip', '.rar', '.7z')\n",
    "compressed_path = os.path.join(parent_directory, 'COMPRESSED FOLDER')\n",
    "os.makedirs(compressed_path, exist_ok=True)\n",
    "\n",
    "# Create Folder Executable ('.exe', '.bat', '.sh', '.msi')\n",
    "executable_path = os.path.join(parent_directory, 'EXECUTABLE FOLDER')\n",
    "os.makedirs(executable_path, exist_ok=True)\n",
    "\n",
    "# Path of folder containing files\n",
    "folder_examples = os.path.join(parent_directory, r'Project 3-20240803T131828Z-001\\Project 3')\n",
    "\n",
    "# Get path of files in folder\n",
    "items = os.listdir(folder_examples)\n",
    "files_path = [os.path.join(folder_examples, item) for item in items]\n",
    "\n",
    "for file in files_path:\n",
    "    file_extension = os.path.splitext(file)[1].lower()\n",
    "\n",
    "    if file_extension == '.csv':\n",
    "        shutil.copy(file, csv_path)\n",
    "    elif file_extension in ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'):\n",
    "        shutil.copy(file, document_path)\n",
    "    elif file_extension in ('.jpg', '.jpeg', '.png', '.gif'):\n",
    "        shutil.copy(file, image_path)\n",
    "    elif file_extension == '.mp3':\n",
    "        shutil.copy(file, audio_path)\n",
    "    elif file_extension in ('.zip', '.rar', '.7z'):\n",
    "        shutil.copy(file, compressed_path)\n",
    "    elif file_extension in ('.exe', '.bat', '.sh', '.msi'):\n",
    "        shutil.copy(file, executable_path)\n",
    "    else:\n",
    "        print('None!!!')\n",
    "\n",
    "print('Successful!!!')"
   ]
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
