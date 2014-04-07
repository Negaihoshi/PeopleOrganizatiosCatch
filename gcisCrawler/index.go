/*
* @Author: rtseng
* @Date:   2014-04-02 16:16:13
* @Last Modified by:   rtseng
* @Last Modified time: 2014-04-07 13:30:59
 */

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("index.csv") // For read access.
	if err != nil {
		log.Fatal(err)
	}

	//dataStruct := map[string]string{}
	businessFile, err := os.Create("business.txt")
	companyFile, err := os.Create("company.txt")
	subCompanyFile, err := os.Create("subcompany.txt")
	//br := bufio.NewReader(file)
	br := bufio.NewScanner(file)
	writeBusiness := bufio.NewWriter(businessFile)
	writeCompany := bufio.NewWriter(companyFile)
	writeSubCompany := bufio.NewWriter(subCompanyFile)

	for br.Scan() {

		//line, err := br.ReadString('\n')

		if err != nil {
			break
		}

		//stringSlice []string
		line := br.Text()
		stringSlice := strings.Split(line, ",")
		//fmt.Printf("%#v\n", stringSlice)
		if stringSlice[1] == "商業登記" {
			writeBusiness.WriteString(line + "\n")
		} else if stringSlice[1] == "公司" {
			writeCompany.WriteString(line + "\n")
		} else if stringSlice[1] == "分公司" {
			writeSubCompany.WriteString(line + "\n")
		}
		fmt.Printf("%v\n", line)
	}
	if err := br.Err(); err != nil {
		log.Fatal(err)
	}

}
