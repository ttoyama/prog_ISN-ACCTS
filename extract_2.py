from BeautifulSoup import BeautifulStoneSoup as bss
from BeautifulSoup import BeautifulSoup as bs
import re
import csv

f = open("xml/ICTRP-Results_saro.xml", "r")
f_data = f.readlines()
#delete data after scientific titlech   

x = bs(''.join(f_data))

#if __name__ == '__main__':
    #text_output()
    #text_min_output()
    #make_csv()
    #make_pdf()