#import all necessary files
import os
import csv
import glob
import datetime

#import csv file employee_data1.csv
#Read all csv file in a folder
filepath = os.path.join("employee_data1.csv")

x = 1

print (filepath)


#iterate through each file and create seperate folder that will store and output end results
for filename in filepath:

       

        x += 1
        outputpath = os.path.join('results', 'results_of_file_' + str(x) + '.csv')

        with open(filename, 'r', newline ='') as csvfile, 
        open(outputpath, 'w', newline = '' ) as matched:
            csvreader = csv.reader(csvfile, delimeter=',')
            csvwriter = csv.writer(csvfile, delimeter=',')

            #Move to the next row getting rid of the first heading
            header = next(csvreader)


            #copy and paste US state and its abbreviations
            us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}

    #initializing all variables
    empId = []
    firstName = []
    lastName = []
    dateOfBirth = []
    ssn = []
    state = []

for line in csvreade:

    empID.append(line[0]) 
            # Create a list of lists with [FirstName, LastName]
            fullName = line[1].split(' ') 
             # Add first name which is [0]
            firstName.append(fullName[0])
             # And second name [1]
            lastName.append(fullName[1])

            # Change a date format and append it to a list
            date = datetime.datetime.strptime(line[2], '%Y-%m-%d').strftime('%d/%m/%Y')
            dateOfBirth.append(date)

            # I don't like this, planning to rework
            numb = line[3]
            ssn.append('***-**-' + str(numb[-4:]))
            
            statename = line[4]
            # Check if state is in our dictionary
            if statename in us_state: 
                # If yes, append the value
                state.append(us_state[statename]) 
            else: # If not.. just not. We need to add anything anyway.
                state.append('This is not yet the US state')

        answer = zip(empID, firstName, lastName, dateOfBirth, ssn, state)

        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        csvwriter.writerows(answer)
    
print('Finished')



 
    


