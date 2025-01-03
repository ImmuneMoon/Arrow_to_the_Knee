Scriptname SaveManagement extends Quest

Event OnQuestCompleted()
    PromptPlayerToSave()
EndEvent

Function PromptPlayerToSave()
    Debug.Notification("Quest completed! Please manually save your game to a new file.")
    int randomNum = Utility.RandomInt(1, 100000)
    String suggestedSaveName = "ArrowKnee_Mod_Save_" + randomNum
    Debug.Notification("Suggested Save Name: " + suggestedSaveName)
    Debug.MessageBox("Please save your game manually now. Suggested Save Name: " + suggestedSaveName)
EndFunction
