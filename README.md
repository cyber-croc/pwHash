<h1 align="center">
  <br>
  <a href="https://github.com/cyber-croc/pwHash"><img src="https://i.imgur.com/Y2qa0Hq.jpg" width="200px height="200px""></a>
  <br>
  pwHash
  <br>
</h1>

<h4 align="center">Simple Password Hash Generator</h4>

### Installation
```
>> git clone https://github.com/cyber-croc/pwHash.git

>> cd pwHash

>> pip install -r requirements.txt

>> python hasher.py
```

### Usage
It requires 2 neccessary arguments to work.

```
>> hasher.py -p [Password] -f [Hash Function]
```
#### Supported Hash Types
1. <b>MD5</b> [md5]
2. <b>SHA-1</b> [sha1]
3. <b>SHA-256</b> [sha256]
4. <b>SHA-384</b> [sha384]
5. <b>SHA-512</b> [sha512]

#### Example
```
>> hasher.py -p 12345 -f md5

MD5:
[+] a6bb4faacdff9dcdcb6f6e22bc51eac9
```
