Scriptname MainQuestCompletionTracker extends Quest

Int Function PlayerHasCompletedMainQuest()
    int result = 0
    Quest MQ305Quest = Game.GetForm(0x000361E2) as Quest
    if MQ305Quest != None
        if MQ305Quest.IsStageDone(200)
            result = 1
        endIf
    endIf
    Return result
EndFunction

Event OnInit()
    int result = PlayerHasCompletedMainQuest()
    GlobalVariable GV_ArrowKnee_MainQuestCompleted = Game.GetFormFromFile(0x01001000, "EldenRingArrowInTheKnee.esp") as GlobalVariable
    if GV_ArrowKnee_MainQuestCompleted != None
        if result == 1
            GV_ArrowKnee_MainQuestCompleted.SetValue(1)
            EnableEldenRingSave()
        else
            GV_ArrowKnee_MainQuestCompleted.SetValue(0)
        endIf
    endIf
EndEvent

Function EnableEldenRingSave()
    Debug.Notification("You have completed Skyrim's main quest. You can now continue your Elden Ring save.")
    ; Logic to enable the Elden Ring save
endFunction
