package main

import (
	"fmt"
	"time"
)

func binarySearch(arr []int, n int, x int) int {
	start := 0
	end := n - 1
	for start <= end {
		mid := start + (end-start)/2

		if arr[mid] == x {
			return mid
		} else if arr[mid] < x {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return -1
}
func linearSearch(arr []int, n int, target int) int {
	for i := 0; i < n; i++ {
		if arr[i] == target {
			return i
		}
	}
	return -1
}

func main() {
	arr := make([]int, 10000000)
	n := len(arr)

	// Isi array dengan angka berurutan dari 1 hingga 10.000.000
	for i := 0; i < n; i++ {
		arr[i] = i + 1
	}

	pilihan := 1
	index1, index2 := 0, 0

	for pilihan != 0 {
		fmt.Println("===========================")
		fmt.Println("1. binary search")
		fmt.Println("2. linear search")
		fmt.Println("0. exit")
		fmt.Println("===========================")
		fmt.Print("Pilih algoritma yang akan digunakan untuk melakukan pencarian : ")
		fmt.Scanf("%d", &pilihan)

		if pilihan == 1 {
			var i int = 100
			start := time.Now()
			for i < 10000000 {
				index1 = binarySearch(arr, n, i)
				if index1 != -1 {
					fmt.Printf("The element %d was found at index %d\n", i, index1)
					stop := time.Now()
					duration := stop.Sub(start)
					fmt.Printf("Running time: %f Seconds\n\n", duration.Seconds())
				} else {
					fmt.Println("The element was not found")
				}
				i = i * 10
			}
		} else if pilihan == 2 {
			var i int = 100
			start := time.Now()
			for i < 10000000 {
				index2 = linearSearch(arr, n, i)
				if index1 != -1 {
					fmt.Printf("The element %d was found at index %d\n", i, index2)
					stop := time.Now()
					duration := stop.Sub(start)
					fmt.Printf("Running time: %f Seconds\n\n", duration.Seconds())
				} else {
					fmt.Println("The element was not found")
				}
				i = i * 10
			}
		}

		fmt.Println("Pilih algoritma yang akan digunakan untuk melakukan pencarian :")
		fmt.Scanf("%d", &pilihan)
	}

	fmt.Println("Program berakhir")
}
