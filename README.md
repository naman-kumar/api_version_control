# How to do a API version control through url arguments

In this sample code i have tried to show how we can control the api version through url arguments.

The decorator api_version_control takes a key and value arguments. Key is the version and value is the respective fuction which will be called for that particular version. The major and minor version is seperated by underscore ( _ ) in the key field. If we have to pass any argument to the function then value becomes tuple in which first index value is the function object and rest other indexes can be used as argument to the function.

Once we run the web app we can see that we will get different output for different version and if we don't pass any version then the actual method will be executed.

**For example:**
If we don't pass any version details then it executes the index() method which return Hello world!
``` 
$ curl http://127.0.0.1:5000/
Hello world!
```
If we pass v=v1 as parameter argument then it will executes the method api_v1() which returns "This is api version v1"
```
$ curl http://127.0.0.1:5000/?v=v1
This is api version v1
```
If we pass v=v1_1 as parameter argument then it will executes the method api_v1_1() which returns "This is api version v1_1"
* Note:- major and minor version number is seperated with underscode ( _ ).
```
curl http://127.0.0.1:5000/?v=v1_1
This is api version v1_1
```
```
$ curl http://127.0.0.1:5000/?v=v1_2
This is api version v1_2
```
```
curl http://127.0.0.1:5000/?v=v2
Hello world from api version v2
```
```
$ curl http://127.0.0.1:5000/?v=v3
This is api version v3
```
```
$ curl http://127.0.0.1:5000/?v=v4
This is api version v4
```
If we pass the wrong version number as argument then it will return 404.
```
$ curl http://127.0.0.1:5000/?v=v5
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```
