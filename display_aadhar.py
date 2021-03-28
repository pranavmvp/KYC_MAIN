from difflib import SequenceMatcher

def similar(a, b):
    a=sorted(a.lower())
    b=sorted(b.lower())
    return SequenceMatcher(None, a, b).ratio()

def display_aadhar(passed_values, input_values):
    print('\n********************')
    print('AADHAR COMPARISON')
    print('********************\n')
    print('Input Name : ',passed_values['Name'], '\n')
    print('Document Name : ',input_values['Name'], '\n')
    print('Input DOB - ',passed_values['DOB'],'\n')
    print('Document DOB - ',input_values['DOB'], '\n')
    print('Input Address - ','\n',passed_values['Address'],'\n')
    print('Document Address - ','\n',input_values['Address'])

    a = input_values['Name']
    b = passed_values['Name']

    if a in b or b in a or similar(a,b)>0.8:
        print("AADHAR Name Matched", similar(a,b))
    else:
        print("AADHAR Name Not Matched", similar(a,b))

    a = input_values['DOB']
    b = passed_values['DOB']

    if a in b or b in a or similar(a,b)>0.75:
        print("AADHAR DOB Matched", similar(a,b))
    else:
        print("AADHAR DOB Not Matched", similar(a,b))

    a = input_values['Address']
    b = passed_values['Address']

    if a in b or b in a or similar(a,b)>=0.65:
        print("AADHAR Addr Matched", similar(a,b))
    else:
        print("AADHAR Addr Not Matched", similar(a,b))
