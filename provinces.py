provinces_list = []

def main():
    text_list = read_provinces_file("provinces.txt")
    print (text_list)
    

def read_provinces_file(filename):

    


    with open(filename, "rt") as text_file:

        for line in text_file:
            clean_line = line.strip()
            provinces_list.append(clean_line)
            

    provinces_list.pop()
    provinces_list.pop(0)
    count = 0
    for i in provinces_list:
        if i == "AB":
            index = provinces_list.index(i)
            provinces_list[index] = "Alberta"
    
    count = provinces_list.count("Alberta")    

            
    print(f"Alberta is {count} times")
        
        

    return provinces_list
            
if __name__ == "__main__":
    main()


