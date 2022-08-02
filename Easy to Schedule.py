#"Easy to Schedule"
#This software serves as a tool to schedule clinical trial´s visit into the physician calendar (Excel ---> CSV)
# The program will automatically calculate the "Windows" for the following Study Visits.

from datetime import datetime
import csv
from datetime import timedelta, date

print(" Welcome to Easy to Schedule")
subject_id = str(input("Enter the subject ID: ")).capitalize()
date_str= str(input("Please enter the Screening day mm/dd/yyyy: ")) 
screening_day = datetime.strptime(date_str, ("%m/%d/%Y"))
print ("The screening day is:", screening_day)

def  write_csv():
#Abrir archivo para escritura
    csvfile = open("subjects_visits.csv","w")
    header = ["Subject_ID","Screening day", "Baseline visit", "First Follow-up visit", "Second Follow-up visit", "Third Follow-up visit", "Fourth Follow-up visit"]
    #Crear el objeto para escribir las lineas de archivo
    #basado en el nombre de las columnas
    writer= csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()
    Subject_ID = (subject_id)

    fila = {"Subject_ID": subject_id, "Screening day": screening_day, "Baseline visit": baseline_visit, "First Follow-up visit": date_required_1, "Second Follow-up visit": date_required_2, "Third Follow-up visit": date_required_3, "Fourth Follow-up visit": date_required_4}
    writer.writerow (fila)
    csvfile.close()

def calculate_visit (baseline_visit, date_required_1, date_required_2, date_required_3, date_requerid_4):
    visits = baseline_visit, date_required_1, date_required_2, date_required_3, date_requerid_4
    print (visits)

answear = input("Does the subject qualify for the trial? YES/NO: ") 
if answear == "YES": # Do this. 
    #Request the protocol number from the ones availables
    protocol_number = str(input("Please enter one of the following protocols : FTX-1432, CTF-1121, WSD-1421 "))
    print("The protocol number selected is:", protocol_number)
    
    
    if protocol_number == "FTX-1432":
    #Request the baseline visit & convert that into a date
        date_str= str(input("Please enter the Baseline visit mm/dd/yyyy: "))
        dates= ()
        baseline_visit = datetime.strptime(date_str, ("%m/%d/%Y"))
        print ("Baseline visit: ", baseline_visit)
        
        #Calculate the Follow-up visit 1 based on the day of the Baseline visit
        date_required_1 = baseline_visit + timedelta(days=35)
        print("First Follow-up visit: ", date_required_1)

        #Calculate the Follow-up visit 2 based on the day of the Baseline visit
        date_required_2 = baseline_visit + timedelta(days=70)
        print("Second Follow-up visit: ", date_required_2)
    
        #Calculate the Follow-up visit 3 based on the day of the Baseline visit
        date_required_3 = baseline_visit + timedelta(days=105)
        print("Third Follow-up visit: ", date_required_3)

        #Calculate the Follow-up visit 4 based on the day of the Baseline visit
        date_required_4 = baseline_visit + timedelta(days=140)
        print("Fourth Follow-up visit: ", date_required_4)
        #Acá agrego la funcion
        write_csv()

    elif protocol_number == "CFT-1121":
        #Request the baseline visit & convert that into a date
        date_str= str(input("Please enter the Baseline visit mm/dd/yyyy: "))
        baseline_visit = datetime.strptime(date_str, ("%m/%d/%Y"))
        print ("Baseline visit: ", baseline_visit)

        #Calculate the Follow-up visit 1 based on the day of the Baseline visit
        date_required_1 = baseline_visit + timedelta(days=12)
        print("First Follow-up visit: ", date_required_1)

        #Calculate the Follow-up visit 2 based on the day of the Baseline visit
        date_required_2 = baseline_visit + timedelta(days=24)
        print("Second Follow-up visit: ", date_required_2)
    
        #Calculate the Follow-up visit 3 based on the day of the Baseline visit
        date_required_3 = baseline_visit + timedelta(days=36)
        print("Third Follow-up visit: ", date_required_3)

        #Calculate the Follow-up visit 4 based on the day of the Baseline visit
        date_required_4 = baseline_visit + timedelta(days=48)
        print("Fourth Follow-up visit: ", date_required_4)
        #Acá agrego la funcion
        write_csv()

    elif protocol_number == "WSD-1421":
        #Request the baseline visit & convert that into a date
        date_str= str(input("Please enter the Baseline visit mm/dd/yyyy: "))
        baseline_visit = datetime.strptime(date_str, ("%m/%d/%Y"))
        print ("Baseline visit: ", baseline_visit)

        #Calculate the Follow-up visit 1 based on the day of the Baseline visit
        date_required_1 = baseline_visit + timedelta(days=56)
        print("First Follow-up visit: ", date_required_1)

        #Calculate the Follow-up visit 2 based on the day of the Baseline visit
        date_required_2 = baseline_visit + timedelta(days=112)
        print("Second Follow-up visit: ", date_required_2)
    
        #Calculate the Follow-up visit 3 based on the day of the Baseline visit
        date_required_3 = baseline_visit + timedelta(days=168)
        print("Third Follow-up visit: ", date_required_3)

        #Calculate the Follow-up visit 4 based on the day of the Baseline visit
        date_required_4 = baseline_visit + timedelta(days=224)
        print("Fourth Follow-up visit: ", date_required_4)
        write_csv()
    else:
        print ("The protocol number is incorrect or it is not saved into the system")

elif answear == "NO": # Do that. 
        print ("Subject does not qualify for this trial: subject is consider a screen failed")
else: 
    print("Please enter YES or NO.") 

def  write_csv():
#Abrir archivo para escritura
    csvfile = open("subjects_visits.csv","w")
    header = ["Subject_ID","Screening day", "Baseline visit", "First Follow-up visit", "Second Follow-up visit", "Third Follow-up visit", "Fourth Follow-up visit"]
    #Crear el objeto para escribir las lineas de archivo
    #basado en el nombre de las columnas
    writer= csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()
    Subject_ID = (subject_id)

    fila = {"Subject_ID": subject_id, "Screening day": screening_day, "Baseline visit": baseline_visit, "First Follow-up visit": date_required_1, "Second Follow-up visit": date_required_2, "Third Follow-up visit": date_required_3, "Fourth Follow-up visit": date_required_4}
    writer.writerow (fila)
    csvfile.close()

def write_csv():
    # Abrir archivo para escritura
    csvfile = open('Physician calendar.csv', 'w', newline='')

    # Detallar los nombres de las columnas
    header = ['Subject', 'Start date']
    # Crear el objeto para escribir las lineas de archivo
    # basado en los nombres de las columnas
    writer = csv.DictWriter(csvfile, fieldnames=header)

    Subject= 'subject_id'
    start_date = 'visits'

    writer.writeheader()
    fila = {'subject_id': Subject, 'visits': start_date}
    fila['subject_id'] = Subject
    writer.writerow(fila)
    writer.writerow({'suject_id': '', 'visits': 'start_Date'})

    csvfile.close()

#To be created: 
#subjects = 
   # {} # Visits from Subject 1
   # {} # Visitis from Subject 2

    if __name__ == '__main__':
        print("Welcome to Easy to schedule")
        calculate_visit ()
        write_csv()

#"""Based on Baseline visit the bucle would need to add x amount of days
#Check if that day is available in the pyshician calendar (csv)
#if follow_up1 not available
#elif baseline visit + 30 days (Beggining of the window)--- check availability at the calendar
#else baseline visit + 40 days (End of the window) --- check availability at the calendar
#        follow_up1 = date.today(baseline_visit) + timedelta(days=35)
#        print(Follow_up1)"""
#
#         date_required_1 = baseline_visit + timedelta(days=35)
#      print("First Follow-up visit: ", date_required_1)
#
#       #Calculate the Follow-up visit 2 based on the day of the Baseline visit
#       date_required_2 = baseline_visit + timedelta(days=70)
#       print("Second Follow-up visit: ", date_required_2)
#   
#       #Calculate the Follow-up visit 3 based on the day of the Baseline visit
#       date_required_3 = baseline_visit + timedelta(days=105)
#       print("Third Follow-up visit: ", date_required_3)
#
#       #Calculate the Follow-up visit 4 based on the day of the Baseline visit
#       date_required_4 = baseline_visit + timedelta(days=140)
#       print("Fourth Follow-up visit: ", date_required_4)
#       #Acá agrego la funcion