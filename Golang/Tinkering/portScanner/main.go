package main

import (
	"fmt"
	"net"
	"sort"
)

func worker(ports, results chan int) {
	for p := range ports {
		url := fmt.Sprintf("scanme.nmap.org:%d", p)
		conn, err := net.Dial("tcp", url)

		if err != nil {
			results <- 0
			continue
		}

		conn.Close()
		results <- p
	}
}

func main() {
	totalPorts := 65535

	ports := make(chan int, 1000)
	results := make(chan int)
	var openports []int

	for i := 0; i <= cap(ports); i++ {
		go worker(ports, results)
	}

	go func() {
		for j := 1; j <= totalPorts; j++ {
			ports <- j
		}
	}()

	for k := 0; k < totalPorts; k++ {
		port := <-results
		if port != 0 {
			openports = append(openports, port)
		}
	}

	close(ports)
	close(results)
	sort.Ints(openports)

	for _, port := range openports {
		fmt.Printf("%d open\n", port)
	}

}
