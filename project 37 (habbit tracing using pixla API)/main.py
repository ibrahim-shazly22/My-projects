import requests
from datetime import datetime as dt
pixala_end_point="https://pixe.la/v1/users"
USERNAME="ibrahim2"
PIXALA_TOKEN="ljdjdpokdlkjdflakj"
GRAPH_ID="graph1"
DATE='today.strftime("%Y%m%d")'

#making a user @ pixala
user_params={
    "token":PIXALA_TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#crasting a graph
graph_endpoint=f"{pixala_end_point}/{USERNAME}/graphs"
graph_params={
    "id":GRAPH_ID,
    "name":"coding_graph",
    "unit":"hours",
    "type":"int",
    "color":"shibafu",
}
headers={
    "X-USER-TOKEN":PIXALA_TOKEN
}


#adding valuse to the graph
today=dt(year=2024,month=9,day=3)
posting_pixel_endpoint=f"{pixala_end_point}/{USERNAME}/graphs/{GRAPH_ID}"
posting_pixel_params={
    "date":today.strftime('%Y%m%d'),               #changing the format of the time to match api
    "quantity":"2",

}
#update a pixel
update_endpoint=f"{posting_pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params={
    "quantity":"3",

}
response=requests.put(url=update_endpoint,json=update_params,headers=headers)
print(response.text)