#!/usr/bin/python3
import sys 

def sumFunc(myfile,index):
    sum=0.0
    first=True
    # reading each line of the file and printing to the console
    for line in myfile:
        stringLine=line.split(",")
        if first:
            nameC=stringLine[index]
            first=False
        # If it was a number it would pass if text it would not pass
        try:
            sum+=float(stringLine[index])
        except:
            pass

    print("The total ", str(nameC) , "is", f'{sum:.2f}' )


# Checks if it is a file of the right type
def isCsv(file):
    if file.endswith(".csv"):
        return True
    else:
        return False

def main():
    try:
        # Checks boundary conditions
        if (len(sys.argv) == 3)==False  or isCsv(sys.argv[1])==False:
            raise ValueError
            exit()
        else:
            # declaration of variables
            file,column = sys.argv[1], int(sys.argv[2])
            myfile = open(file)
            sumFunc(myfile,column)
    except ValueError:
        print("Error! Invalid input")
        print("Usage: sum-columns.py <'FileName.csv'> <'Integer'> ")

main()
