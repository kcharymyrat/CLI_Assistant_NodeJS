const { mkdir, rm, access, accessFile, rmFile,  } = require('node:fs/promises');

const getCommandResponse = require("./tools/getCommandResponse.js")


const args = process.argv.slice(2)
args.forEach((arg) => {
    const [command, value] = arg.split("=")
    // console.log(command, value)
    getCommandResponse(command, value)
});

// args.forEach((arg) => getCommandResponse(arg))



