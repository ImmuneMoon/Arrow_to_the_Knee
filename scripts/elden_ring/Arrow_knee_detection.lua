function detectArrowKneeHit(event)
    -- Logic to detect arrow to the knee event in Elden Ring
    if playerHitByArrowToKnee(event) then
        playArrowToKneeSound()
        teleportToSkyrim()
    end
end

function playerHitByArrowToKnee(event)
    -- Check if the hitObject is the player character and the projectile is an arrow
    local hitObject = event.target
    local projectile = event.projectile

    if hitObject:IsPlayer() and projectile:GetType() == "Arrow" then
        -- Check if the hit location is on either knee
        return isKneeHit(event.hitLocation)
    end
    return false
end

function isKneeHit(hitLocation)
    -- Define the knee region boundaries (example values)
    local leftKneeRegionMin = { x = 0.4, y = 0.3, z = 0.4 }
    local leftKneeRegionMax = { x = 0.6, y = 0.5, z = 0.6 }
    local rightKneeRegionMin = { x = -0.6, y = 0.3, z = 0.4 }
    local rightKneeRegionMax = { x = -0.4, y = 0.5, z = 0.6 }

    -- Check if the hitLocation is within the boundaries of either knee region
    if (hitLocation.x >= leftKneeRegionMin.x and hitLocation.x <= leftKneeRegionMax.x and
        hitLocation.y >= leftKneeRegionMin.y and hitLocation.y <= leftKneeRegionMax.y and
        hitLocation.z >= leftKneeRegionMin.z and hitLocation.z <= leftKneeRegionMax.z) or
       (hitLocation.x >= rightKneeRegionMin.x and hitLocation.x <= rightKneeRegionMax.x and
        hitLocation.y >= rightKneeRegionMin.y and hitLocation.y <= rightKneeRegionMax.y and
        hitLocation.z >= rightKneeRegionMin.z and hitLocation.z <= rightKneeRegionMax.z) then
        return true  -- Hit is on one of the knees
    end
    return false  -- Hit is not on either knee
end

function playArrowToKneeSound()
    -- Logic to play the arrow to the knee sound effect
    local soundPath = "Data/Music/arrow to the knee 1.0/arrow_to_knee.mp3"
    PlaySound(soundPath)
    print("Playing arrow to the knee sound effect...")
end

function teleportToSkyrim()
    -- Logic to teleport the player to Skyrim
    print("Teleporting to Skyrim...")
    -- Save the game state in Elden Ring
    SaveGame("EldenRingSave")

    -- Launch Skyrim and load the save file
    LaunchGame("Skyrim", "SkyrimSave")
end

-- Register the event listener for arrow hits
RegisterEvent("ProjectileHit", detectArrowKneeHit)

-- Placeholder functions for saving and launching the game
function SaveGame(saveName)
    print("Game state saved:", saveName)
end

function LaunchGame(gameName, saveName)
    print("Launching", gameName, "with save:", saveName)
end

function PlaySound(soundPath)
    -- Logic to play a sound file
    -- This function needs to be implemented with the game's audio API
    print("Playing sound:", soundPath)
end
