import json
import requests
import unittest
import logging

class TestCaseUnit(unittest.TestCase):

#Add single user
  def test_addSingleUser(self):

    addSingleUser_response=requests.post("https://petstore.swagger.io/v2/user",json={
      "id": 111,
      "username": "jdsn1",
      "firstName": "pavan",
      "lastName": "dev1",
      "email": "jdsn1@gmail.com",
      "password": "pavanpass",
      "phone": "04564554551",
      "userStatus": 1
    },headers={"Accept":"application/json","Content-Type":"application/json","Name":"api_key",'Value':"apivalue"},)
    print(addSingleUser_response.json())
    logger=logging.getLogger('adduser')
    logger.setLevel(logging.DEBUG)
    #print(addSingleUser_response.headers)
    assert addSingleUser_response.json()['code']==200

  def test_addMultipleUser(self):
    #Add multiple users
    addMultipleUser_response=requests.post("https://petstore.swagger.io/v2/user/createWithList",json=[
        {
            "id": 2,
            "username": "jdsn2",
            "firstName": "pavan2",
            "lastName": "dev2",
            "email": "jdsn2@gmail.com",
            "password": "pavan2pass",
            "phone": "04564554552",
            "userStatus": 1
        },
        {
            "id": 3,
            "username": "jdsn3",
            "firstName": "pavan3",
            "lastName": "dev3",
            "email": "jdsn3@gmail.com",
            "password": "pavan3pass",
            "phone": "04564554553",
            "userStatus": 1
        },
        {
            "id": 3,
            "username": "jdsn3",
            "firstName": "pavan4",
            "lastName": "dev3",
            "email": "jdsn3@gmail.com",
            "password": "pavan4pass",
            "phone": "04564554553",
            "userStatus": 1
        }
    ],headers={"Accept":"application/json","Content-Type":"application/json"})
    print(addMultipleUser_response.json())
    logger = logging.getLogger('adduser')
    logger.setLevel(logging.DEBUG)
    #print(addMultipleUser_response.headers)
    assert addMultipleUser_response.json()['code']==200

  def test_getUserLogin(self):
    #Get Logs user into the system
    response_logsUser=requests.get("https://petstore.swagger.io/v2/user/login",params={"username":"pavan2","password":"pavan2"},headers={"Accept":"application/json"},)
    assert response_logsUser.status_code==200
    logger = logging.getLogger('adduser')
    logger.setLevel(logging.DEBUG)
    print(response_logsUser.json())
    #print(response_logsUser.headers)

  def test_getUserLogout(self):
    #Get Logs out current logged in user session
    response_logsoutUser=requests.get("https://petstore.swagger.io/v2/user/logout",headers={"Accept":"application/json"},)
    assert response_logsoutUser.status_code==200
    logger = logging.getLogger('adduser')
    logger.setLevel(logging.DEBUG)
    print(response_logsoutUser.json())
    #print(response_logsoutUser.headers)

  def test_getUser(self):
    #Get user detail
    response_get=requests.get("https://petstore.swagger.io/v2/user/jdsn3",)
    assert response_get.status_code==200
    logger = logging.getLogger('getuser')
    logger.setLevel(logging.DEBUG)
    print(response_get.json())
    #print(response_get.headers)


  def test_deleteUser(self):
    #Delete user
    response_delete=requests.delete("https://petstore.swagger.io/v2/user/jdsn1",headers={"Accept":"application/json"},)
    assert response_delete.status_code==200
    logger = logging.getLogger('delete')
    logger.setLevel(logging.DEBUG)
    print(response_delete.json())
    #print(response_delete.headers)

  def test_modifiy(self):
    #modify user
    response_modify=requests.put("https://petstore.swagger.io/v2/user/jdsn2",json={
      "id": 2,
      "username": "jdsn2",
      "firstName": "janardan2updated",
      "lastName": "dev2updated",
      "email": "jdsn2@gmail.com",
      "password": "janardandev2",
      "phone": "04564554552",
      "userStatus": 1},headers={"Accept":"application/json","Content-Type":"application/json"},)
    assert response_modify.status_code==200
    logger = logging.getLogger('modify')
    logger.setLevel(logging.DEBUG)
    print(response_modify.json())
    #print(response_modify.headers)




