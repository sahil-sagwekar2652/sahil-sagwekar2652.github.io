Title: Create an HTTP server in Python
Date: 2023-03-29 12:19
Author: Sahil Sagwekar
Slug: create-an-http-server-in-python

Introduction {#heading-introduction}
------------

Whenever we hear the word server, an image of a big bulky computer with lots of cables and no display pops up in our mind. But technically any computer can be a server. A server is just a computer that is 'serving' accessible data on a network.

In this blog post, we will learn how to create a simple HTTP server in Python.

How does a server work? {#heading-how-does-a-server-work}
-----------------------

![Spider Man How Does That Work Exactly GIF - Spider Man How Does That Work Exactly How Does It Work GIFs](https://media.tenor.com/W7C6o9zgj_QAAAAC/spider-man-how-does-that-work-exactly.gif){.image--center .mx-auto}

A server works by listening on a specific port for incoming connections from clients. Generally, multiple services which all connect to the Internet are running simultaneously on a server. In simple terms, the port number is used to identify the service to which the request is being made. For example, port 80 is usually used for HTTP (HyperText Transfer Protocol), which is the protocol for web communication.

![alt](https://cdn.hashnode.com/res/hashnode/image/upload/v1680070124220/7fc9b86b-45ff-4499-9e0b-f527452e5138.png){.image--center .mx-auto}

When a client connects to a server on a port, the server accepts the connection and creates a socket, which is an endpoint for communication between the two parties. The client and the server then exchange messages using the protocol of the service. For example, for HTTP, the client sends an HTTP request message, which contains information such as the method (GET, POST, etc.), the path (the URL of the resource), and the headers (additional information). The server then processes the request and sends back an [HTTP response message](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), which contains information such as the status code (200 OK, 404 Not Found, etc.), the headers, and the body (the content of the resource).

How to create a server using the http.server module in Python? {#heading-how-to-create-a-server-using-the-httpserver-module-in-python}
--------------------------------------------------------------

### Method 1 {#heading-method-1}

This is the fastest way to get your server up and running and also to local data to other devices on your local network.
To achieve this we run the following command:
```bash
python -m http.server
# Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```
This command will host the contents of the current directory on localhost i.e. 127.0.0.1 and default port 8000.

![That Was Fast GIF - Fast GIFs](https://media.tenor.com/stcVUHuVy5IAAAAS/fast.gif){.image--center .mx-auto}

We can also access the server from another device that is connected to the same network as our server device. To do this, we need to find out the IP address of our server device. For example, on Windows, we can use the `ipconfig` command in a command prompt, and on Linux or macOS, we can use the `ifconfig` command in a terminal. We need to note down the IP address that is shown for our network adapter.
```bash
python -m http.server --bind <local-ip-addr> <port-number>python -m http.server --bind 192.168.1.206 9999
# Serving HTTP on 192.168.1.206 port 9999 (http://192.168.1.206:9999/) ...
```
The above command will host the content of the current directory on the <http://192.168.1.206:9999/> URL and will be accessible to all the devices on the local network.

### Method 2 {#heading-method-2}

To create a slightly more customized server using Python, we can use the built-in http.server module. This module provides classes for handling HTTP requests and responses. We can use the `HTTPServer` class to create a server object, and the `BaseHTTPRequestHandler` class to define how to handle requests.

To use the http.server module, we need to import it into our Python script. Then, we need to create a subclass of `BaseHTTPRequestHandler` and override the `do_GET` method. This method is called when the server receives a [GET request](http://www.devdoc.net/web/developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET.html#:~:text=The%20HTTP%20GET%20method%20requests%20a%20representation%20of,GET%20should%20only%20retrieve%20data.%20Syntax%20GET%20%2Findex.html) from a client. We can write our logic for handling the request inside this method. For example, we can send back some HTML code to display on the client's browser.

Next, we need to create an instance of HTTPServer and pass it two arguments: a tuple of an empty string and a port number, and our handler class. The empty string means that the server will listen on all available IP addresses, and the port number is the port where the server will run. We can choose any port number that is not already in use by another program. Finally, we need to call the serve\_forever method on the server object to start the server.

Here is an example of how to create a simple HTTP server in Python:
```python
# Import the http.server module
import http.server

# Create a subclass of BaseHTTPRequestHandler
class MyHandler(http.server.BaseHTTPRequestHandler):

# Override the do_GET method
def do_GET(self):
    # Send a 200 OK response
    self.send_response(200)
    # Send headers
    self.send_header("Content-type", "text/html")
    self.end_headers()
    # Write some HTML code
    self.wfile.write(b"<h1>Hello from Python!</h1>")

# Create an instance of HTTPServer
server = http.server.HTTPServer(("", 8000), MyHandler)

# Start the server
server.serve_forever()
```
To run this script, we need to save it as a .py file and execute it in a terminal or command prompt. For example, if we save it as [server.py](http://server.py), we can run it with:
```bash
python server.py
```
This will start the server on port 8000. To access the server from a web browser, we need to enter the URL <http://localhost:8000> or <http://127.0.0.1:8000>. This will display the HTML code that we wrote in the do\_GET method. If we enter the IP address of the server then, we can enter the URL http://\<ip\_address\>:8000 in a web browser on another device, where \<ip\_address\> is the IP address of our server device. This is how we can create a simple HTTP server in Python using http.server module. We can customize our handler class to handle different types of requests and send different types of responses.

### Testing the output {#heading-testing-the-output}

You can test the output by simply opening the link on you browser or by using curl, which is a command line program to make a request to the server from the command line.
```bash
# e.g.
curl http://0.0.0.0:8000/
# curl http://<ip_address>:<port_number>
```
