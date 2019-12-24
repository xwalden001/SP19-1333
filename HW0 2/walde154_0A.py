def pounds2kilo(pounds):
    if type(pounds) == int or type(pounds)== float:
        kilos = float(pounds)*0.454 #Convert
        return str(float(kilos))+ " kilos"
    else:
        return "None"

def main():
    pounds = 100 #input("Enter Weight in Pounds: ")
    pounds2kilo(pounds)
    print(pounds2kilo(pounds))
    pounds = 22 #input("Enter Weight in Pounds: ")
    pounds2kilo(pounds)
    print(pounds2kilo(pounds))
    pounds = 0.5 #input("Enter Weight in Pounds: ")
    pounds2kilo(pounds)
    print(pounds2kilo(pounds))

if __name__ == '__main__':
    main()
