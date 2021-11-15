*Class choices:*
In aehyam.json.data.choices.class staan denk ik de class keuzes die je hebt gemaakt voor je character.
Hier kun je bijvoorbeeld de keuzes zien in .options en de keuze die gemaakt is in .optionValue.
Search "            { "id": 3783, "label": "Athletics", "description": null }, " for example.

*Actions (Rage, magic awareness, mogelijk iets anders?)*
In aehyam.json.data.actions.class.0 staan dingen zoals rege met een max aantal uses en de current uses.
.name is de naam van de eigenschap
.limitedUse heeft de data voor het gebruik
	.maxUses 
	.resetType denk ik of het reset bij een long rest of iets anders? (Zoek naar resetType in de json op te checken)
	.numberUsed is denk ik hoeveel er geconsumed is, anders misschien minNumberConsumed, maxNumberConsumed
	.operator Check ook even wat operator betekent. Dit lijkt een id te zijn van een andere lijst binnen de json.

Note: Misschien containt aehyam.json.data.actions.class.race de uses van dezelfde-achtige dingen die je puur door je race kan doen ipv door je class

*Modifiers (Proficiencies en voordelen van alle soorten en maten, maar ook bijvoorbeeld perception proficiency)*
Aehyam.json.data.modifiers.race.1 Perception modifiers

Aehyam.json.data.modifiers.class.0

*Spellslots*
Aehyam.json.data.spellSlots.1#level/#used/#available


*Conditions*
Het is onduidelijk welke van de volgende:
Aehyam.json.data
	.conditions
	.spells.race.0.definition.conditions
	.spells.race.0.definition.conditions
	.spells.race.racialTraits.0.definition.description

**
