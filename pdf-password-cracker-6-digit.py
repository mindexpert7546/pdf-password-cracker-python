import PyPDF2

def nums_all_combinations_6_digit(pdf_loc):
    with open(pdf_loc, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        if pdf_reader.is_encrypted:
            nums = '0123456789'

            for i in nums:
                for j in nums:
                    for k in nums:
                        for l in nums:
                            for m in nums:
                                for n in nums:
                                    password = i + j + k + l + m + n
                                    print("Trying ...." + password)
                                    if pdf_reader.decrypt(password):
                                        print("Password Is : " + password)
                                        return
            print("Password not found after trying all combinations.")
        else:
            return "Pdf Has No Password"

print("PDF Password Cracker")

pdf_location = input("\nEnter the PDF Location : ").replace("%20", " ")

print("\n1) All Combinations of 6-digit Numbers")

choice = int(input("\nEnter Choice (1): "))

if choice == 1:
    print("\nAll Combinations of 6-digit Numbers")
    nums_all_combinations_6_digit(pdf_location)

else:
    print("\nEnter Valid Choice")
