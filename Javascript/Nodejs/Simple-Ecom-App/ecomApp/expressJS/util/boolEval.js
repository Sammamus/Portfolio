const evalBool = (stringBool) => {
    if (stringBool.toLowerCase() === "true") {
        return true
    } else {
        return false
    }
}

module.exports = evalBool;