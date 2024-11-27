# IPGen

**Tool generates a list of IP addresses within a specified range for a given subnet**. The generated IPs are written to a file, one per line, in a format suitable for further networking tasks or automation.

---

## Features

- **Subnet Specification**: Provide a subnet (e.g., `10.0.0.`) as a prefix for the generated IP addresses.
- **Range Selection**: Define a range of host IDs (e.g., `1,50`) to generate only the desired subset of addresses.
- **Output to File**: Write the generated IP addresses to a file (`out.txt` by default) for easy access and reuse.
- **Validation**: Ensures valid subnet formats and IP range inputs.

---

## Requirements

- Python 3.6 or later.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/skravco/ipgen.git
   cd ipgen
   ```

---

## Usage

Run the tool from the command line with the required arguments:

### **Basic Command**
```bash
python3 ipgen.py <subnet> <range> [--output <file>]
```

### **Positional Arguments**
1. **`subnet`**:
   - The subnet prefix for the IP addresses (e.g., `192.168.1.` or `10.0.0.`).
   - Must end with a dot (`.`).
   - Example: `192.168.1.`

2. **`range`**:
   - The range of host IDs to generate IP addresses for.
   - Format: `start,end` (e.g., `10,25`).
   - Values must be integers between `0` and `255`, with `start <= end`.

### **Optional Arguments**
- **`--output <file>`**:
  - Specify the name of the file to write the generated IPs. Default: `out.txt`.

---

### Examples

#### **Generate IPs for Subnet `192.168.1.` with Range `10,20`**
```bash
python3 ipgen.py 192.168.1. 10,15
```
Output file (`out.txt`):
```
192.168.1.10
192.168.1.11
192.168.1.12
192.168.1.13
192.168.1.14
192.168.1.15
```

#### **Specify a Custom Output File**
```bash
python3 ipgen.py 10.0.0. 1,5 --output generated_ips.txt
```
Output file (`generated_ips.txt`):
```
10.0.0.1
10.0.0.2
10.0.0.3
10.0.0.4
10.0.0.5
```

#### **Validation Example**
```bash
python3 ipgen.py 10.0.0 1,300
```
Output:
```
Range must be specified as 'start,end' with values between 0 and 255.
```

---

## How It Works

1. **Subnet Validation**:
   - The subnet must end with a dot (e.g., `192.168.1.`).
   - Ensures correct format for IP address generation.

2. **Range Validation**:
   - Validates that `start` and `end` are integers between `0` and `255`.
   - Ensures that `start <= end`.

3. **IP Address Generation**:
   - Combines the subnet prefix with each number in the specified range to generate valid IPs.

4. **Output to File**:
   - Writes each generated IP to the specified file, one per line.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

---