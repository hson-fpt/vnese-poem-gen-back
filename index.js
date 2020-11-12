const express = require("express")
const bodyParser = require("body-parser")
const cors = require("cors")
const app = express()

const {readReactInp} = require("./app")


app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors())
app.post("/getInp", (req, res) => {
    console.log("oke bro")
    let resPoem = readReactInp(req.body.poemStarter)
    res.json({resPoem})
})


app.listen("8008", () => {console.log("bruh")})
