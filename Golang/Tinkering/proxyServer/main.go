package main

import (
	"fmt"
	"io"
	"log"
	"net"
)

func handle(src net.Conn, site string) {
	siteWithPort := site + ":80"
	dst, err := net.Dial("tcp", siteWithPort)
	if err != nil {
		log.Fatalln("Unable to connect to out unreachable host")
	}
	defer dst.Close()

	go func() {
		if _, err := io.Copy(dst, src); err != nil {
			log.Fatalln(err)
		}
	}()

	if _, err := io.Copy(src, dst); err != nil {
		log.Fatalln(err)
	}
}

func main() {

	fmt.Println("What site do you wish to proxy to?")

	var site string

	fmt.Scanln(&site)

	listener, err := net.Listen("tcp", ":80")
	if err != nil {
		log.Fatalln("Unable to bind to port")
	}
	log.Println("Listening on 0.0.0.0:80")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalln("Unable to accept connection")
		}

		go handle(conn, site)
	}
}
