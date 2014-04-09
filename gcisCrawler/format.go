/* 
* @Author: rtseng
* @Date:   2014-04-09 10:53:23
* @Last Modified by:   rtseng
* @Last Modified time: 2014-04-09 14:19:56
*/

package main

import (
    "io/ioutil"
    "log"
    "net/http"
    "os"
    "encoding/json"
    //"github.com/ugorji/go/codec"
    "fmt"
)

type CompanyStruct struct{

}

func main() {

    //var mh codec.MsgpackHandle

    //data := CompanyStruct{}

    //mh.StructToArray = true

    //enc = codec.NewEncoderBytes(&b, &mh)
    //err = enc.Encode(data)

    res, err := http.Get("http://company.g0v.ronny.tw/api/show/97751885")
    if err != nil {
        log.Println(err)
        os.Exit(0)
    }
    defer res.Body.Close()

    var s string
    body, _ := ioutil.ReadAll(res.Body)
    //log.Println(string(body))
    json.Unmarshal([]byte(string(body)), &s)
    fmt.Println(string(s))
}