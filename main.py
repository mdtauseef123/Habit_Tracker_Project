import requests
from datetime import datetime

USERNAME = "mdtauseef123"
TOKEN = "armaan786"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.text is just used to give the post request is successfull or not by providing the message.
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hrs",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

"""
In order to view the graph in the browser just type the following link:-
https://pixe.la/v1/users/{user_name}/graphs/{id_name}.html
which in our case will be:-
https://pixe.la/v1/users/mdtauseef123/graphs/graph1.html
"""
# Posting the data of each day in graph
post_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
"""
Since it will be a tough for us to change the current date in date parameters we will be using datetime module and we
will tap into now() in order to get current date. But there is a problem with this as the date return in the format
is (2022-10-09 17:07:23.153381) not accepted in date parameter so we have to format that date using strftime().
We can also use datetime as today = datetime(year=2022, month=7, day=23).
"""
today = datetime.now()
post_graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}
response = requests.post(url=post_graph_endpoint, json=post_graph_config, headers=headers)
print(response.text)


# Updating the pixel of a particular date
pixel_update_endpoint = f"{post_graph_endpoint}/20221008"
pixel_update_config = {
    "quantity": "15"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

# Deleting the pixel of a particular date
# delete_pixel_endpoint = f"{post_graph_endpoint}/20221008"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)


"""
Sites required in making the above project are the following:- 
1.https://pixe.la/(Pixel Website)
2.https://docs.pixe.la/(Pixel API Documentation)
3.https://www.w3schools.com/python/python_datetime.asp(strftime() description)
4.https://requests.readthedocs.io/en/latest/api/(requests module description)
"""


"""
Sometimes the requests says:- 
503 Service Unavailable
This error occurs when Pixela is temporarily unavailable. Please take a moment and retry your request.
If the response body contains "isRejected":true, it indicates that the request was rejected 25% of the time. 
In this case, the request can be retried until it succeeds.
You can avoid this rejection by becoming a Pixela supporter. See this page for more information.
"""
