import sys
import os
from pathlib import Path
from os import listdir

# master_folder is the output path to the directory for the generated files
# example: "C:/Users/firstname.lastname/Documents/New_Descriptor_Files/"
# change the master_folder string depending on where you would like to ouput the files
master_folder = 'C:/Users/firstname.lastname/Documents/New_Descriptor_Files/'

# color, color_abv, color_ABV, and color_code are all arrays that must have the same length
# color is a list of strings pertaining to each color of wire to be generated
color = ['Black', 'Blue', 'Brown', 'Gray', 'Green', 'Red', 'White', 'Yellow']

# color_abv is a list of strings pertaining to the abreviation of each of the above colors
# each color abreviation in color_abv must have the same index as the coresponding color it represents in the color array
# example: color[0] = 'Black'; therefore, the abreviation 'blk' must be in index 0: color_abv[0] = 'blk'
color_abv = ['blk', 'blue', 'brn', 'gry', 'grn', 'red', 'wht', 'ylw']

# color_ABV is a list of strings pertaining to the capitalized abreviation of each of the above colors
# color_ABV follows the same indexing rules as color_abv above
color_ABV = ['BLK', 'BLU', 'BRN', 'GRY', 'GRN', 'RED', 'WHT', 'YLW']

# color_code is a list of numeric codes pertaining to each of the above colors
# as with both color_abv, and color_ABV, each code must share the same index as its coresponding color
color_code = [216, 134, 125, 87, 36, 186, 44, 6]

# gauge, gauge_str, and diameter are all arrays that must have the same length
# gauge is a list of strings pertaining to each gauge of wire to be generated
gauge = ['4/0', '3/0', '2/0', '1/0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24']

# gauge_list is a list of strings pertaining to each gauge of wire to be generated
# guage_str has a different format than the above gauge list
# gauges such as 4/0 and 3/0 are represented as 0000 and 000 respectively
# gauges such as 2 and 6 are represented as 02 and 06 respectively
# each gauge_str element must share the same index as its coresponding gauge element
gauge_str = ['0000', '000', '00', '0', '02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24']

# diameter is a list of strings pertaining to the diamter of each gauge in inches
# each diameter element must share the same index as its coresponding gauge and gauge_str element
diameter = [0.46, 0.41, 0.365, 0.325, 0.258, 0.204, 0.162, 0.129, 0.102, 0.0808, 0.0641, 0.0508, 0.0403, 0.032, 0.0254, 0.0201]

# the following statements check for any errors in list length
has_error = False

if(len(color) != len(color_ABV)):
    print('Error: color_ABV does not have the correct number of arguments')
    has_error = True

if(len(color) != len(color_code)):
    print('Error: color_code does not have the correct number of arguments')
    has_error = True

if(len(gauge) != len(gauge_str)):
    print('Error: gauge_str does not have the correct number of arguments')
    has_error = True

if(len(gauge) != len(diameter)):
    print('Error: diameter does not have the correct number of arguments')
    has_error = True

if(has_error == True):
    sys.exit()

# template_file is the file name for the template used to generate the descriptor files
# template.txt is the default but can be changed as needed
# if the template file is not in the same directory as this python script, add the full path before the file name
# example: 'C:/Users/firstname.lastname/Documents/template.txt'
template_file = 'template.txt'

for i in range(len(color)):
    for j in range(len(gauge)):
        # file_path takes the master_folder and adds a subfolder for each color
        file_path = master_folder + color[i] + '/'
        # file_name generates the file name in the following format:
        # awg-[gauge-str]-[color_abv].desc
        file_name = 'awg-' + gauge_str[j] + '-' + color_abv[i] + '.desc'
        # if the path for the current wire color doesn't exist, it will be created here
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        # the template file is opened so that it can be used to generate the .desc file    
        template = open(template_file, 'r')
        # the following code parses the file and replaces each delimiter with the necesary text
        # the new text for the .desc file is stored in memory before it is written to the output file
        data = template.read()
        data = data.replace('[NAME]', '"AWG ' + gauge[j] + ' ' + color[i] + '"')
        data = data.replace('[COLOR]', color[i])
        data = data.replace('[DIAMETER]', str(diameter[j]))
        data = data.replace('[COLOR_CODE]', str(color_code[i]))
        data = data.replace('[GAUGE]', gauge[j])
        data = data.replace('[GAUGE_NAME]', 'AWG_' + gauge[j] + '_' + color[i])
        data = data.replace('[COLOR_ABV]', color_ABV[i])
        data = data.replace('["COLOR_ABV"]', '"' + color_ABV[i] + '"')
        # file is used to generate the .desc file and write the necessary information to it from memory before it is saved and closed
        file = open(file_path + file_name, 'a')
        file.write(data)
        file.close()
        # the template file must be closed and reopened with each loop so that it can be read from the beginning again
        template.close()