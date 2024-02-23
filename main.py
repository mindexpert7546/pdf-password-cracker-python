import PyPDF2
import random

def generate_password():
    nums = '0123456789'

    # Generate 4-digit number password
    password = ''
    for _ in range(4):
        password += nums[random.randint(0, len(nums)-1)]

    return password

def nums_4_digit(pdf_loc):
    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        if pdf_reader.is_encrypted:
            for _ in range(10000):  # You can adjust the number of attempts as needed
                password = generate_password()
                print("Trying ...." + password)
                if pdf_reader.decrypt(password):
                    print("Password Is : " + password)
                    return
            print("Password not found after trying all combinations.")
        else:
            return "Pdf Has No Password"

print("PDF Password Cracker")

pdf_location = input("\nEnter the PDF Location : ").replace("%20", " ")


print("\n1) 4-digit Numbers")

choice = int(input("\nEnter Choice (1): "))

if choice == 1:
    print("\n4-digit Numbers")
    nums_4_digit(pdf_location)

else:
    print("\nEnter Valid Choice")
