# ipgen

The program generates a list of IP addresses within a given range 
<br>
Results are printed to both the console and a file (`out.txt`)

### build the program
> Ensure Go is installed, then run: 
``` bash 
go build -o ipgen
```

### run the program 
> Execute the program and provide the subnet and IP range:
``` bash 
./ipgen
```

### examples:
##### input 
---
Subnet: 192.168.1
<br>
Range: 5 1

##### output
---
192.168.1.1
<br>
192.168.1.2
<br>
192.168.1.3
<br>
192.168.1.4
<br>
192.168.1.5

