function manageSaves()
    print("Managing save files...")
    saveEldenRingState("EldenRingSave")
    saveSkyrimState("SkyrimSave")
end

function saveEldenRingState(saveName)
    local savePath = "EldenRingSaves/" .. saveName .. ".sav"
    print("Saving Elden Ring state to:", savePath)
end

function saveSkyrimState(saveName)
    local savePath = "SkyrimSaves/" .. saveName .. ".ess"
    print("Saving Skyrim state to:", savePath)
end

function loadEldenRingState(saveName)
    local savePath = "EldenRingSaves/" .. saveName .. ".sav"
    print("Loading Elden Ring state from:", savePath)
end

function loadSkyrimState(saveName)
    local savePath = "SkyrimSaves/" .. saveName .. ".ess"
    print("Loading Skyrim state from:", savePath)
end

manageSaves()

