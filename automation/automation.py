import re

def get_emails(file):
    email_pattern = r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]+"
    emails = []

    #find email addresses
    with open(file,'r') as file:
        file = file.read()
        emails_found = re.findall(email_pattern, file)

    #prevent repetition
    for email in emails_found:
        if email not in emails:
            emails.append(email) 

    #sort emails and write them to the file   
    with open('emails.txt','w') as output_file:
        for email in sorted(emails):
            output_file.write(f"{str(email)}\n")

    return emails


def format_phone_number(phone_number):
    """
    This function re-formats the phone number to XXX-YYY-ZZZZ 
    """

    if len(phone_number) == 7:
        phone_number = f"206{phone_number}"
    if "." in phone_number:
        phone_number = phone_number.replace(".", "")
    if "(" in phone_number:
        phone_number = phone_number.replace("(", "")
    if ")" in phone_number:
        phone_number = phone_number.replace(")", "")
    if "-" in phone_number:
        phone_number = phone_number.replace("-", "")
    phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"

    return phone_number
         

def get_phone_numbers(file):
    phone_number_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    
    #finds phone numbers
    with open(file,'r') as file:
        file = file.read()
        phone_numbers = re.findall(phone_number_pattern, file)

    #sorts and writes the formatted phone numbers to a file
    with open('phone_numbers.txt','w') as output_file:
        clean_phone_numbers = []
  
        for phone_number in phone_numbers:
            phone_number = format_phone_number(phone_number) 
            clean_phone_numbers.append(phone_number)
        
        for phone_number in sorted(clean_phone_numbers):
            output_file.write(f"{phone_number}\n")

    return clean_phone_numbers


if __name__ == "__main__":
    print("Emails: \n", get_emails("./potential-contacts.txt"))
    print("Phone Numbers: \n", get_phone_numbers("./potential-contacts.txt"))


