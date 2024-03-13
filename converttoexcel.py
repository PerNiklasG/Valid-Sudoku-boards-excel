import pandas as pd


# Define the path to your input text file containing the Sudoku board
input_file = r'C:\Users\nikgru\Downloads\sudoku_boards.txt'

# Read the Sudoku board from the text file
with open(input_file, 'r') as file:
    sudoku_board = [list(line.strip()) for line in file]

# Convert the Sudoku board to a Pandas DataFrame
df = pd.DataFrame(sudoku_board)

# Define the output Excel file name
output_file = 'sudoku_board2.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False, header=False)

print(f'Sudoku board has been successfully written to {output_file}.')