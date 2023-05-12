# Importing the datetime module to work with date and time data
import datetime

# Setting the values for the user's username, token, and graph ID
USERNAME = 'dennis21ss3445'
TOKEN = 'damiodoadasdok3d2d2'
GRAPH_ID = 'graph1'

# Setting the endpoint URL for the Pixela API
pixela_endpoint = 'https://pixe.la/v1/users'

# Creating the dictionary with the user's information and parameters for the API call
users_param = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# -----------------------Sending an HTTP POST request to create a new user on the Pixela API (commented out)--------------------
# response = requests.post(pixela_endpoint, json=users_param)
# print(response.text)

# Setting the endpoint URL for creating a new graph on the Pixela API
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Creating the dictionary with the configuration data for the new graph
graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'ajisai'
}

# Creating the dictionary with the headers for the HTTP request
headers = {
    'X-USER-TOKEN': TOKEN
}

# -----------------------Sending an HTTP POST request to create a new graph on the Pixela API (commented out)-----------------------
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Setting the endpoint URL for adding a new pixel (data point) to the graph
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

# Getting the current date and time
today = datetime.datetime.now()

# Converting the date to a string in the format expected by the API
TIME = today.strftime("%Y%m%d")

# Creating the dictionary with the data for the new pixel
pixel_data = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '10',
}

#--------------------- Sending an HTTP POST request to add a new pixel to the graph (commented out)--------------------------------
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Setting the endpoint URL for updating an existing pixel on the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TIME}"

# Creating the dictionary with the updated data for the pixel
new_pixel_data = {
    'quantity': '11'
}

#-------------------------------- Sending an HTTP PUT request to update an existing pixel on the graph (commented out)----------------------
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Setting the endpoint URL for deleting an existing pixel on the graph
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TIME}"

# ------------------------Sending an HTTP DELETE request to delete an existing pixel on the graph (commented out)---------------------------
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
