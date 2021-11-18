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


--- Choose an ability score: ---
{
          "fixedValue": 1,
          "id": "1665",
          "entityId": null,
          "entityTypeId": null,
          "type": "bonus",
          "subType": "choose-an-ability-score",
          "dice": null,
          "restriction": null,
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Choose an Ability Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 1,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 695,
          "componentId": 56,
          "componentTypeId": 12168134
        },
        {
          "fixedValue": 1,
          "id": "1789",
          "entityId": null,
          "entityTypeId": null,
          "type": "bonus",
          "subType": "choose-an-ability-score",
          "dice": null,
          "restriction": null,
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Choose an Ability Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 1,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 695,
          "componentId": 56,
          "componentTypeId": 12168134
        },


------

DATA -> RACE -> RACIALTRAITS -> ABLITY SCORIE INCREASE

        {
          "definition": {
            "id": 72,
            "definitionKey": "racial-trait:72",
            "entityTypeId": 1960452172,
            "displayOrder": 1,
            "name": "Ability Score Increase",
            "description": "<p>Your Dexterity score increases by 2.</p>",
            "snippet": "",
            "hideInBuilder": true,
            "hideInSheet": true,
            "activation": null,
            "sourceId": 1,
            "sourcePageNumber": 23,
            "creatureRules": [],
            "spellListIds": [],
            "featureType": 1,
            "sources": [{ "sourceId": 1, "pageNumber": 23, "sourceType": 1 }],
            "affectedFeatureDefinitionKeys": [],
            "isCalledOut": false,
            "entityType": "racial-trait",
            "entityID": "72",
            "entityRaceId": 3,
            "entityRaceTypeId": 1743923279,
            "displayConfiguration": {
              "ABILITYSCORE": 1,
              "RACIALTRAIT": 1,
              "LANGUAGE": 0,
              "CLASSFEATURE": 0
            }
          }



        {
          "definition": {
            "id": 73,
            "definitionKey": "racial-trait:73",
            "entityTypeId": 1960452172,
            "displayOrder": 100,
            "name": "Ability Score Increase",
            "description": "<p>Your Intelligence score increases by 1.</p>",
            "snippet": "",
            "hideInBuilder": false,
            "hideInSheet": true,
            "activation": null,
            "sourceId": 1,
            "sourcePageNumber": 23,
            "creatureRules": [],
            "spellListIds": [],
            "featureType": 1,
            "sources": [{ "sourceId": 1, "pageNumber": 23, "sourceType": 1 }],
            "affectedFeatureDefinitionKeys": [],
            "isCalledOut": false,
            "entityType": "racial-trait",
            "entityID": "73",
            "entityRaceId": 1,
            "entityRaceTypeId": 1228963568,
            "displayConfiguration": {
              "ABILITYSCORE": 1,
              "RACIALTRAIT": 1,
              "LANGUAGE": 0,
              "CLASSFEATURE": 0
            }
          }
        }

		RESULTS IN: (BINDS ON ID TO COMPONENTNID)

DATA -> MODIFIERS -> RACE -> COMPONENTID = PREVID

        {
          "fixedValue": 1,
          "id": "1609",
          "entityId": 4,
          "entityTypeId": 1472902489,
          "type": "bonus",
          "subType": "intelligence-score",
          "dice": null,
          "restriction": "",
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Intelligence Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 1,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 5,
          "componentId": 73,
          "componentTypeId": 1960452172
        }


        {
          "fixedValue": 2,
          "id": "1608",
          "entityId": 2,
          "entityTypeId": 1472902489,
          "type": "bonus",
          "subType": "dexterity-score",
          "dice": null,
          "restriction": "",
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Dexterity Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 2,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 3,
          "componentId": 72,
          "componentTypeId": 1960452172
        },

        --------


           {
          "fixedValue": 1,
          "id": "1665",
          "entityId": null,
          "entityTypeId": null,
          "type": "bonus",
          "subType": "choose-an-ability-score",
          "dice": null,
          "restriction": null,
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Choose an Ability Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 1,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 695,
          "componentId": 56,
          "componentTypeId": 12168134
        },
        {
          "fixedValue": 1,
          "id": "1789",
          "entityId": null,
          "entityTypeId": null,
          "type": "bonus",
          "subType": "choose-an-ability-score",
          "dice": null,
          "restriction": null,
          "statId": null,
          "requiresAttunement": false,
          "duration": null,
          "friendlyTypeName": "Bonus",
          "friendlySubtypeName": "Choose an Ability Score",
          "isGranted": true,
          "bonusTypes": [],
          "value": 1,
          "availableToMulticlass": true,
          "modifierTypeId": 1,
          "modifierSubTypeId": 695,
          "componentId": 56,
          "componentTypeId": 12168134
        },


        ---

        