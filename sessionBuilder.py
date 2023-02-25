import csv

finalXML = ''

# Open the CSV file
with open('SecureCRT_Sessions.csv', 'r') as file:
    reader = csv.reader(file)

    # Create an empty list to hold the rows of data
    data = []

    # Iterate over each row in the CSV file
    for row in reader:
        # Append the row to the list of data
        data.append(row)


# Print the data to verify that it was read correctly
#print(data[1][1])


# Variable to hold a line of 
#lineData = []

# Outer Loop: Step through each line of the CSV
for outerData in data:
    folderTitle = outerData[0]
    currentStateAbbrv = str(folderTitle[0:2])
    jTS01 = outerData[1]
    jET01 = outerData[2]
    jFW01 = outerData[3]
    aTS01 = outerData[4]
    aET01 = outerData[5]
    aFW01 = outerData[6]

    siteIpList = outerData[1:]

    # open folder element
    finalXML = finalXML + '		<key name="' + folderTitle + '">\n'
    
    # Inner Loop 
    for deviceIP in siteIpList:
        octets = deviceIP.split('.')

        # set location based on 3rd octet
        if str(octets[2]) == '150':
            location = 'JFHQ'
        elif str(octets[2]) == '250':
            location = 'Alt'

        #set device type based on 4th octet
        if str(octets[3]) == '1':
            deviceType = 'TS01'
        elif str(octets[3]) == '10':
            deviceType = 'ET01'
        elif str(octets[3]) == '25':
            deviceType = 'FW01'
        
        description = currentStateAbbrv + ' ' + location + ' ' + deviceType
        
        sessionName = str(deviceIP) + ' - ' + currentStateAbbrv + ' ' + deviceType
        print(sessionName)

        with open('xml_profile_example.txt', 'r') as file:
            finalXML = finalXML + file.read().replace("{session_Name}", str(sessionName)).replace("{description}", description).replace("{hostname}", deviceIP)
            #.format(session_Name=sessionName, description=description, hostname=deviceIP)

#print(contents)



    # close folder element
    finalXML = finalXML +  '		</key>\n'

with open("SessionsFinal.txt", "w") as file:
    file.write(str(finalXML))