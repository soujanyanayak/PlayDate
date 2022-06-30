from MySQLdb import Error
import mysql.connector 

inputdata=[]



def readInput():
    global inputdata
    global cities

    with open("location.txt", "r") as datafile:
        x1 = []
        for each_line in datafile:
            x1.append(each_line.split('\t'))
        inputdata.extend(x1)

    try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="sou@12345",
            database="playdate",
            auth_plugin="mysql_native_password",
        )
        mycursor =mydb.cursor()
            
        for item in inputdata:
            country_code=item[0]
            zipcode = item[1]
            city= item[2]
            state=item[3]
            state_code=item[4]
            #insert_query = ("INSERT INTO location (country_code, zipcode, city, state_name, state_code) VALUES(%s,%d,%s,%s,%s)",(country_code,zipcode,city,state,state_code))
            #print(insert_query)
            mycursor.execute("INSERT INTO playdate.location (country_code, zipcode, city, state_name, state_code) VALUES(%s,%s,%s,%s,%s)",(country_code,zipcode,city,state,state_code))
            mydb.commit()
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


    

        
        




