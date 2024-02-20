package main

// Importing fmt and time
import (
	"fmt"
	"time"
)

// Calling main
func main() {

	// Declaring layout constant
	const layout = "2006-01-02 15:04:05-0700"

	// Calling Parse() method with its parameters
	tm, _ := time.Parse(layout, "2024-01-28 09:57:35-0300")

	// Returns output
	fmt.Println(tm)
}
