import json
import api_pb2
from google.protobuf import json_format
import requests
from itertools import product
json_str = '''{
  "settings": {
    "iterations": 3000,
    "phase": 4,
    "showDamageMetrics": true,
    "showThreatMetrics": true,
    "language": "en",
    "faction": "Alliance",
    "filters": {
      "oneHandedWeapons": true,
      "twoHandedWeapons": true
    }
  },
  "raidBuffs": {
    "giftOfTheWild": "TristateEffectImproved",
    "powerWordFortitude": "TristateEffectImproved",
    "commandingShout": "TristateEffectImproved",
    "strengthOfEarthTotem": "TristateEffectImproved",
    "abominationsMight": true,
    "leaderOfThePack": "TristateEffectImproved",
    "icyTalons": true,
    "swiftRetribution": true,
    "moonkinAura": "TristateEffectImproved",
    "wrathOfAirTotem": true,
    "sanctifiedRetribution": true,
    "shadowProtection": true,
    "bloodlust": true,
    "thorns": "TristateEffectImproved",
    "devotionAura": "TristateEffectImproved",
    "stoneskinTotem": "TristateEffectImproved",
    "retributionAura": true
  },
  "debuffs": {
    "judgementOfLight": true,
    "misery": true,
    "faerieFire": "TristateEffectRegular",
    "ebonPlaguebringer": true,
    "heartOfTheCrusader": true,
    "shadowMastery": true,
    "savageCombat": true,
    "mangle": true,
    "exposeArmor": true,
    "vindication": true,
    "frostFever": "TristateEffectImproved",
    "insectSwarm": true
  },
  "tanks": [
    {
      "type": "Player"
    }
  ],
  "partyBuffs": {
  },
  "player": {
    "name": "Player",
    "race": "RaceUndead",
    "class": "ClassDeathknight",
    "equipment": {
      "items": [
        {"id":49986,"enchant":3812,"gems":[41380,40130]},
        {"id":50627,"gems":[40119]},
        {"id":51130,"enchant":3852,"gems":[40119]},
        {"id":50718,"enchant":3294,"gems":[40119]},
        {"id":51305,"enchant":3297,"gems":[40119,40119]},
        {"id":50611,"enchant":3850,"gems":[36767,36767]},
        {"id":51132,"enchant":3234,"gems":[40119,0]},
        {"id":43587,"gems":[40141,40167,42154]},
        {"id":51131,"enchant":3822,"gems":[40166,40119]},
        {"id":47430,"enchant":3232,"gems":[40119,40119]},
        {"id":50403},
        {"id":43582,"gems":[40118]},
        {"id":47735},
        {"id":47451},
        {"id":50738},
        {},
        {"id":47672}
      ]
    },
    "consumes": {
      "flask": "FlaskOfStoneblood",
      "food": "FoodBlackenedDragonfin",
      "defaultPotion": "IndestructiblePotion",
      "prepopPotion": "IndestructiblePotion",
      "defaultConjured": "ConjuredHealthstone",
      "thermalSapper": true,
      "fillerExplosive": "ExplosiveSaroniteBomb"
    },
    "bonusStats": {
      "stats": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      "pseudoStats": [0,0,0,0,0,0]
    },
    "buffs": {
      "blessingOfKings": true,
      "blessingOfMight": "TristateEffectImproved",
      "blessingOfSanctuary": true,
      "revitalizeRejuvination": 100,
      "tricksOfTheTrades": 1,
      "painSuppressions": 1,
      "handOfSacrifices": 3,
      "shatteringThrows": 1
    },
    "tankDeathknight": {
      "rotation": {
      },
      "options": {
      }
    },
    "talentsString": "005512153330030320102013-3050505000023-005",
    "glyphs": {
      "major1": 45805,
      "major2": 43550,
      "major3": 43554,
      "minor1": 43544,
      "minor2": 43535,
      "minor3": 43673
    },
    "profession1": "Blacksmithing",
    "profession2": "Jewelcrafting",
    "cooldowns": {
    },
    "rotation": {
      "type": "TypeAPL",
      "prepullActions": [
        {"action":{"castSpell":{"spellId":{"spellId":48263}}},"doAtValue":{"const":{"val":"-12s"}}},
        {"action":{"castSpell":{"spellId":{"otherId":"OtherActionPotion"}}},"doAtValue":{"const":{"val":"-1s"}}},
        {"action":{"castSpell":{"spellId":{"spellId":49938}}},"doAtValue":{"const":{"val":"0"}}}
      ],
      "priorityList": [
        {"action":{"condition":{"not":{"val":{"auraIsActive":{"auraId":{"itemId":40093}}}}},"castSpell":{"spellId":{"itemId":40093}}}},
        {"action":{"condition":{"auraIsActive":{"auraId":{"spellId":69409}}},"castSpell":{"spellId":{"spellId":49938}}}},
        {"action":{"condition":{"cmp":{"op":"OpLt","lhs":{"spellTimeToReady":{"spellId":{"spellId":49938}}},"rhs":{"const":{"val":"2"}}}},"strictSequence":{"actions":[{"castSpell":{"spellId":{"spellId":45529}}},{"castSpell":{"spellId":{"spellId":55233}}},{"castSpell":{"spellId":{"itemId":50361}}},{"castSpell":{"spellId":{"spellId":48707}}}]}}},
        {"action":{"condition":{"and":{"vals":[{"auraIsActive":{"auraId":{"spellId":69409}}},{"cmp":{"op":"OpLe","lhs":{"auraRemainingTime":{"auraId":{"spellId":69409}}},"rhs":{"const":{"val":"2"}}}},{"auraIsActive":{"auraId":{"spellId":55233}}}]}},"castSpell":{"spellId":{"spellId":6940,"tag":-1}}}},
        {"action":{"condition":{"and":{"vals":[{"cmp":{"op":"OpLt","lhs":{"spellTimeToReady":{"spellId":{"spellId":49938}}},"rhs":{"const":{"val":"2"}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":55233}}}}}]}},"castSpell":{"spellId":{"spellId":48792}}}},
        {"action":{"condition":{"and":{"vals":[{"auraIsActive":{"auraId":{"spellId":69409}}},{"cmp":{"op":"OpLe","lhs":{"auraRemainingTime":{"auraId":{"spellId":69409}}},"rhs":{"const":{"val":"2"}}}},{"auraIsActive":{"auraId":{"spellId":48792}}}]}},"castSpell":{"spellId":{"spellId":33206,"tag":-1}}}},
        {"action":{"condition":{"and":{"vals":[{"cmp":{"op":"OpLt","lhs":{"spellTimeToReady":{"spellId":{"spellId":49938}}},"rhs":{"const":{"val":"2"}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":55233}}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":48792}}}}}]}},"castSpell":{"spellId":{"spellId":33206,"tag":-1}}}},
        {"action":{"condition":{"and":{"vals":[{"auraIsActive":{"auraId":{"spellId":69409}}},{"cmp":{"op":"OpLe","lhs":{"auraRemainingTime":{"auraId":{"spellId":69409}}},"rhs":{"const":{"val":"2"}}}},{"auraIsActive":{"auraId":{"spellId":33206,"tag":-1}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":48792}}}}}]}},"castSpell":{"spellId":{"spellId":6940,"tag":-1}}}},
        {"action":{"condition":{"and":{"vals":[{"cmp":{"op":"OpLt","lhs":{"spellTimeToReady":{"spellId":{"spellId":49938}}},"rhs":{"const":{"val":"2"}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":55233}}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":48792}}}}},{"not":{"val":{"auraIsActive":{"auraId":{"spellId":33206,"tag":-1}}}}}]}},"castSpell":{"spellId":{"spellId":6940,"tag":-1}}}},
        {"action":{"condition":{"auraIsActive":{"auraId":{"spellId":69409}}},"castSpell":{"spellId":{"spellId":48707}}}},
        {"action":{"condition":{"cmp":{"op":"OpLe","lhs":{"currentHealthPercent":{}},"rhs":{"const":{"val":"60%"}}}},"castSpell":{"spellId":{"spellId":48982}}}},
        {"action":{"condition":{"cmp":{"op":"OpLe","lhs":{"currentHealthPercent":{}},"rhs":{"const":{"val":"60%"}}}},"castSpell":{"spellId":{"spellId":48743}}}},
        {"action":{"condition":{"cmp":{"op":"OpGt","lhs":{"currentRuneCount":{"runeType":"RuneBlood"}},"rhs":{"const":{"val":"1"}}}},"castSpell":{"spellId":{"spellId":49941}}}},
        {"action":{"condition":{"cmp":{"op":"OpGt","lhs":{"currentRuneCount":{"runeType":"RuneFrost"}},"rhs":{"const":{"val":"1"}}}},"castSpell":{"spellId":{"spellId":59131}}}},
        {"action":{"condition":{"cmp":{"op":"OpGt","lhs":{"currentRuneCount":{"runeType":"RuneUnholy"}},"rhs":{"const":{"val":"1"}}}},"castSpell":{"spellId":{"spellId":49921,"tag":1}}}}
      ]
    },
    "reactionTimeMs": 200,
    "inFrontOfTarget": true,
    "healingModel": {
      "hps": 30000,
      "cadenceSeconds": 0.3,
      "cadenceVariation": 1.2,
      "inspirationUptime": 0.99,
      "burstWindow": 5
    },
    "database": {
      "items": [],
      "enchants": [],
      "gems": []
    },
    "nibelungAverageCasts": 11
  },
  "encounter": {
    "duration": 118,
    "durationVariation": 5,
    "executeProportion20": 0.2,
    "executeProportion25": 0.25,
    "executeProportion35": 0.35,
    "targets": [
      {
        "id": 36853,
        "name": "Sindragosa (Heroic)",
        "level": 83,
        "mobType": "MobTypeUndead",
        "stats": [0,0,0,0,0,0,0,0,0,0,0,805,0,0,0,0,0,0,0,0,10643,0,0,0,76,0,0,0,46018500,0,0,0,0,0,0,0,0,0,0,0],
        "minBaseDamage": 88072,
        "damageSpread": 0.5,
        "swingSpeed": 1.5,
        "parryHaste": true,
        "suppressDodge": true,
        "targetInputs": [
          {
            "label": "Include Mystic Buffet",
            "tooltip": "Model the ramping magic damage taken debuff applied during Phase 3 of the encounter, in addition to the normal Phase 1 mechanics.",
            "boolValue": true
          }
        ]
      }
    ]
  },
  "epWeightsStats": {
    "stats": [1.2461098853830275,5.031968943671985,12.344458571320493,0,0,0,0,0.23035050796957587,-0.0008234163151713311,-0.2348918605704927,0,0,-0.19592902531839054,0,1.2959407486517347,0,-0.6218723962217892,0,0,0,1.4920985230288268,0,5.588964764032385,0,0,5.648659567106241,4.461590327660895,0,1,0,0,0,0,0.15481196215132206,0.8285365673346483,0,0,0,0,0],
    "pseudoStats": [0,0,0,0,0,0]
  },
  "epRatios": [
    0,
    0,
    1,
    1,
    0,
    0
  ],
  "tankRefStat": "StatHealth"
}'''
json_dict = json.loads(json_str)
full_db = json.load(open("../assets/database/db.json"))
item_db = {}
for v in full_db['items']:
  item_vals = {k: v.get(k) for k in ('id', 'name', 'stats', 'gemSockets', 'type', 'armorType', 'weaponType', 'socketBonus', 'setName', 'handType')}
  if item_vals['type'] == 1:
    item_vals['type'] = 'ItemTypeHead'
  elif item_vals['type'] == 2:
    item_vals['type'] = 'ItemTypeNeck'
  elif item_vals['type'] == 3:
    item_vals['type'] = 'ItemTypeShoulder'
  elif item_vals['type'] == 4:
    item_vals['type'] = 'ItemTypeBack'
  elif item_vals['type'] == 5:
    item_vals['type'] = 'ItemTypeChest'
  elif item_vals['type'] == 6:
    item_vals['type'] = 'ItemTypeWrist'
  elif item_vals['type'] == 7:
    item_vals['type'] = 'ItemTypeHands'
  elif item_vals['type'] == 8:
    item_vals['type'] = 'ItemTypeWaist'
  elif item_vals['type'] == 9:
    item_vals['type'] = 'ItemTypeLegs'
  elif item_vals['type'] == 10:
    item_vals['type'] = 'ItemTypeFeet'
  elif item_vals['type'] == 11:
    item_vals['type'] = 'ItemTypeFinger'
  elif item_vals['type'] == 12:
    item_vals['type'] = 'ItemTypeTrinket'
  elif item_vals['type'] == 13:
    item_vals['type'] = 'ItemTypeWeapon'

  if item_vals['armorType'] == 4:
    item_vals['armorType'] = 'ArmorTypePlate'

  if item_vals['weaponType'] == 1:
    item_vals['weaponType'] = 'WeaponTypeAxe'
  elif item_vals['weaponType'] == 2:
    item_vals['weaponType'] = 'WeaponTypeDagger'
  elif item_vals['weaponType'] == 3:
    item_vals['weaponType'] = 'WeaponTypeFist'
  elif item_vals['weaponType'] == 4:
    item_vals['weaponType'] = 'WeaponTypeMace'
  elif item_vals['weaponType'] == 5:
    item_vals['weaponType'] = 'WeaponTypeOffHand'
  elif item_vals['weaponType'] == 6:
    item_vals['weaponType'] = 'WeaponTypePolearm'
  elif item_vals['weaponType'] == 7:
    item_vals['weaponType'] = 'WeaponTypeShield'
  elif item_vals['weaponType'] == 8:
    item_vals['weaponType'] = 'WeaponTypeStaff'
  elif item_vals['weaponType'] == 9:
    item_vals['weaponType'] = 'WeaponTypeSword'

  if item_vals['handType'] == 1:
    item_vals['handType'] = 'HandTypeMainHand'
  elif item_vals['handType'] == 2:
    item_vals['handType'] = 'HandTypeOneHand'
  elif item_vals['handType'] == 3:
    item_vals['handType'] = 'HandTypeOffHand'
  elif item_vals['handType'] == 4:
    item_vals['handType'] = 'HandTypeTwoHand'
  item_db[v['id']] = item_vals
enchant_db = {v["effectId"]: {"effectId": v["effectId"], "stats": v["stats"]} for v in full_db["enchants"]}
gems_db = {v["id"]: {k: v.get(k) for k in ('id', 'name', 'color', 'stats')} for v in full_db["gems"]}
max_iterations = 30000
# item_options = {"slot1": ["item1", "item2"], "slot2": ["item1", "item2", "item3"]}
item_options = {"head": [50640, 51306]}
wowsims_slots = (
    'head', 'neck', 'shoulder', 'back', 'chest', 'wrist', 'hands', 'waist',
    'legs', 'feet', 'finger1', 'finger2', 'trinket1', 'trinket2',
    'weapon1', 'weapon2', 'ranged')
item_slots = list(item_options.keys())
combinations = list(product(*item_options.values()))
iterations = max_iterations // len(combinations)
rsr_dict = {
    "raid": {"parties": [
        {"players": [json_dict['player'], {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
        {"players": [{}, {}, {}, {}, {}], "buffs": {}},
      ],
      "numActiveParties": 5,
      "buffs": {},
      "debuffs": {},
      "tanks": [
            {
                "type": "Player"
            }
        ]
    },
    "encounter": json_dict["encounter"],
    "simOptions": {
        "iterations": 3000
    }
}
for combination in combinations:
  equipment = rsr_dict['raid']['parties'][0]['players'][0]['equipment']
  if not len(equipment['items']) == len(wowsims_slots):
    print("items is wrong length", len(equipment['items']), equipment['items'])
    break
  database = rsr_dict['raid']['parties'][0]['players'][0]["database"]
  db_items = []
  gem_ids = set()
  effect_ids = set()
  for slot, item in zip(wowsims_slots, equipment['items']):
    if slot in item_slots:
      # e.g. "head" in ("head", "legs")
      new_item_id = combination[item_slots.index(slot)]
      item["id"] = new_item_id
      new_item_gem_slots = len(item_db[new_item_id]['gemSockets'])
      item['gems'] = item['gems'][:new_item_gem_slots]
    gem_ids |= set(item.get('gems', []))
    effect_ids.add(item.get('enchant'))
    if 'id' in item:
      db_items.append({k: v for k, v in item_db[item['id']].items() if v})
  database['items'] = db_items
  database['gems'] = [gems_db[id] for id in gem_ids if id]
  database['enchants'] = [enchant_db[effect_id] for effect_id in effect_ids if effect_id]
  print(json.dumps(rsr_dict))
  rsr = api_pb2.RaidSimRequest()
  message = json_format.ParseDict(rsr_dict, rsr)
  response = requests.post("http://localhost:3333/raidSim", data=message.SerializeToString() , headers={"content_type": "application/x-protobuf"})
  print(response.content)
  # import pdb; pdb.set_trace()
  raid_sim_result = api_pb2.RaidSimResult()
  raid_sim_result.ParseFromString(response.content)
  result_dict = json_format.MessageToDict(raid_sim_result)
  player = result_dict['raidMetrics']['parties'][0]['players'][0]
  print("combination", combination)
  print("dps", player['dps']['avg'])
  # player['dtps']['avg']
  # player['threat']['avg']