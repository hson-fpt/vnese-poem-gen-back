const {execSync} = require("child_process")
let fs = require("fs")



function readReactInp(reactInput) {
    execSync(`python3 app.py ${reactInput} > output.txt`)
    let result = fs.readFileSync("output.txt", {encoding: "utf-8"})    
    return result
}


module.exports = {
    readReactInp
}