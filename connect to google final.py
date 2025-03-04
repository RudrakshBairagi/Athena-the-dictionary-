from bs4 import BeautifulSoup
import requests
y="1"
print("Welcome to ATHENA")
for i in range(0,100):
    if y=="1":
        print()
        n=input("Enter the word: ")
        d="https://www.dictionary.com/browse/"
        g=d+n

        html_text= requests.get(g).text#searches the content in browser

        soup= BeautifulSoup(html_text,"lxml")
        content= soup.find('div',class_='NZKOFkdkcvYgD3lqOIJw')
        c=str(content)#fetched content from dictionary.com
        if c=='None':
            print()
            print("Word does not exist, kindly check spelling")
        else:
            print()
            print(content.text)
        
        
        print()
        y=input('''Would you like to continue?

PRESS 1 FOR YES/////PRESS ANY OTHER KEY FOR NO

INPUT: ''')
    else:
        print()
        print("Thanks for working with us")
        break
       






