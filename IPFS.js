// import ipfsAPI from "ipfs-api";
//C:\Users\tengfa.000\Downloads\Video
const ipfsAPI = require("ipfs-api")
const fs = require('fs')
const ipfs = ipfsAPI({
    host: "ipfs.infura.io",
    port: "5001",
    protocol: "https"
});


const video = fs.readFileSync("C:/Users/tengfa.000/Downloads/Video/1.mp4")


let handler = (a,b,c,d)=>{
    console.log("handler>>",a,b,c,d)
}
ipfs.add(video, { progress: handler },(err,file)=>{
    console.log(err,file)
})

// .then(rep=>{
//     console.log(rep)
// })
// console.log(video)

