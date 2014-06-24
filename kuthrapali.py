#!/usr/bin/python3

from math import log

MALE  =False
FEMALE=True 

def calc_sex(child):
    if child == 0:
        return MALE
    elif child == 1:
        return FEMALE
    else:
        part = log(child, 2)//1
        return not calc_sex( child % (2**part)) 

def get_sex(generation, child):
    sex = calc_sex(child-1)
    if sex == MALE:
        return 'Male'
    else:
        return 'Female'

def main():
    lines = input()
    requests = []
    for i in range(int(lines)): 
        requests.append(input())

    for request in requests: 
        generation, child = map(lambda x: int(x), request.split())
        sex = get_sex(generation,child)
        print(sex) 

if __name__ == "__main__":
    main()
   
