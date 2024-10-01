package main

import (
	"fmt"
	"io"
	"os"
)

// keep asc order
func swap(x, y *int) {
	var tmp int = *x
	*x = *y
	*y = tmp
}

// cat subnet + ip
func merge(subnet string, ip int) string {
	return fmt.Sprintf("%s.%d", subnet, ip)
}

// write to file and console
func declare(out string, writer io.Writer) {
	fmt.Fprintln(writer, out)
}

func main() {

	// take input
	fmt.Print("Subnet: ")
	var subnet string
	fmt.Scan(&subnet)

	fmt.Print("Range: ")
	var a, b int
	fmt.Scan(&a, &b)

	if a > b {
		swap(&a, &b)
	}

	// touch an 'out.txt' file
	file, err := os.Create("out.txt")
	if err != nil {
		fmt.Println("can't touch file: ", err)
		return
	}
	defer file.Close()

	// let write to console and 'out.txt' file same time
	writer := io.MultiWriter(os.Stdout, file)

	// loop through the range and write
	for ip := a; ip <= b; ip++ {
		merged := merge(subnet, ip)
		declare(merged, writer)
	}
}
