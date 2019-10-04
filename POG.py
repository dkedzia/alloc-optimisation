class POG:
    participants = []
    groups = []

    preferences = [[]]
    preferences.append([])
    def addParticipant(self, name):
        POG.participants.append(name)

    def addClass(self, name):
        POG.groups.append(name)

    def setPreference(self, participant, group):
        POG.preferences[0].append(participant)
        POG.preferences[1].append(group)


pog = POG()
pog.addParticipant("Dominik")
pog.addParticipant("Piotr")
pog.addParticipant("Magda")
pog.addParticipant("Przemyslaw")
pog.addParticipant("Agnieszka")
print(pog.participants)

pog.addClass("IA")
pog.addClass("IB")
print(pog.preferences)

pog.setPreference()