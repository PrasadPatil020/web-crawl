from bs4 import BeautifulSoup
from urllib.request import urlopen

#Taking input from user to concat url to crawl particular page number  
input1 = input("Enter the page number:") 

# conacting the taken input value to the follwoing given URL
url = f'https://stackoverflow.com/questions?tab=newest&page={input1}'

# Reading the above url using following python inbuilt package
page = urlopen(url).read()

# passing the load source page to beautiful soup package
soup = BeautifulSoup(page, 'html.parser')

#crawling the particular div element with its classname and creating as object
a = soup.find('div', {'id': 'questions'})

# using the particular selected soup object, Finding all div element with its classname  
question_summary = a.find_all('div',{'class':'question-summary'})

# a list to append final result
final_list = []

# iterating the all sellected div element
for k in question_summary:
    # finding the question by its child element and getting the text. Which is placed inbetween the element 
    question = k.find('div',{'class':'summary'}).find('h3').find('a').text

    #finding the user details by its child element
    user_detail = k.find('div',{'class':'summary'}).find('div',{'class':'started fr'}).find('div',{'class':'user-info'}).find('div',{'class':'user-details'}).find('a').text
    
    # creating temp dictionary to combine userdetail and question
    temp = {
        user_detail:question
    }

    # appending the created dictionary to final_list
    final_list.append(temp)

print(final_list)

    