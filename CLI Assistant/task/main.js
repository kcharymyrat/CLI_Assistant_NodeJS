const args = process.argv
const print = console.log
// print(args)

if (args.length > 2) {
    const commands = args.slice(2)
    commands.forEach( (arg) => getArgsResponse(arg.trim()))
}

function getArgsResponse(arg) {
    if (arg.startsWith("--")) {
        const command = arg.slice(2)
        return getCommandResponse(command)
    } else if (arg.startsWith("-")) {
        const command = arg.slice(1)
        return getCommandResponse(command)
    }
}

function getCommandResponse(command) {
    if (command.includes("=")){
        if (command[command.length - 1] === "="){
            print("It seems you forget to specify argument!")
        } else {
            const index = command.indexOf("=")
            print(`${command.slice(0, index)}: ${command.slice(index + 1)}`)
        }
    } else {
        print(`${command}: true`)
    }
}

