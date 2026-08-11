from characters import characters
from file_manager import load_discovered, save_discovered 

#hayami's known elemental fusion
fusions = {
    ("earthquake", "blaze"): "Ashfall",
    ("ice", "solar"): "Aurora",
    ("blaze", "thorn"): "Briar",
    ("cyclone", "thorn"): "Canopy",
    ("cyclone", "solar"): "Cyclar",
    ("cyclone", "blaze"): "Emberstorm",
    ("thunderstorm", "cyclone"): "Flashgale",
    ("blaze", "ice"): "FrostFire",
    ("earthquake", "ice"): "Glacier",
    ("thunderstorm", "ice"): "Hailstorm",
    ("earthquake", "solar"): "Ironleaf",
    ("cyclone", "ice"): "Mistveil",
    ("ice", "thorn"): "Permaforst",
    ("earthquake", "thunderstorm"): "Rumble",
    ("thunderstorm", "blaze"): "Scalding",
    ("blaze", "solar"): "Solaris",
    ("thorn", "solar"): "Sorn",
    ("earthquake", "cyclone"): "Stonegale",
    ("thunderstorm", "solar"): "Supra",
    ("thunderstorm", "thorn"): "Thundervine",
    ("earthquake", "thorn"): "Verdant",
}

fusion_power = {
    "Ashfall": 78.75,
    "Aurora": 84.50,
    "Briar": 78.42,
    "Canopy": 80.83,
    "Cyclar": 83.33,
    "Emberstorm": 78.92,
    "Flashgale": 81.25,
    "FrostFire": 80.08,
    "Glacier": 82.33,
    "Hailstorm": 82.42,
    "Ironleaf": 83.17,
    "Mistveil": 82.50,
    "Permaforst": 82.00,
    "Rumble": 81.08,
    "Scalding": 78.83,
    "Solaris": 80.92,
    "Sorn": 82.83,
    "Stonegale": 81.17,
    "Supra": 83.25,
    "Thundervine": 80.75,
    "Verdant": 80.67,
}

#All valid elements
valid_elements = [
    "earth", "lightning", "wind", "fire", "water",
    "leaf", "light", "earthquake", "thunderstorm",
    "blaze", "cyclone", "ice", "thorn", "solar"
]

# Detailed fusion data
fusion_details = {
    "Ashfall": {
        "components": "Earthquake + Blaze",
        "personality": "Slow to act but catastrophic when they do. Earthquake's patience makes the explosion worse, not better. Enemies who've watched Ashfall stand still for ten seconds learn very quickly that the stillness was a wind-up.",
        "abilities": "Coats fists in superheated rock. Combines earth's weight with fire's explosion into single points of contact. Can fracture and ignite terrain simultaneously.",
        "moves": [
            "Magma Fist - coats fist in superheated rock and delivers a single devastating punch that erupts, sending molten debris outward in all directions",
            "Eruption Pillar - stomps the ground sending a fissure toward a target, erupting a pillar of burning rock from below that launches them skyward",
            "Ashfall Surger - raises both arms causing terrain to fracture and ignite simultaneously, blanketing the battlefield in flaming debris that continues to burn"
        ]
    },
    "Aurora": {
        "components": "Ice + Solar",
        "personality": "Breathtaking, almost otherworldly composure. Does not find you worth being angry at. Has calculated exactly how this fight ends and is allowing it to proceed at its natural pace purely because stopping it early would be beneath them. Every move is elegant.",
        "abilities": "Fires solar energy so cold it freezes rather than burns. Releases radial pulses of solar-chilled energy. Can compress solar energy to sub-zero temperatures.",
        "moves": [
            "Glacial Beam - fires a sustained beam of solar energy so cold it flash-freezes everything it touches in a clean precise line, fired with one hand the other in their pocket",
            "Frost Nova Burst - releases a radial pulse of solar-chilled energy, a wide blinding flash of cold white light that simultaneously blinds and freezes anyone in the radius",
            "Absolute Zero Flare - channels solar energy inward compressed to sub-zero temperatures then releases it in a catastrophic explosion of frozen light that flash-freezes the entire surrounding area"
        ]
    },
    "Briar": {
        "components": "Blaze + Thorn",
        "personality": "Chaotic, feral, and genuinely fun to watch from a safe distance. Fights like they're playing the world's most dangerous game and winning. Loud, reckless, laughs at their own attacks. There is no plan. There is only momentum.",
        "abilities": "Wields vines wreathed in fire. Can erupt fire and roots simultaneously from the ground. Creates prisons of burning bramble.",
        "moves": [
            "Blazing Thorn Whip - summons a long vine wreathed entirely in fire wielded as a whip that burns and lacerates simultaneously with massive range",
            "Wildfire Bloom - slams both hands into the ground erupting fire and roots simultaneously, plants ignite as they grow creating a spreading carpet of burning thorn-growth",
            "Inferno Thicket - conjures a dense wall of massive flaming thorned growth around a target, a prison of burning bramble that constricts inward"
        ]
    },
    "Canopy": {
        "components": "Cyclone + Thorn",
        "personality": "The most genuinely unhinged version of Hayami that is somehow also the most fun. Treats the entire fight like a jungle gym. Zips through the air on wind, drops carnivorous plants from above, and narrates their own chaos with unbridled enthusiasm.",
        "abilities": "Rides hoverboard with roots growing along its underside. Drops rapidly growing roots from above. Fires compressed seeds that explode into spinning carnivorous plants.",
        "moves": [
            "Aerial Root Drop - rides hoverboard high above and drops rapidly growing roots downward, by the time they reach the ground they crash like pillars spreading thorned vines everywhere",
            "Cyclone Seed - fires a compressed seed wrapped in a spinning wind current that embeds in the ground and explodes into a massive carnivorous plant that spins violently",
            "Canopy Vortex - generates a tornado seeded with thousands of razor leaves and thorned vines creating a spinning green tempest that shreds anything caught inside"
        ]
    },
    "Cyclar": {
        "components": "Solar + Cyclone",
        "personality": "Genuinely delightful and absolutely insufferable in equal measure. Fights with breathtaking elegance and knows it. Compliments your effort right before making you look ridiculous. The grace is real, the power is overwhelming, and they are having the absolute time of their life.",
        "abilities": "Manipulates light refraction through wind currents to create illusions and invisible strikes. Rides a golden glowing hoverboard.",
        "moves": [
            "Mirage Step - refracts light through wind currents creating multiple convincing afterimages that move independently, attacking from impossible angles and bowing theatrically after each strike",
            "Invisible Blade - focuses light refraction into a single compressed edge of wind, a cutting strike completely invisible until it lands. Cyclar announces it beforehand anyway",
            "Radiant Vortex - generates a massive tornado threaded with blinding solar light, enemies inside can't see or orient and are shredded by wind and photon energy simultaneously"
        ]
    },
    "Emberstorm": {
        "components": "Cyclone + Blaze",
        "personality": "Fights like a natural disaster with a personal grudge. Loud, fast, and everywhere at once. Doesn't stand still long enough to be hit, always moving, always burning, always angling for the next strike. Enemies report seeing fire trails in three directions at once.",
        "abilities": "Rides a fully aflame hoverboard. Leaves wide fire trails at extreme speed. Generates mobile spinning vortexes of fire and wind.",
        "moves": [
            "Firestorm Dash - ignites hoverboard and tears across the battlefield at extreme speed leaving a wide trail of fire, used to circle enemies or crash through them at full speed",
            "Ember Cyclone - generates a spinning vortex of fire and wind that chases targets at high speed while Emberstorm rides alongside directing it like a weapon",
            "Supercell Blaze - spins rapidly pulling fire and wind into a massive rotating firestorm that expands outward, incinerating everything in its radius while flinging flaming debris everywhere"
        ]
    },
    "Flashgale": {
        "components": "Thunderstorm + Cyclone",
        "personality": "Cannot be pinned down in any sense of the word. There, then not there, then behind you, then somewhere above you. The cold edge of Thunderstorm keeps the chaos just controlled enough to be surgical. Fighting them is deeply disorienting.",
        "abilities": "Moves with unpredictably fast direction changes mid-dash. Releases electrically charged wind. Rides a hoverboard wrapped in cyan lightning.",
        "moves": [
            "Static Gale - releases a burst of electrically charged wind, a blanket of numbing static that disrupts movement throws off footing and makes precise attacks nearly impossible",
            "Thunder Drift - combines Lightning Movement with aerial agility, moving unpredictably fast and changing direction mid-dash in ways that should be physically impossible",
            "Stormbreak - ascends on a column of wind, charges both hands with red lightning, then descends in a spiraling dive hitting the ground with a combined shockwave that craters the battlefield"
        ]
    },
    "FrostFire": {
        "components": "Ice + Blaze",
        "personality": "Genuinely unhinged in the most calculated way. Will freeze an enemy in place and then set the ice on fire while critiquing their fighting stance. Competitive and ruthless but weirdly analytical. The rage is always one second away from the logic.",
        "abilities": "Wields a Frost bow in one hand and a Fire arrow in the other. Burns enemies while freezing them simultaneously causing thermal shock damage.",
        "moves": [
            "Thermal Shock - simultaneously burns and freezes a target, the contradicting temperatures cause catastrophic cellular damage through direct touch or close-range dual blast",
            "Frost-Fired Arrow - fires a frost bow with a fire arrow that freezes the outer layer while igniting the interior, a prison of ice that burns from within",
            "Blizzard Pyre - generates a massive storm of simultaneously freezing and burning energy, a roaring vortex of fire and ice. FrostFire finds it funny that enemies can't defend against either"
        ]
    },
    "Glacier": {
        "components": "Ice + Earthquake",
        "personality": "Total unshakeable authority. Doesn't raise their voice. Has already assessed the situation, determined the most efficient outcome, and begun executing it. Regal, composed, and quietly terrifying. When Glacier moves it is because they have decided the fight is over.",
        "abilities": "Summons massive permafrost and rock constructs. Creates Ice Golems. Slides on ice terrain with the weight of a mountain behind their punches.",
        "moves": [
            "Permafrost Golem - constructs a massive golem of permafrost-reinforced stone harder than either material separately, enemies risk frostbite on contact. Summoned without looking",
            "Glacial Slam - coats fist in ice-compressed rock and punches the ground, simultaneously cracking the earth and flash-freezing everything the fissure touches",
            "Continental Lock - stomps the ground raising an enormous terrain of permafrost and rock across the battlefield making movement almost impossible. Glacier walks through it like they own it"
        ]
    },
    "Hailstorm": {
        "components": "Thunderstorm + Ice",
        "personality": "Absolutely zero patience for anything. Doesn't taunt. Doesn't monologue. Assesses, dismisses, and dismantles. Every move is faster than it should be and colder than it looks. The scariest thing is that they seem genuinely unbothered by the entire fight.",
        "abilities": "Manifests twin swords of ice-encased red lightning. Fires bolts of lightning that freeze mid-travel. Moves at lightning speed through self-generated blizzards.",
        "moves": [
            "Frost Blade - manifests twin swords of ice-encased red lightning, each strike simultaneously cuts shocks and flash-freezes the wound with precise economical movements",
            "Ice Bolt Snipe - fires a bolt of red lightning that freezes mid-travel arriving as a spear of electrified ice that shatters on impact, fragments electrocute while cold spreads from each shard",
            "Blizzard Execution - moves at lightning speed through a self-generated blizzard, invisible within it and striking from every direction. The cold slows reactions; the lightning ends them"
        ]
    },
    "Ironleaf": {
        "components": "Earthquake + Solar",
        "personality": "Profound, almost geological authority. Speaks rarely but when they do it lands like a proclamation. Has the strategic mind of Solar and the unshakeable calm of Earthquake. Has already won before you've processed that the fight has started. Not arrogant in the flashy sense. Just absolutely, quietly certain.",
        "abilities": "Raises solar-charged stone pillars that radiate heat and light. Delivers ground punches laced with solar energy. Creates solar-charged fortress walls nearly indestructible.",
        "moves": [
            "Solar Monolith - raises a massive pillar of solar-charged stone that radiates heat and light blinding nearby enemies, can be detonated remotely for a solar explosion",
            "Radiant Quake - delivers Earthquake's ground punch charged with solar energy, the shockwave radiates outward laced with blinding light and scorching heat burning the ground as it cracks it",
            "Fortress Sun - raises a full Fortress Field where every wall is solar-charged, glowing searingly bright and radiating heat intense enough to damage anyone who gets close"
        ]
    },
    "Mistveil": {
        "components": "Cyclone + Ice",
        "personality": "Deeply unbothered and slightly mischievous about it. Doesn't engage dramatically, simply isn't where you're looking. Disappears into their own fog, reappears somewhere inconvenient, freezes something important, and drifts away. Fighting them feels like arguing with the weather.",
        "abilities": "Exhales massive clouds of freezing fog. Rides an ice-covered hoverboard invisibly through their own mist. Merges full tornadoes with blizzards.",
        "moves": [
            "Frost Mist - exhales a massive cloud of freezing fog blanketing the battlefield, visibility drops to near zero and anyone moving through it has their limbs gradually numbed",
            "Phantom Drift - rides hoverboard through their own mist at high speed becoming effectively invisible, strikes then freezes the point of contact and vanishes back into the fog",
            "Blizzard Veil - merges a full tornado with a blizzard creating a massive opaque storm of wind and ice that batters blinds and freezes everything inside while Mistveil drifts through it serenely"
        ]
    },
    "Permaforst": {
        "components": "Ice + Thorn",
        "personality": "Quietly feral in the most composed way possible. Doesn't rush. Sets traps, freezes the exits, grows something carnivorous in the corner, then comments drily on how long it's taking you to notice. There's a childlike delight buried under the cynicism that surfaces when the plants do something particularly creative.",
        "abilities": "Summons vines that freeze instantly on contact with air. Creates rapid blooms of ice-preserved plants. Flash-freezes ground while erupting ice-hardened roots simultaneously.",
        "moves": [
            "Cryogenic Vine - summons vines that freeze instantly on contact with air, rigid and razor-edged they spread in branching fractal patterns trapping anything they touch",
            "Glacial Garden - causes a rapid bloom of massive ice-preserved plants across the battlefield, frozen trees crystalline thorns and immovable barriers that reshape the terrain completely",
            "Permafrost Snare - flash-freezes the ground in a wide radius while erupting ice-hardened roots through it, pinning targets in place. Escape requires breaking both. Permaforst remarks it seemed efficient"
        ]
    },
    "Rumble": {
        "components": "Earthquake + Thunderstorm",
        "personality": "Commands absolute fear without performing it. Not loud because they are angry. Loud because the ground shakes when they walk and lightning answers when they speak. Doesn't threaten, informs. Every word lands like the move that follows it.",
        "abilities": "Wields a massive hammer crackling with embedded red lightning. Drives hammer into ground to send fissures racing toward targets. Releases catastrophic combined seismic and electrical shockwaves.",
        "moves": [
            "Thunder Hammer - wields a massive hammer of compressed earth crackling with red lightning, the weight gives tectonic force and lightning discharges on impact. One hit changes the fight",
            "Seismic Bolt - drives the hammer into the ground sending a fissure racing toward the target, a pillar of red lightning erupts from the crack directly beneath their feet",
            "Tremble - plants both feet and releases full combined energy into the ground, a catastrophic shockwave of seismic force laced with red lightning that fractures the ground and launches everything in range"
        ]
    },
    "Scalding": {
        "components": "Thunderstorm + Blaze",
        "personality": "Terrifyingly fast and absolutely furious about it. Doesn't pace themselves. Identifies the target and closes the distance before the target has finished registering they've been identified. There is no de-escalation available here.",
        "abilities": "Ignites Thunder Blades with fire. Uses Lightning Movement to deliver burning slashes faster than the eye can follow. Moves at full speed across entire battlefields leaving fire and electricity behind.",
        "moves": [
            "Burning Blade Rush - ignites Thunder Blades with fire then uses Lightning Movement to tear through enemies in a single streak, rapid burning slashes delivered faster than the eye can follow",
            "Thunderfire Strike - delivers a single punch charged with both red lightning and concentrated fire, simultaneously an electrical discharge and a point-blank explosion",
            "Scorched Earth Blitz - moves at full speed across the entire battlefield striking every surface with burning lightning until everything in the arena is on fire electrified or both"
        ]
    },
    "Solaris": {
        "components": "Blaze + Solar",
        "personality": "Genuinely magnificent and completely aware of it. Fights like a performance. Every move is deliberate, every angle chosen for maximum visual impact. Solar's intelligence keeps them tactical but the passion is always there beneath the composure ready to turn a calculated strike into something enormous.",
        "abilities": "Hurls Fire Chakrams charged with solar energy at light-enhanced speed. Ignites entire body in concentrated solar fire for full-body charges. Rises on fire jets to drop miniature stars onto the battlefield.",
        "moves": [
            "Solar Chakram Blast - hurls Fire Chakrams charged with solar energy at light-enhanced speed, they strike with explosive solar force and return trailing fire, nearly impossible to avoid at range",
            "Corona Strike - ignites entire body in concentrated solar fire and charges forward, a full-body impact that hits like a meteor from a pre-calculated angle of maximum damage",
            "Stellar Inferno - rises into the air on fire jets, charges an enormous sphere of solar fire overhead and releases it, a miniature star that crashes into the battlefield with catastrophic incinerating force"
        ]
    },
    "Sorn": {
        "components": "Solar + Thorn",
        "personality": "Deeply disarming and somehow more unsettling than either alone. Speaks gently, moves gracefully, and genuinely seems sorry about what they're doing to you. The intelligence is real. The remorse is not. Every apology is sarcastic and condescending delivered with a smile that makes it worse.",
        "abilities": "High-speed vine attacks. Uses Solar's light to make Thorn's plants grow instantly to kaiju-sizes.",
        "moves": [
            "Solar Feed - floods a target area with concentrated solar light into the ground, plants erupt to kaiju-scale in seconds with a gentle wave of the hand and a murmured apology",
            "Photon Vine Whip - manifests vines threaded with solar energy that move at light-enhanced speed, burning and constricting simultaneously while Sorn quietly expresses regret",
            "Overgrowth Eclipse - releases a pulse of solar energy into the terrain triggering an explosive uncontrolled bloom, every plant grows to monstrous size consuming the battlefield. 'I really am sorry about this.'"
        ]
    },
    "Stonegale": {
        "components": "Earthquake + Cyclone",
        "personality": "Bewilderingly unpredictable for something that heavy. Relaxed, almost cheerful, and moves with a looseness that makes no sense given the scale of what they're doing. Will drop a twenty-ton boulder on you while humming. The chaos is real; so is the weight. Neither cancels the other out.",
        "abilities": "Tears chunks of rock and launches them at projectile velocity using wind. Generates massive rolling spheres of compressed rock. Rides the heaviest hoverboard made of rock formations.",
        "moves": [
            "Boulder Gale - tears chunks of rock from the ground and launches them at near-projectile velocity using concentrated wind, multiple at once from multiple directions",
            "Rolling Stone - generates a massive rolling sphere of compressed rock wind-propelled forward, gains speed as it travels redirectable mid-roll and hits like a wrecking ball that doesn't stop",
            "Avalanche Drive - raises massive quantities of earth and stone above the battlefield then releases everything at once in a wind-driven avalanche. Stonegale watches from above looking pleasantly surprised"
        ]
    },
    "Supra": {
        "components": "Thunderstorm + Solar",
        "personality": "The single most dangerous version of Hayami. Does not speak unless to tell you exactly how this ends. Has already run the numbers. There is no move you can make that they have not accounted for. The fight was over before it started; Supra is just finalizing the math.",
        "abilities": "Wields dual Eclipse Scythes. Moves as fast as light and fires blasts that seek targets automatically.",
        "moves": [
            "Eclipse Scythes - dual scythes forged from red lightning wrapped in solar energy that hum at a frequency destabilizing matter on contact, each swing calculated to be the last one necessary",
            "Lightspeed Execution - combines Light Jump with Thunderstorm's flash-step, movement that doesn't register as movement at all. Witnesses describe watching an outcome without seeing a cause",
            "Supernova Drive - charges both scythes with full solar and lightning output then releases everything in a single catastrophic forward explosion. Supra has already turned away before it lands"
        ]
    },
    "Thundervine": {
        "components": "Thunderstorm + Thorn",
        "personality": "Something that hunts. Doesn't announce themselves. Doesn't posture. Moves fast, sets things that grab you, and waits. The wildness of Thorn gives Thunderstorm's coldness an almost feral quality, patient the way a predator is patient. You won't see Thundervine until the vines are already moving.",
        "abilities": "Sends electrified roots racing at lightning speed. Saturates areas with electrically charged vines below ground. Releases massive networks of red-lightning-charged vines across entire battlefields.",
        "moves": [
            "Lightning Root - sends electrified roots racing along the ground at lightning speed, reaching a target before they can react and delivering a sustained electrical discharge simultaneously",
            "Static Thicket - saturates a wide area with electrically charged vines just below ground level, invisible until triggered and erupting upward to electrocute whatever activated the trap",
            "Thundervine Surge - releases a massive network of red-lightning-charged vines across the entire battlefield simultaneously, everything is reached grabbed and electrocuted at once"
        ]
    },
    "Verdant": {
        "components": "Earthquake + Thorn",
        "personality": "Something ancient and slightly terrifying in its gentleness. Warm, even kind, would prefer not to hurt you. But has the patience of geological time and the creativity of something that has watched things grow for centuries. Will wait. Will grow. And eventually everything in the area will belong to them.",
        "abilities": "Raises fortress walls interwoven with massive thorned roots that grow thicker over time. Plants hands in the ground to accelerate growth on a massive scale. Combines full ground manipulation with total plant eruption.",
        "moves": [
            "Root Fortress - raises a full Fortress Field where every wall is interwoven with massive thorned roots, harder than pure rock and actively constricting anything that touches it, walls grow thicker over time",
            "Ancient Growth - plants both hands in the ground accelerating growth on a massive scale, enormous ancient trees erupt roots crack the battlefield and the terrain transforms into a primordial forest within seconds",
            "World's Weight - combines Earthquake's full ground manipulation with Thorn's Forest Surge, earth fractures and rises while every plant erupts simultaneously reshaping the battlefield entirely"
        ]
    },
}

def show_characters(name):
    if name in characters:
        c = characters[name]
        print("\n" + "="*40)
        print(f"  {c['full_name']} ({c['pronouns']})")
        print("="*40)
        print(f"MBTI    : {c['mbti']}")
        print(f"Group   : {c['group']}")
        print(f"Height  : {c['height']}")
        print(f"\nPersonality (+): {', '.join(c['personality']['positive'])}")
        print(f"Personality (-): {', '.join(c['personality']['negative'])}")
        print(f"\nPower   : {c['power']}")
        print(f"Details : {c['power_description']}")
        print(f"\nAcademic : {c['stats']['academic']}")
        print(f"Social   : {c['stats']['social']}")
        print(f"Strategic: {c['stats']['strategic']}")
        print("\nHabits:")
        for habit in c["habits"]:
            print(f" - {habit}")
        print ("="*40)
    else:
        print(f"No character found name '{name}'.")

def get_fusion(element1, element2):
    e1 = element1.lower()
    e2 = element2.lower()

    if e1 not in valid_elements:
        return f"'{e1}' is not a valid element. Check your spelling."
    if e2 not in valid_elements:
        return f"'{e2}' is not a valid element. Check your spelling."
    
    combo = (e1, e2)
    reverse_combo = (e2, e1)

    if combo in fusions:
        return fusions[combo]
    elif reverse_combo in fusions:
        return fusions[reverse_combo]
    else:
        return "No fusion discovered yet for those elements."
    
def show_details(fusion_name):
    if fusion_name in fusion_details:
        details = fusion_details[fusion_name]
        print("\n" + "="*40)
        print(f" {fusion_name} Hayami")
        print("="*40)
        print(f"Components : {details['components']}")
        print(f"Personality : {details['personality']}")
        print(f"Abilities : {details['abilities']}")
        print("\nSignature Moves:")
        for move in details["moves"]:
            print(f" - {move}")
        print("="*40)

if __name__ == "__main__":
    print("Welcome to the Hayami Fusion Calculator!")
    print("---------------------------------------")

    #Track fusions discovered this session
    discovered = load_discovered()

    while True:
        print("\nOptions: [fusion] [character] [quit]")
        choice = input("What would you like to do? ").lower()
        
        if choice == "quit":
            save_discovered(discovered)
            if discovered:
                print("\nFusions discovered so far: ")
                for fusion in discovered:
                    print(f" - {fusion}")
            print("Closing the calculator. See you next time!")
            break

        elif choice == "fusion":
            element1 = input("Enter the first element: ")
            if element1.lower() in [e.lower() for e in valid_elements]:
                element2 = input("Enter the second element: ")
                result = get_fusion(element1, element2)
                if result in fusion_details:
                    if result not in discovered:
                        print(f"\n*** New fusion discovered: {result} Hayami! ***")
                    discovered.add(result)
                    show_details(result)
                else:
                    print("Result: " + result)
            else:
                print(f"'{element1}' is not a valid element!")
        
        elif choice == "character":
            name = input("Enter character name: ").lower()
            show_characters(name)

        else:
            print("Invalid option")