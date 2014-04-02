/* 
* @Author: rtseng
* @Date:   2014-04-02 16:16:13
* @Last Modified by:   rtseng
* @Last Modified time: 2014-04-02 17:52:36
*/

package main

import (
    "fmt"
    "os"
    "strings"
    "log"
    "bufio"
)

type company struct {
    Id      string
    Type    string
    Name    string
}

func main() {
    file, err := os.Open("index.csv") // For read access.
    if err != nil {
        log.Fatal(err)
    }

    //dataStruct := map[string]string{}
    businessFile, err := os.Create("business.txt")
    companyFile, err := os.Create("company.txt")
    subCompanyFile, err := os.Create("subcompany.txt")
    br := bufio.NewReader(file)
    writeBusiness := bufio.NewWriter(businessFile)
    writeCompany := bufio.NewWriter(companyFile)
    writeSubCompany := bufio.NewWriter(subCompanyFile)
    for{
       //每次读取一行
        line , _ := br.ReadString('\n')
        //stringSlice []string
        stringSlice := strings.Split(line,",")
        if stringSlice[1] == "商業登記" {
            business, _ := writeBusiness.WriteString(line)
            fmt.Printf("wrote %d bytes\n", business)
        }else if stringSlice[1] == "公司" {
            company, _ := writeCompany.WriteString(line)
            fmt.Printf("wrote %d bytes\n", company)
        }else if stringSlice[1] == "分公司" {
            subCompany, _ := writeSubCompany.WriteString(line)
            fmt.Printf("wrote %d bytes\n", subCompany)
        }
        fmt.Printf("%v",line)
   }

}