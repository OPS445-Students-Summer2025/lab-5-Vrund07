#!/usr/bin/env python3
# Author ID: vspadariya

def read_file_string(file_name):
      with open(file_name, 'r') as file:
        return file.read()
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
      with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as file:
        file.write(string_of_lines)
    # Takes two strings, appends the string to the end of the file

def write_file_list(file_name, list_of_lines):
     with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(f"{line}\n")

    # Takes a string and list, writes all items from list to file where each item is one line

def copy_file_add_line_numbers(file_name_read, file_name_write):
      with open(file_name_read, 'r') as infile, open(file_name_write, 'w') as outfile:
        for index, line in enumerate(infile, start=1):
            outfile.write(f"{index}:{line.strip()}\n")
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
