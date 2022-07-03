from MySQLdb import Error
from bs4 import BeautifulSoup
import mysql.connector
import requests 
from datetime import datetime


eventlist=[]
def searchevents(city,state):

    URL = "https://www.eventbrite.com/d/"+state+"--"+city+"/dog-events/"
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results=soup.find_all("div", {"class": "eds-event-card-content__content"})
    events=[]

    for item in results:
        links = item.find_all('a')
        blog_titles = item.findAll('h3', attrs={"class":"eds-event-card-content__title eds-text-color--ui-800 eds-text-bl eds-text-weight--heavy"})
        venue = item.findAll("div", {"data-subcontent-key":"location"})
        url=''
        location=''
        for link in links:
            if "href" in link.attrs:
                url=link.attrs['href']
        for loc in venue:
            location=loc.text
        for title in blog_titles:
            if str(title.text).find('Dog') != -1:
                event={}
                event['title']= str(title.text)
                event['url']=str(url)
                event['location']=str(location)
                event['source']="Eventbrite"
                event['state']=state
                event['city']=city
                events.append(event)
    return events



def readInput():

    #inputdata=searchevents('')
    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="sou@12345",
            database="playdate",
            auth_plugin="mysql_native_password",
        )
        mycursor =mydb.cursor()
        mycursor.execute("select city, state_code, zipcode from location where state_code='CA' LIMIT 100")
        data=mycursor.fetchall()

        for row in data:
            city=row[0]
            state=row[1]
            if city != None and state!=None:
                inputdata=searchevents(city,state)
                if inputdata is not None:
                    eventlist.extend(inputdata)
        event_id=100
        count=0
        for item in eventlist:
            if count%2 == 0:
                name=item['title']
                location=item['location']
                url=item['url']
                state=item['state']
                city=item['city']
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                mycursor.execute("select zipcode from location where city=%s and state_code=%s LIMIT 1",(city,state))
                zipcode=mycursor.fetchone()
                print(str(zipcode).strip("(,)"))

                mycursor.execute("INSERT INTO event(event_id,name,created_on,description,category,street_address,location,url) VALUES (%s,%s,%s,'','pet',%s,%s,%s)",(event_id,name,formatted_date,location,str(zipcode).strip("(),"),url))
                event_id=event_id+1
            count=count+1
            # key=event_id
            # #print(key)
            # mycursor.execute("Insert into public_event(event_id,url) values(%s,%s)",(key,url))

        mydb.commit()
            



        #

        # for item in inputdata:
        #     country_code=item[0]
        #     zipcode = item[1]
        #     city= item[2]
        #     state=item[3]
        #     state_code=item[4]
        #     #insert_query = ("INSERT INTO location (country_code, zipcode, city, state_name, state_code) VALUES(%s,%d,%s,%s,%s)",(country_code,zipcode,city,state,state_code))
        #     #print(insert_query)
        #     mycursor.execute("INSERT INTO playdate.location (country_code, zipcode, city, state_name, state_code) VALUES(%s,%s,%s,%s,%s)",(country_code,zipcode,city,state,state_code))
        #     mydb.commit()
    except Error as e:
        print(e)
    

    
    
    
    
    # with open("location.txt", "r") as datafile:
    #     x1 = []
    #     for each_line in datafile:
    #         x1.append(each_line.split('\t'))
    #     inputdata.extend(x1)
    
    # for item in inputdata:
    #     country_code=item[0]
    #     zipcode = item[1]
    #     city= item[2]
    #     state=item[3]
    #     state_code=item[4]

    #     # if city == "Fremont":
    #     #     print(country_code + "\t"+ zipcode + "\t"+ city + "\t"+ state + "\t"+ state_code + "\n")

        
   



# Main program
if __name__ == "__main__":
    readInput()


    

        
        




