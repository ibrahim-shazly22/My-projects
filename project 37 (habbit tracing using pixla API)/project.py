import requests
from datetime import datetime as dt

TOKEN="oidjpjp2ijdpij2fpip00if2"
pixala_endpoint="https://pixe.la/v1/users"
GRAPH_ID="graph22"
USERNAME="ibrahim2001"

#---------------------------------------------creating user--------------------------------------
pixala_params={

    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixala_endpoint,json=pixala_params)
# print(response.text)
#-------------------------------------------crating graph----------------------------------------
header={
    "X-USER-TOKEN":TOKEN,
}
graph_endpoint=f"{pixala_endpoint}/{USERNAME}/graphs"

graph_params={
    "id":GRAPH_ID,
    "name":"cycling_graph",
    "unit":"KM",
    "type":"float",
    "color":"ajisai",
}
#-----------------------------------adding pixel------------------------------------------------
adding_pixel_endpoint=f"{pixala_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=dt.now()
adding_pixel_params={
    "date":today.strftime('%Y%m%d'),
    "quantity":input("how many km you achieve today? "),
}
response=requests.post(url=adding_pixel_endpoint,json=adding_pixel_params,headers=header)
print(response.text)

#-----------------------------------updating pixel------------------------------------------------
update_pixel_endpoint=f"{pixala_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params={
    "quantity":"4"
}
# response=requests.put(url=update_pixel_endpoint,json=update_params,headers=header)
# print(response.text)
#------------------------------------deleting pixel--------------------------------------------

deleting_pixel_endpoint=f"{pixala_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response=requests.delete(url=deleting_pixel_endpoint,headers=header)
# print(response.text)