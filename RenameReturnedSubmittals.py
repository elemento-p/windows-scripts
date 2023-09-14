import glob, os
import pandas as pd

working_directory = 'C:\\Rename_Files'
master_sheet = r'X:\Engineering\1.2.2022 ORDER FOLDER\78903 - Wood - Conoco Willow Hamm - DS\Submittals\2) Client\Fusion Status\1) Master List.xlsx'
os.chdir(working_directory)

# Get lis of PDF's in the folder
pdf_list = glob.glob('*.pdf')
# print(pdf_list)

# Strip the file extension from the file list
file_name_list = []
for file in pdf_list:
    file_name_list.append(file[:-4])
    
# print(file_name_list)

# Get list with pdf files with extension and column with no extension
df = pd.DataFrame(list(zip(pdf_list, file_name_list)), columns = ['Original File Name', 'Reference'])

# read in master spreadsheet that has current documentation status
df2 = pd.read_excel(master_sheet, sheet_name = 'Sheet1')

# Merge df based on file list and drop extra columns not needed from Master Sheet
df = pd.merge(df, df2, how = 'left', left_on = 'Reference', right_on = 'Reference').drop(['Vendor Reference Number',
    'Title','Revision Date','PM Status','Forecast Submission Date','Actual Submission Date','Planned Resubmission Date',
    'Forecast Resubmission Date','Actual Resubmission Date','Planned Return Date','Actual Return Date','Decision Code2'
    ], axis = 1)

# extract number from decision code and make new column with number
df['Code'] = df['Decision Code'].str.extract('(\d+)', expand=False)
df['New File Name'] = df['Reference'] + '_R' + df['Revision'] + '_C' + df['Code'] + '.pdf'

# Rename files
for index, row in df.iterrows():
    old_filename = row['Original File Name']
    new_filename = row['New File Name']
    
    os.rename(old_filename, new_filename)
    
# write to csv file
df.to_csv('file_list.csv', index = False)

print(df)
