import pandas as pd
import json
import os


def read_data(file_path):

	"""Read in the json file"""

	# open the file
	f = open(file_path)

	# read the file as string
	f_str = f.read()

	# read the string back into json
	f_data = json.loads(f_str)

	return f_data


def get_chain(data):

	"""Get the name of the restaurant chain"""

	return data['chain_name']


def get_district(data):

	"""Get information about the district"""

	# get the district dictionary
	district = json.loads(data['district'])

	# get the name of the district in English
	district_name = district['name_en']

	# get district latitude
	district_latitude  = district['coordinates']['latitude']

	# get district longitude
	district_longitude = district['coordinates']['longitude']

	return district_name, district_latitude, district_longitude


if __name__ == "__main__":

	# define the output dataframe with necessary information as columns
	out = pd.DataFrame(
		[], 
		columns = 
		[
			'chain_name', 'district_name',
			'district_lat', 'district_long',
			'meal_type', 'meal_name', 'calories',
			'price', 'description', 'image'	
		]
	)

	# initialize indexing for the output CSV file
	idx = 0

	# for each file in the `data` directory
	for file in os.listdir('./data'):

		# if the file is in `json` format

		if '.json' in file:

			# try the following 
			try:

				# read the data in using the full path
				data = read_data('./data/'+ file)

				# get restaurant chain name
				chain_name = get_chain(data)

				# get district information
				district_name, district_lat, district_long = get_district(data)

				# load the vendor menu from data
				vendor_menu = json.loads(data['vendor_menu'])

				# for each menu item
				for menu in vendor_menu:

					# get meal type
					meal_type  = menu['name']

					# for each meal type item
					for item in menu['items']:

						# get meal name
						meal_name = item['name']

						# get meal calories
						calories  = item['calories']

						# get meal price
						price     = item['price']

						# get meal description
						describe  = item['description']

						# get meal image
						image     = item['image']

						# write the above info to the output dataframe using the index
						out.loc[idx,'chain_name']     = chain_name
						out.loc[idx, 'district_name'] = district_name
						out.loc[idx, 'district_lat']  = district_lat
						out.loc[idx, 'district_long'] = district_long
						out.loc[idx, 'meal_type']     = meal_type
						out.loc[idx, 'meal_name']     = meal_name
						out.loc[idx, 'calories']      = calories
						out.loc[idx, 'price']         = price
						out.loc[idx, 'description']   = describe
						out.loc[idx, 'image']         = image

						# save the output dataframe as a CSV
						out.to_csv('./data/consolidated_output.csv')

						# increment index for the next row
						idx += 1

			except:

				# in case of error continue to next item in iteration
				continue
