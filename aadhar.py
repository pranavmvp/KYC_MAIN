import pytesseract

def aadhar_check(img):
    text = pytesseract.image_to_string(img)
    i=0

    MAIN_LINES=[]

    addr_Index=[]
    s = ''
    dob_s = ''

    for line in text.splitlines() :

        if ((line=='') or (line==' ') or (line=='  ') or (line=='   ')):
            continue
        else:
            MAIN_LINES.append(line)
            #print(i,' ',line)
        i+=1

    #print(MAIN_LINES)

    for i in range(len(MAIN_LINES)):
        if (MAIN_LINES[i]=='To' or MAIN_LINES[i]=='To,'):
            name_index = i+2
            dad_index = i+3

            addr_Index.append(i+4)
            addr_Index.append(i+5)
            addr_Index.append(i+6)
            addr_Index.append(i+7)
            addr_Index.append(i+8)

            ph_index = i+9

        if('DOB' in MAIN_LINES[i]):
                dob_s = MAIN_LINES[i][-10:]

    for x in addr_Index:
        s = s + MAIN_LINES[x]
        s = s + '\n'

    #print('\n')
    #print('Name ', MAIN_LINES[name_index])
    #print(MAIN_LINES[dad_index])
    #print('Address \n')
    #print(s)
    #print('Phone: ', MAIN_LINES[ph_index])
    #print('DOB:',dob_s)

    aadhar_values = {
            'Name' : MAIN_LINES[name_index],
            'Address' : s,
            'Daddy' : MAIN_LINES[dad_index],
            'Phone' : MAIN_LINES[ph_index],
            'DOB' : dob_s
        }

    return aadhar_values
