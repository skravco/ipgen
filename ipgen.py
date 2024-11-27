import argparse


class IPAddressGenerator:
    """
    Class to generate IP addresses within a given range for a specified subnet.
    """

    def __init__(self, subnet: str, ip_range: str):
        self.subnet = subnet
        self.start, self.end = self._parse_range(ip_range)

    def _parse_range(self, ip_range: str):
        """
        Parse the range string (e.g., "10,25") and return the start and end as integers.
        """
        try:
            start, end = map(int, ip_range.split(","))
            if start < 0 or end > 255 or start > end:
                raise ValueError("Invalid range values.")
            return start, end
        except Exception:
            raise ValueError("Range must be specified as 'start,end' with values between 0 and 255.")

    def generate_ips(self):
        """
        Generate IP addresses based on the subnet and range.
        """
        for i in range(self.start, self.end + 1):
            yield f"{self.subnet}{i}"

    def write_to_file(self, output_file: str = "out.txt"):
        """
        Write the generated IP addresses to a file.
        """
        try:
            with open(output_file, "w") as f:
                for ip in self.generate_ips():
                    f.write(f"{ip}\n")
            print(f"IP addresses written to {output_file}")
        except Exception as e:
            print(f"Failed to write to file: {e}")


def main():
    """
    Command-line interface for the IPAddressGenerator tool.
    """
    parser = argparse.ArgumentParser(
        description="Generate IP addresses within a range for a specified subnet."
    )
    parser.add_argument(
        "subnet", help="The subnet prefix (e.g., '10.0.0.')"
    )
    parser.add_argument(
        "range",
        help="The range of host IDs (e.g., '10,25'). Start and end must be between 0 and 255.",
    )
    parser.add_argument(
        "--output",
        default="out.txt",
        help="The output file where IPs will be written. Default is 'out.txt'.",
    )
    args = parser.parse_args()

    # Validate subnet format
    if not args.subnet.endswith(".") or not all(part.isdigit() for part in args.subnet.split(".")[:-1]):
        print("Invalid subnet format. Subnet must end with a dot (e.g., '10.0.0.')")
        return

    # Generate and write IP addresses
    generator = IPAddressGenerator(args.subnet, args.range)
    generator.write_to_file(args.output)


if __name__ == "__main__":
    main()
