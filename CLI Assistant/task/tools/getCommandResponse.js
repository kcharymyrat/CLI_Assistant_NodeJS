const { mkdir, rm, access, stat, readdir} = require('node:fs/promises');
const path = require('node:path');

const isExists = async (value) => {
    try {
        await access(value);
        return true
    } catch {
        return false
    }
}

const getCommandResponse = async (command, value) => {
    switch (command) {
        case '--isFolder':
            try {
                if (await isExists(value)) {
                    const stats = await stat(value);
                    if (stats.isDirectory()) {
                        console.log(`The ${value} is a folder!`);
                    } else {
                        console.log(`The ${value} is not a folder!`);
                    }
                } else {
                    console.log(`It seems that some specified files don't exist!`)
                }
            } catch {
                 console.log(`It seems that some specified files don't exist!`)
            }
            break;
        case '--size':
            try {
                const filenames = value.split('-');
                let exists = true
                let size = 0
                for (const filename of filenames) {
                    if (await isExists(filename)) {
                        const stats = await stat(filename);
                        size += Math.trunc(stats.size)
                    } else {
                        exists = false
                        break;
                    }
                }
                if (exists) {
                    console.log(`The size of the specified files is ${size} kilobytes`)
                } else {
                    console.log(`It seems that some specified files don't exist!`)
                }
            } catch {
                 console.log(`It seems that some specified files don't exist!`)
            }
            break;
        case '--content':
            try {
                const files = await readdir(".");
                for (const file of files) {
                    console.log(file);
                }
            } catch (e) {
                console.log(`No such directory: ${value}`);
            }
            break;
        case '--exist':
            try {
                await access(value);
                console.log(`The file ${value} exists!`)
            } catch {
                console.log(`The file ${value} does not exist!`)
            }
            break;
        case '--create':
            try {
                await mkdir(value, {recursive: true})
                if (value.includes("/"))  {
                    console.log(`The folders ${value} were created!`)
                } else {
                    console.log(`The folder ${value} was created!`)
                }
            } catch {
                console.error(`Error creating folder ${value}: ${e}`)
            }
            break;
        case '--remove':
            try {
                if (await isExists(value)) {
                    await rm(value, { recursive: true })
                    if (value.includes("/")) {
                        // console.log(value)
                        const [parent, child] = value.split("/")
                        console.log(`The folder ${parent} in ${child} folder was deleted!`)
                    } else {
                        console.log(`The folder ${value} was deleted!`)
                    }
                } else {
                    console.log(`This ${value} folder doesn't exist!`)
                }
            } catch {
                console.error(`Error removing folder ${value}`)
            }
            break;
        default:
            console.log(`Unknown command: ${command}`);
    }
}

module.exports = getCommandResponse