Scriptname MainQuestCompletionTracker extends Quest

; Function to check if the player has completed the main quest
Int Function PlayerHasCompletedMainQuest()
    ; Declare result as an integer and initialize it to 0
    int result = 0
    ; Get the quest object from its form ID
    Quest MQ305Quest = Game.GetForm(0x000361E2) as Quest
    ; Check if the quest object is valid (not None)
    if MQ305Quest != None
        ; Check if the main quest is completed
        if MQ305Quest.IsStageDone(200) ; Assuming 200 is the completion stage
            result = 1
        endIf
    endIf
    ; Return the result
    Return result
EndFunction

; Event that initializes when the script is loaded
Event OnInit()
    ; Call the function and store the result
    int result = PlayerHasCompletedMainQuest()
    ; Get the global variable object from its form ID and ESP file
    GlobalVariable GV_EldenRing_MainQuestCompleted = Game.GetFormFromFile(0x01001000, "EldenRingArrowInTheKnee.esp") as GlobalVariable
    ; Check if the global variable object is valid (not None)
    if GV_EldenRing_MainQuestCompleted != None
        ; Set the global variable value based on the result
        if result == 1
            GV_EldenRing_MainQuestCompleted.SetValue(1)
        else
            GV_EldenRing_MainQuestCompleted.SetValue(0)
        endIf
    endIf
EndEvent
