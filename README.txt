For the template file, create the file exactly as you would like the final .desc file to look.
When creating the file, use the following delimiters for their coresponding replacements:
	[NAME]		"AWG *gauge* *color*"
	[COLOR]		*color*
 	[DIAMETER]	*diameter*
	[COLOR_CODE]	*color code*
	[GAUGE]		*gauge*
	[GAUGE_NAME]	AWG_*gauge*_*color*
	[COLOR_ABV]	*color abreviation* (all caps)
	["COLOR_ABV"]	"*color abreviation*" (all caps)

Open wire_descriptor_generator.py in a text editor and read the comments to properly setup the 
output directory for the descriptor files using the master_folder variable.

To execute the program, first be sure that the python 3.6 or higher is installed and than open
a Command Prompt in the directory of wire_descriptor_generator.py and type:
	python ./wire_descriptor_generator.py