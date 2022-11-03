# Code for displaying the extension of a file
extensions = {"pdf" : "Portable Document File", "doc" : "Word document", "docx" : "Word document",
              "html" : "Hyper Text Markup Language", "xlsx" : "Excel Spreadhseet", "txt" : "Text File",
              "py" : "Python File", "cpp" : "C++ File", "js" : "JavaScript File", "java" : "Java File"}

file_name = input("Enter the file name: ")
file_ext = file_name.split(".")[-1]

print(f"The given file is a {extensions[file_ext]}.")