import os
from sys import argv

fileName = argv[1]
comm1 = "nasm -f elf " + fileName + ".asm"
comm2 = "ld -m elf_i386 -o file " + fileName + ".o io.o"
comm3 = "./file"

if (len(argv)==3):
    if argv[2].strip()=="compileLink":
        os.system(comm1)
        os.system(comm2)
        print("Successfully Compiled and Linked.")
    elif argv[2].strip()=="compile":
        os.system(comm1)
        print("Successfully Compiled.")
    elif argv[2].strip()=="link":
        os.system(comm2)
        print("Successfully Linked.")
    else:
        print("'" + argv[2].strip() + "' is not recognized as a valid option.\nEnter a valid command\nThe valid commands are:\npython3 run.py <filename-without-asm> <option>\nOptions are:\ncompileLink : To compile and link\ncompile : To compile only\nlink : To link only\nTo directly run don't use any option.")
else:
    os.system(comm1)
    os.system(comm2)
    os.system(comm3)
