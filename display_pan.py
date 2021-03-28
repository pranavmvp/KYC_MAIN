from difflib import SequenceMatcher

def similar(a, b):
    a=sorted(a.lower())
    b=sorted(b.lower())
    return SequenceMatcher(None, a, b).ratio()

def display_pan(passed_values, input_values):
    print('\n********************')
    print('PAN COMPARISON')
    print('********************\n')
    print('Input Name : ',passed_values['Name'], '\n')
    print('Document Name : ',input_values['Name'], '\n')
    print('Input DOB - ',passed_values['DOB'],'\n')
    print('Document DOB - ',input_values['DOB'], '\n')

    a = input_values['Name']
    b = passed_values['Name']

    if a in b or b in a or similar(a,b)>0.8:
        print("PAN Name Matched", similar(a,b))
    else:
        print("PAN Name Not Matched", similar(a,b))

    a = input_values['DOB']
    b = passed_values['DOB']

    if a in b or b in a or similar(a,b)>0.75:
        print("PAN DOB Matched", similar(a,b))
    else:
        print("PAN DOB Not Matched", similar(a,b))
