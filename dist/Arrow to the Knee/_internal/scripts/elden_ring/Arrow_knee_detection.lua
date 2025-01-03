function detectArrowKneeHit(event)
    if playerHitByArrowToKnee(event) then
        playArrowToKneeSound()
        markEldenRingSaveAsDisabled()
        teleportToSkyrim()
    end
end

function playerHitByArrowToKnee(event)
    local hitObject = event.target
    local projectile = event.projectile

    if hitObject:IsPlayer() and projectile:GetType() == "Arrow" then
        return isKneeHit(event.hitLocation)
    end
    return false
end

function isKneeHit(hitLocation)
    local leftKneeRegionMin = { x = 0.4, y = 0.3, z = 0.4 }
    local leftKneeRegionMax = { x = 0.6, y = 0.5, z = 0.6 }
    local rightKneeRegionMin = { x = -0.6, y = 0.3, z = 0.4 }
    local rightKneeRegionMax = { x = -0.4, y = 0.5, z = 0.6 }

    if (hitLocation.x >= leftKneeRegionMin.x and hitLocation.x <= leftKneeRegionMax.x and
        hitLocation.y >= leftKneeRegionMin.y and hitLocation.y <= leftKneeRegionMax.y and
        hitLocation.z >= leftKneeRegionMin.z and hitLocation.z <= leftKneeRegionMax.z) or
       (hitLocation.x >= rightKneeRegionMin.x and hitLocation.x <= rightKneeRegionMax.x and
        hitLocation.y >= rightKneeRegionMin.y and hitLocation.y <= rightKneeRegionMax.y and
        hitLocation.z >= rightKneeRegionMin.z and hitLocation.z <= rightKneeRegionMax.z) then
        return true
    end
    return false
end

function playArrowToKneeSound()
    local soundPath = "Data/Music/arrow to the knee 1.0/arrow_to_knee.mp3"
    PlaySound(soundPath)
    print("Playing arrow to the knee sound effect...")
end

function markEldenRingSaveAsDisabled()
    -- Logic to disable the Elden Ring save
    SaveGame("Disabled_EldenRingSave")
    print("Marked Elden Ring save as disabled.")
end

function teleportToSkyrim()
    print("Teleporting to Skyrim...")
    SaveGame("EldenRingSave")
    os.execute("start skyrim_launcher.bat")
end

RegisterEvent("ProjectileHit", detectArrowKneeHit)

function SaveGame(saveName)
    print("Game state saved:", saveName)
end

function PlaySound(soundPath)
    print("Playing sound:", soundPath)
end
