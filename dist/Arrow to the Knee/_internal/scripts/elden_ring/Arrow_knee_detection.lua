-- Queue to manage notifications
local notifications = {}

-- Function to display notifications on screen
function displayNotification(message)
    table.insert(notifications, message)
    print(message)  -- Also print to console or log for debugging

    -- Ensure the list doesn't exceed 7 notifications
    if #notifications > 7 then
        table.remove(notifications, 1)
    end

    -- Show notification on screen (hypothetical function, replace with actual in-game notification code)
    ShowMessageOnScreen(message)
end

-- Function to process and update notifications on screen
function updateNotifications()
    -- Loop through notifications and update their display positions (bottom-left corner)
    for i, notification in ipairs(notifications) do
        -- Display each notification (replace with actual in-game UI update code)
        DisplayNotificationAt(notification, i, "bottom-left")
    end
end

function detectArrowKneeHit(event)
    displayNotification("Projectile hit detected")
    if playerHitByArrowToKnee(event) then
        playArrowToKneeSound()
        markEldenRingSaveAsDisabled()
        teleportToSkyrim()
    end
end

function playerHitByArrowToKnee(event)
    local hitObject = event.target
    local projectile = event.projectile
    displayNotification("Checking if player hit by arrow to knee...")

    if hitObject:IsPlayer() and (projectile:GetType() == "Arrow" or projectile:GetType() == "Bolt" or isSpecialProjectile(projectile)) then
        displayNotification("Projectile type matched, checking hit location...")
        return isKneeHit(event.hitLocation)
    end
    displayNotification("Projectile type did not match or hit object is not player")
    return false
end

function isSpecialProjectile(projectile)
    local id = projectile:GetID()
    displayNotification("Checking if projectile is special. ID: " .. id)
    return id == 007 or id == 008  -- Include other special projectile IDs as needed
end

function isKneeHit(hitLocation)
    local leftKneeRegionMin = { x = 0.4, y = 0.3, z = 0.4 }
    local leftKneeRegionMax = { x = 0.6, y = 0.5, z = 0.6 }
    local rightKneeRegionMin = { x = -0.6, y = 0.3, z = 0.4 }
    local rightKneeRegionMax = { x = -0.4, y = 0.5, z = 0.6 }

    displayNotification("Hit location: " .. hitLocation.x .. ", " .. hitLocation.y .. ", " .. hitLocation.z)
    if (hitLocation.x >= leftKneeRegionMin.x and hitLocation.x <= leftKneeRegionMax.x and
        hitLocation.y >= leftKneeRegionMin.y and hitLocation.y <= leftKneeRegionMax.y and
        hitLocation.z >= leftKneeRegionMin.z and hitLocation.z <= leftKneeRegionMax.z) or
       (hitLocation.x >= rightKneeRegionMin.x and hitLocation.x <= rightKneeRegionMax.x and
        hitLocation.y >= rightKneeRegionMin.y and hitLocation.y <= rightKneeRegionMax.y and
        hitLocation.z >= rightKneeRegionMin.z and hitLocation.z <= rightKneeRegionMax.z) then
        displayNotification("Hit registered on knee")
        return true
    end
    displayNotification("Hit not on knee")
    return false
end

function playArrowToKneeSound()
    local soundPath = "Data/Music/arrow to the knee 1.0/arrow_to_knee.mp3"
    PlaySound(soundPath)
    displayNotification("Playing arrow to the knee sound effect...")
end

function markEldenRingSaveAsDisabled()
    -- Logic to disable the Elden Ring save
    SaveGame("Disabled_EldenRingSave")
    displayNotification("Marked Elden Ring save as disabled.")
end

function teleportToSkyrim()
    displayNotification("Teleporting to Skyrim...")
    SaveGame("EldenRingSave")
    os.execute("start skyrim_launcher.bat")
end

RegisterEvent("ProjectileHit", detectArrowKneeHit)

function SaveGame(saveName)
    displayNotification("Game state saved: " .. saveName)
end

function PlaySound(soundPath)
    displayNotification("Playing sound: " .. soundPath)
end

-- Call updateNotifications periodically to refresh notifications on screen
Game.OnUpdate(updateNotifications)  -- Replace with the actual in-game event loop or update function
