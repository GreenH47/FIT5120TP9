import random
import openpyxl

# Define the possible values for the "plans" column
possible_values = ["Reduce", "Reuse", "Recycle"]

# Open the workbook
workbook = openpyxl.load_workbook("waste_information.xlsx")

# Select the "waste" sheet
sheet = workbook["waste"]

# Iterate over the rows starting from row 2
for row in sheet.iter_rows(min_row=2, max_row=24, min_col=6, max_col=6):
    # Generate a random number of items (between 1 and 3)
    num_items = random.randint(1, 3)

    # Select random values from the possible_values list
    random_values = random.sample(possible_values, num_items)

    # Convert the random values to a single string separated by "; "
    plans = "; ".join(random_values)

    # Assign the generated plans to the cell in the "plans" column
    row[0].value = plans

# Save the changes to the workbook
workbook.save("waste_information.xlsx")
