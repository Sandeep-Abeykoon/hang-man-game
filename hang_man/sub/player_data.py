# Importing modules and packages
import mysql.connector, datetime, webbrowser
from mysql.connector import Error



def curr_session(name, time_list, word_save_list, turn_save_list, status_list):
    """This function is to display the current session details to the player"""

    print("""\n=============================================================================
                                                                                         
            YOUR PROGRESSION ON THE CURRENT SESSION""")
    
    print("\nPlayer name :\t",name)
    print("\n-----------------------------------------------------------------------------")
    print("WORD\t\tCHANCES(Got)\tCHANCES(Exhausted)\tSTATUS")
    print()
    for i in range (len(word_save_list)):
        print(f'{(word_save_list[i]):20}{(len(word_save_list[i])):<16}{len(word_save_list[i])-(turn_save_list[i]):<22}{status_list[i]}')
    print("=============================================================================")

    # Calling the data insert function
    data_insert(name, time_list, word_save_list, turn_save_list, status_list)





def data_insert(name, time_list, word_save_list, turn_save_list, status_list):
    """This function insert the current session player gameplay data
       to the database"""

    option=""
    # Getting today's date
    today=datetime.date.today()

    # Initializing the database
    data_base={'host':'localhost',
               'database':'hang_man',
               'user':'root',
               'password':''}
    
    # Open database connection
    try:
        db=mysql.connector.connect(**data_base)
        if db.is_connected():
            print()
            print("Database Connected")
    except Error as e:
        print()
        print("Ooops!!")
        print(e)
        exit()    # The code exits if db connection is not established
    
    #Cursor object
    cursor=db.cursor()

    sql="INSERT INTO player_data VALUES(%s,%s,%s,%s,%s,%s,%s)"

    for x in range (len(word_save_list)):
        time=time_list[x]
        word=word_save_list[x]
        turns_provided=len(word)
        turns_used=(len(word))-(turn_save_list[x])
        status=status_list[x]
        values=(name,today,time,word,turns_provided,turns_used,status)
        cursor.execute(sql,values)
        db.commit()
    db.close()
    print("\n")

    #Getting and validating user option for viewing past records
    while option != 'y' or option != 'n':
        option=input("Do you want to view your past records ? (y/n) : ").lower()
        if option=='y' or option=='n':
            break
        else:
            print("Please enter a valid input")
            print()
            continue
    
    if option =='y':
        # Calling function
        past_records(name)
        
    


def past_records(name):
    """This function is to get the user gameplay records from the database"""

    # Initializing the database
    data_base={'host':'localhost',
               'database':'hang_man',
               'user':'root',
               'password':''}

    # Open database connection
    try:
        db=mysql.connector.connect(**data_base)
        if db.is_connected():
            print()
            print("Database Connected")
    except Error as e:
        print()
        print("Ooops!!")
        print(e)
        exit()   # The code exits if db connection is not established

    #Cursor object
    cursor=db.cursor()

    #SQL query
    cursor.execute(f"SELECT * FROM player_data WHERE player_name ='{name}' ")
    data=cursor.fetchall()

    # Calling function
    html_output(data)



    
def html_output(data):
    """This function will create an html file and display user records from a
       web browser"""

    # Creating a hrml file object
    html_object=open("records.html",'w')

    html_object.write("""<!DOCTYPE html>
    <html>
    <head>

    <title>Table with database</title>

    <style type="text/css">
    table {
    border-collapse: collapse;
    width: 100%;
    color: #d96459;
    font-family: monospace;
    font-size: 25px;
    text-align: center;
    }

    th{
    background-color: #d96459;
    color: white;
    }
		
    </style>
    </head>

    <body>

    <table>
    <tr>
    <th>PLAYER NAME</th>
    <th>PLAY DATE</th>
    <th>PLAY TIME</th>
    <th>WORD</th>
    <th>TURNS PROVIDED</th>
    <th>TURNS USED</th>
    <th>STATUS</th>
    </tr>""")

    # Using a loop to insert data to html table
    for i in range (len(data)):
        html_object.write(f"""<tr>
            <td> {(data[i][0])} </td>
	    <td> {(data[i][1])} </td>
	    <td> {(data[i][2])} </td>
	    <td> {(data[i][3])} </td>
	    <td> {(data[i][4])} </td>
	    <td> {(data[i][5])} </td>
            <td> {(data[i][6])} </td>
            </tr> \n""")

    html_object.write("""\n
    </table>
    </body>
    </html>""")

    # Closing the file object
    html_object.close()

    # Opening the html file using the web browser
    webbrowser.open_new_tab("records.html")

                      
                
       
     

    
    

    
    
   




