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

func main() {
    file, err := os.Open("test.csv") // For read access.
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

        line , _ := br.ReadString('\n')
        //stringSlice []string
        stringSlice := strings.Split(line,",")
        if stringSlice[1] == "商業登記" {
            writeBusiness.WriteString(line + "\n")
        }else if stringSlice[1] == "公司" {
            writeCompany.WriteString(line + "\n")
        }else if stringSlice[1] == "分公司" {
            writeSubCompany.WriteString(line + "\n")
        }
        fmt.Printf("%v",line)
   }

}