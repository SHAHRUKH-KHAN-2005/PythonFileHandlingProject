# 📁 Python File Management System

A simple **File Management System built with Python** that allows users to perform basic **CRUD operations** on files through a command-line interface.

This project uses Python's built-in `pathlib` and `os` modules to create, read, update, and delete files.

## 🚀 Features

The project supports the following operations:

* 📄 **Create a File**
* 📖 **Read a File**
* ✏️ **Update a File**

  * Rename a file
  * Overwrite file content
  * Append content to a file
* 🗑️ **Delete a File**
* 📂 Display available files and folders
* ⚠️ Basic exception handling for errors

## 🛠️ Technologies Used

* **Python**
* `pathlib`
* `os`
* File Handling
* Exception Handling
* Command Line Interface (CLI)

## 📌 CRUD Operations

| Operation  | Description                                         |
| ---------- | --------------------------------------------------- |
| **Create** | Creates a new file and adds user-provided content   |
| **Read**   | Reads and displays the contents of an existing file |
| **Update** | Renames, overwrites, or appends data to a file      |
| **Delete** | Deletes an existing file                            |

## 📂 Project Structure

```text
File-Management-System/
│
├── main.py
└── README.md
```

> Replace `main.py` with the actual name of your Python file if it is different.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to the project directory

```bash
cd your-repository-name
```

### 3. Run the Python program

```bash
python main.py
```

## 💻 How It Works

When the program starts, it displays a menu:

```text
Press 1 for writing into a file
Press 2 for reading a file
Press 3 for updating into a file
Press 4 for deleting a file

enter your choice:
```

### 1️⃣ Create a File

Select option `1`.

The program:

1. Displays existing files and folders.
2. Asks for the file name.
3. Checks whether the file already exists.
4. Creates the file if it doesn't exist.
5. Takes input from the user.
6. Writes the input into the file.

### 2️⃣ Read a File

Select option `2`.

The program:

1. Displays available files.
2. Asks for the file name.
3. Checks whether the file exists.
4. Opens the file in read mode.
5. Displays its contents.

### 3️⃣ Update a File

Select option `3`.

You can perform three types of updates:

```text
Press 1 for rename the file name
Press 2 for overwriting the data into a file
Press 3 for appending into the file
```

#### Rename

Changes the existing file name using:

```python
path.rename(path2)
```

#### Overwrite

Replaces the existing file content using:

```python
open(path, "w")
```

#### Append

Adds new content to the existing file using:

```python
open(path, "a")
```

### 4️⃣ Delete a File

Select option `4`.

The program checks the selected file and removes it from the system.

## 🧠 Concepts Learned

This project helped in understanding several important Python concepts:

* File handling
* `open()` function
* Read (`r`) mode
* Write (`w`) mode
* Append (`a`) mode
* `pathlib.Path`
* `Path.exists()`
* `Path.is_file()`
* `Path.rglob()`
* `Path.rename()`
* `os.remove()`
* Exception handling using `try-except`
* User input using `input()`
* Conditional statements
* Functions
* CRUD operations

## 🔍 Example

A typical workflow could look like:

```text
Press 1 for writing into a file
Press 2 for reading  a file
Press 3 for updating  into a file
Press 4 for deleting a file

enter your choice:- 1

enter the file name you want to create:- notes.txt
enter the data you want to add in a file:- Learning Python File Handling

FILE CREATED SUCCESSFULLY
```

The file can then be read using option `2`.

## 🎯 Project Objective

The main objective of this project is to understand how Python can interact with the file system and perform basic **Create, Read, Update, and Delete (CRUD)** operations using a command-line interface.

## 🔮 Future Improvements

Some possible improvements for this project are:

* Add a continuous menu using a `while` loop.
* Add a proper exit option.
* Allow users to create folders.
* Add file search functionality.
* Add file copying and moving functionality.
* Add file size and modification date information.
* Improve input validation.
* Add a graphical user interface (GUI).
* Add confirmation before deleting a file.
* Support selecting files using numbers instead of typing file names.

## 👨‍💻 Author

**SRK**

This project was created as a Python practice project to learn **file handling, `pathlib`, `os`, exception handling, and CRUD operations**.

---

⭐ If you found this project useful, consider giving the repository a star!
