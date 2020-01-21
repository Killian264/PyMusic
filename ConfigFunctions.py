import json

configLoc = "./config.json"
baseMusicLoc = "./Music"

# this could be changed out later to some kind of object or have an object passed after which it would be converted and written to file
def updateConfig(volume, musicFolder, configLoc=configLoc):
    config ={
        "Volume": volume,
        "MusicFolder": musicFolder
    }
    with open(configLoc, "w") as file:
        json.dump(config, file)


def getSettings(configLoc=configLoc):
    # This can be updated later with more settings pretty easily
    try:
        with open(configLoc) as file:
            config = json.load(file)
    except:
        updateConfig(10, baseMusicLoc)
        return 10, baseMusicLoc

    volume = config["Volume"]
    musicLoc = config["MusicFolder"]

    print(volume, musicLoc)

    if volume == '' or musicLoc == '':
        volume = 10 if volume == '' else volume
        musicLoc = baseMusicLoc if musicLoc == '' else musicLoc

        updateConfig(volume, musicLoc)

    return volume, musicLoc