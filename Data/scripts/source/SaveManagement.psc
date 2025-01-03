Scriptname SaveManagement extends Quest

Event OnQuestCompleted()
    PromptPlayerToSave()
EndEvent

Function PromptPlayerToSave()
    ; Logic to prompt the player to save the game
    Debug.Notification("Quest completed! Please manually save your game to a new file.")
    
    ; Generate a unique save file name suggestion
    int randomNum = Utility.RandomInt(1, 100000)
    String suggestedSaveName = "Arrow_to_the_Knee_Mod_Save_" + randomNum

    ; Display the suggested save name to the player
    Debug.Notification("Suggested Save Name: " + suggestedSaveName)
    
    ; Inform the player to save manually
    Debug.MessageBox("Please save your game manually now. Suggested Save Name: " + suggestedSaveName)
EndFunction

