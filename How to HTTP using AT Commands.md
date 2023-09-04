---
publish: true
review-frequency: normal
---
2022-02-28-Mo
Type:: #documentation 
Tags:: [[UBlox]], [[SARA-R5]], [[HTTP]], [[AT Commands]], [[Performance]]

# How to HTTP using AT Commands
Supported methods are:
- HEAD
- GET
- DELETE
- PUT
- POST

# Setup File in FS for HTTP methods Input/Output
The UHTTP AT commands require the http input/output data to be passed in via files
```
"AT+ULSTFILE=1",  # Get total free size in FS
"AT+ULSTFILE=0",  # List files
"AT+ULSTFILE=2,\"post_data\"",  # List files
"AT+UDELFILE=\"post_data\"",    # Delete file
"AT+UDWNFILE=\"post_data\",15", # Create a new file
> .... Insert 15 bytes of data ....
"AT+URDFILE=\"post_data\"",     # Read back the data, the returned data is not all unicode
# b'+URDFILE: "post_data",15,";\xa3s\xa9Fw7\x1e\x86\x93\xd7p\xf9\xddP"\r\n'
```

# Setup profile ID for each HTTP operation
```
"AT+UHTTP=0,1,\"echo-ln2he653pq-ue.a.run.app\"", # Setting server name
"AT+UHTTP=0,6,1" # Enable HTTPS
```

# HTTP Post method
Post method can be issue via with input from a file or data over AT command, these are different `AT+UHTTPC`
```
"AT+UHTTPC=0,4,"/","post_result","post_data",4" # Send input data via file
"AT+UHTTPC=0,5,"/","post_result","1234567890",4" # Send input data on AT Command
```

This is async command, where there HTTP request result is returned via UUHTTPCR.

#  UUHTTPCR
URC message to notify

Wait for `UUHTTPCR` message in a loop, which should indicate a http response is received.
```
1646100369.3612921: b'+UUHTTPCR: 2,4,1\r\n'
======AT+URDFILE="post_result"=======
1646100369.373533: b'\r\n'
1646100369.3743281: b'+URDFILE: "post_result",395,"HTTP/1.0 200 OK\r\n'
1646100369.3792121: b'Content-Type: text/html; charset=utf-8\r\n'
1646100369.384853: b'X-Cloud-Trace-Context: ad4978328e06624489f283625fa6d33d;o=1\r\n'
1646100369.385688: b'Date: Tue, 01 Mar 2022 02:06:08 GMT\r\n'
1646100369.389964: b'Server: Google Frontend\r\n'
1646100369.3902478: b'Content-Length: 20\r\n'
1646100369.416528: b'Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"\r\n'
1646100369.4166038: b'\r\n'
1646100369.4169862: b'\x08Q6\xc5\xa9\x9cb\xea\x03\xed\xcd\x94\xecg\xc2\xd1\x10\xbfE\x1c"\r\n'
1646100369.417081: b'OK\r\n'
======AT+UDELFILE="post_result"=======
1646100370.742423: b'\r\n'
1646100370.7425768: b'OK\r\n'
======AT+UHTTPER=2=======
1646100371.7646499: b'\r\n'
1646100371.764836: b'+UHTTPER: 2,10,0\r\n'
1646100371.764864: b'\r\n'
1646100371.764906: b'OK\r\n'
```

# TLS
```
"AT+USECPRF=2,0,0",
"AT+USECPRF=2,1,0",
"AT+USECPRF=2,2",
"AT+USECPRF=2,3,\"ubx_verisign_universal_root_certification_authority\"",
"AT+USECPRF=2,3",
```


---
# References
- SARA-R5 AT Commands UBX-19047455