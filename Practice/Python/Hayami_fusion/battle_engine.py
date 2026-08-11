import random
from characters import characters

# Convert character traits into numeric combat stats
def get_combat_stats(name):
    c = characters[name]
    group = c["group"]

    #Base stats by group
    group_stats = {
        "Analysts":  {"hp": 85,  "attack": 80, "defense": 70, "speed": 65, "special": 90},
        "Explorers": {"hp": 90,  "attack": 85, "defense": 65, "speed": 90, "special": 75},
        "Sentinels": {"hp": 100, "attack": 75, "defense": 90, "speed": 60, "special": 70},
        "Diplomats": {"hp": 80,  "attack": 70, "defense": 65, "speed": 70, "special": 95},     
    }

    #Induividual modifiers per character
    modifiers = {
        "paula":   {"attack": +5,  "special": +10, "speed": -5},
        "mica":    {"attack": +10, "special": +5,  "defense": -5},
        "hiromi":  {"special": +10, "defense": +5, "speed": -5},
        "gillian": {"attack": +15, "hp": +5,       "defense": -5},
        "hayami":  {"speed": +15,  "attack": +10,  "hp": -5},
        "shaye":   {"attack": +10, "speed": +10,   "defense": -10},
        "shiina":  {"special": +15, "defense": +5, "attack": -5},
        "theresa": {"special": +10, "speed": +10,  "defense": -10},
        "chiyo":   {"defense": +15, "attack": +5,  "special": -5},
        "shizuka": {"attack": +15, "special": +5,  "speed": -5},
        "mayumi":  {"defense": +20, "hp": +10,     "attack": -10},
        "lily":    {"special": +15, "speed": +5,   "defense": -5},
        "sonia":   {"special": +20, "speed": +5,   "attack": -10},
        "himiko":  {"special": +15, "attack": +5,  "defense": -5},
        "katie":   {"special": +20, "hp": -5,      "defense": -5},
        "emily":   {"speed": +15,  "special": +10, "defense": -10},        
    }

    stats = dict(group_stats[group])
    if name in modifiers:
        for stat, val in modifiers[name].items():
            stats[stat] += val
    return stats

#Generate a combat action for a character
def generate_action(name, stats, opponent_name, round_num):
    c = characters[name]
    power = c["power"]
    opp_name = characters[opponent_name]["full_name"].split()[0]
    mbti = c["mbti"].split()[0]

    # MBTI flavored action lines
    mbti_actions = {
        "INTP": [
            f"calculates the optimal weak point and deploys {power} with cold precision",
            f"deconstructs {opp_name}'s defensive pattern and exploits the gap with {power}",
            f"theorizes mid-fight and lands a {power} strike that shouldn't have worked — but did",
        ],
        "ENTP": [
            f"pivots completely mid-attack and catches {opp_name} off guard with {power}",
            f"argues with {opp_name} while deploying {power} from three angles simultaneously",
            f"adapts their {power} into a counter nobody expected, including them",
        ],
        "INTJ": [
            f"executes a pre-planned {power} sequence with mechanical efficiency",
            f"forces {opp_name} into a corner and deploys {power} with surgical calm",
            f"anticipated this moment four exchanges ago and lands {power} exactly on schedule",
        ],
        "ENTJ": [
            f"commands the space and drives {power} straight through {opp_name}'s defense",
            f"overwhelms {opp_name} with relentless {power} pressure",
            f"reads the battlefield instantly and delivers {power} from the dominant angle",
        ],
        "ISTP": [
            f"finds the single most efficient angle and deploys {power} without wasted motion",
            f"reads the physics of the fight and applies {power} exactly where it hurts most",
            f"says nothing and hits {opp_name} with {power} from a direction that made no sense",
        ],
        "ESTP": [
            f"charges forward and escalates with {power}, momentum building with every second",
            f"smirks and launches {power} before {opp_name} finishes processing the last hit",
            f"turns the fight into a street brawl and thrives — {power} lands hard",
        ],
        "ISFP": [
            f"senses the imbalance in {opp_name}'s stance and corrects it violently with {power}",
            f"moves with quiet precision and lands {power} at the exact point of vulnerability",
            f"disrupts {opp_name}'s rhythm with an unexpected {power} application",
        ],
        "ESFP": [
            f"reads {opp_name}'s energy in real time and fires {power} into the gap",
            f"turns the entire fight into a performance and lands {power} center stage",
            f"improvises a {power} combo that shouldn't work — it works",
        ],
        "ISTJ": [
            f"executes {power} with textbook precision, no deviation, no hesitation",
            f"follows the plan and delivers {power} exactly as intended",
            f"waits for {opp_name} to make the mistake, then punishes it with {power}",
        ],
        "ESTJ": [
            f"dominates the exchange and drives {power} through any resistance",
            f"takes control of the fight's tempo and lands {power} on her terms",
            f"refuses to yield ground and forces {power} through {opp_name}'s defense",
        ],
        "ISFJ": [
            f"absorbs the pressure and retaliates with {power} at the perfect moment",
            f"protects her position and strikes back with {power} when the opening appears",
            f"waits with quiet patience and delivers {power} precisely when it's needed most",
        ],
        "ESFJ": [
            f"reads the entire emotional tempo of the fight and lands {power} at peak impact",
            f"turns {opp_name}'s aggression against them with a perfectly timed {power}",
            f"grabs the momentum of the exchange and redirects it into {power}",
        ],
        "INFJ": [
            f"perceives {opp_name}'s intention before they move and intercepts with {power}",
            f"guides the fight toward this exact moment and delivers {power} with quiet certainty",
            f"reads something in {opp_name}'s eyes and deploys {power} before they act",
        ],
        "ENFJ": [
            f"inspires herself mid-fight and channels that energy straight into {power}",
            f"takes command of the exchange and lands {power} with complete authority",
            f"reads {opp_name}'s weakening resolve and strikes with {power} at the critical moment",
        ],
        "INFP": [
            f"digs into something deep and dangerous and erupts with {power}",
            f"feels the injustice of losing and converts it into a devastating {power} strike",
            f"gets quiet for one second and then hits {opp_name} with {power} harder than expected",
        ],
        "ENFP": [
            f"connects three unrelated ideas mid-fight and somehow lands {power} from all of them",
            f"pivots on pure instinct and finds {power} working in a way nobody planned",
            f"gets excited mid-exchange and overcommits to {power} — it lands anyway",
        ],
    }

    if mbti in mbti_actions:
        return random.choice(mbti_actions[mbti])
    return f"unleashes {power} with focused intensity"

#Calculate damage with variance
def calculate_damage(attacker_stats, defender_stats, is_special=False):
    if is_special:
        base = attacker_stats["special"] * 0.6
        defense_factor = defender_stats["defense"] * 0.2
    else:
        base = attacker_stats["special"] * 0.6
        defense_factor = defender_stats["defense"] * 0.3

    variance = random.uniform(0.8, 1.2)
    damage = max(5, (base - defense_factor) * variance)
    return round(damage, 1)

#Generate round commentary
def generate_commentary(attacker, defender, damage, defender_hp, is_critical=False):
    a_name = characters[attacker]["full_name"].split()[0]
    d_name = characters[defender]["full_name"].split()[0]
    a_mbti = characters[attacker]["mbti"].split()[0]
    d_mbti = characters[defender]["mbti"].split()[0]

    if is_critical:
        lines = [
            f"A devastating hit — {d_name} staggers visibly.",
            f"Critical! {d_name} barely holds their ground.",
            f"{a_name} finds the gap. That one landed deep.",
            f"Pinpoint precision from {a_name}. {d_name} felt that one.",
            f"{d_name} had no answer for that. Critical damage.",
            f"The crowd goes quiet. {d_name} is in trouble.",
        ]
    elif damage < 10:
        lines = [
            f"{d_name} absorbs most of it. Barely a scratch.",
            f"{d_name}'s defense holds firm. {a_name} needs a better angle.",
            f"Glancing hit. {d_name} doesn't even blink.",
            f"{a_name} lands the strike but {d_name} rolls with it.",
            f"Partial block from {d_name}. Minimal damage.",
        ]
    elif defender_hp < 20:
        lines = [
            f"{d_name} is running on empty. One more hit ends this.",
            f"The end is near for {d_name}. They're barely standing.",
            f"{d_name} refuses to go down. But they're fading fast.",
            f"Everything {d_name} has left is pride at this point.",
            f"{a_name} smells blood. {d_name} is almost done.",
            f"{d_name} is fighting on instinct now. Not much left.",
        ]
    elif defender_hp < 40:
        lines = [
            f"{d_name} is feeling the pressure now.",
            f"The momentum has shifted. {d_name} needs to turn this around.",
            f"{a_name} is pulling ahead. {d_name} is running out of options.",
            f"{d_name} takes the hit and recalculates. Things look grim.",
        ]
    else:
        lines = [
            f"{d_name} takes the hit but pushes forward.",
            f"Solid damage. {d_name} adjusts their stance.",
            f"{a_name} presses the advantage.",
            f"{d_name} absorbs the blow and holds their ground.",
            f"Clean hit from {a_name}. {d_name} responds with a look.",
            f"{d_name} winces but doesn't retreat.",
            f"The exchange favors {a_name} this round.",
        ]

    # Occasionally add MBTI flavor
    if random.random() > 0.65:
        mbti_flavor = {
            "INTJ": f" {d_name} was already recalculating.",
            "ENTP": f" {d_name} immediately starts adapting.",
            "ISTP": f" {d_name} files it away without expression.",
            "ENTJ": f" {d_name} refuses to show it hurt.",
            "ISFJ": f" {d_name} steadies themselves quietly.",
            "ESFP": f" {d_name} shakes it off with characteristic flair.",
            "INFP": f" Something in {d_name}'s eyes shifts dangerously.",
            "ESTP": f" {d_name} grins. They're just getting warmed up.",
        }
        if d_mbti in mbti_flavor:
            return random.choice(lines) + mbti_flavor[d_mbti]

    return random.choice(lines)

#Main battle simulation
def simulate_battle(name1, name2):
    stats1 = get_combat_stats(name1)
    stats2 = get_combat_stats(name2)

    hp1 = stats1["hp"]
    hp2 = stats2["hp"]

    c1 = characters[name1]
    c2 = characters[name2]

    log = []
    log.append(f"{'='*45}")
    log.append(f"  {c1['full_name']} ({c1['mbti'].split()[0]})")
    log.append(f"  vs")
    log.append(f"  {c2['full_name']} ({c2['mbti'].split()[0]})")
    log.append(f"{'='*45}\n")
    log.append(f"  HP: {c1['full_name'].split()[0]} {hp1} | {c2['full_name'].split()[0]} {hp2}\n")

    round_num = 1
    max_rounds = 20

    while hp1 > 0 and hp2 > 0 and round_num <= max_rounds:
        log.append(f"--- Round {round_num} ---")

        #Determine who goes first based on speed
        speed1 = stats1["speed"] + random.randint(-10,10)
        speed2 = stats2["speed"] + random.randint(-10,10)

        if speed1 >= speed2:
            first, second = name1, name2
            first_stats, second_stats = stats1, stats2
        else:
            first, second = name2, name1
            first_stats, second_stats = stats2, stats1

        #First attacker strike
        is_special = random.random() > 0.5
        is_critical = random.random() > 0.85
        damage = calculate_damage(first_stats, second_stats, is_special)
        if is_critical:
            damage *= 1.5
            damage = round(damage, 1)
        
        action = generate_action(first, first_stats, second, round_num)
        log.append(f"{characters[first]['full_name'].split()[0]} {action}.")

        if second == name1:
            hp1 -= damage
            hp1 = max(0, round(hp1, 1))
            commentary = generate_commentary(first, second, damage, hp1, is_critical)
            log.append(f"{commentary} (-{damage} HP)")
            log.append(f"HP: {c1['full_name'].split()[0]} {hp1} | {c2['full_name'].split()[0]} {hp2}\n")
        else:
            hp2 -= damage
            hp2 = max(0, round(hp2, 1))
            commentary = generate_commentary(first, second, damage, hp2, is_critical)
            log.append(f"{commentary} (-{damage} HP)")
            log.append(f"HP: {c1['full_name'].split()[0]} {hp1} | {c2['full_name'].split()[0]} {hp2}\n")

        #check if battle is over
        if hp1 <= 0 or hp2 <=0:
            break
        
        #second attacker strikes back
        is_special = random.random() > 0.5
        is_critical = random.random() > 0.85
        damage = calculate_damage(second_stats, first_stats, is_special)
        if is_critical:
            damage *= 1.5
            damage = round(damage, 1)
        
        action = generate_action(second, second_stats, first, round_num)
        log.append(f"{characters[second]['full_name'].split()[0]} {action}.")

        if second == name2:
            hp1 -= damage
            hp1 = max(0, round(hp1, 1))
            commentary = generate_commentary(second, first, damage, hp1, is_critical)
            log.append(f"{commentary} (-{damage} HP)")
            log.append(f"HP: {c1['full_name'].split()[0]} {hp1} | {c2['full_name'].split()[0]} {hp2}\n")
        else:
            hp2 -= damage
            hp2 = max(0, round(hp2, 1))
            commentary = generate_commentary(second, first, damage, hp2, is_critical)
            log.append(f"{commentary} (-{damage} HP)")
            log.append(f"HP: {c1['full_name'].split()[0]} {hp1} | {c2['full_name'].split()[0]} {hp2}\n")

        round_num += 1

    #Determine winner
    log.append(f"{'='*45}")
    if hp1 <= 0 and hp2 <= 0:
        log.append("DRAW! Both fighters fall simultaneously.")
    elif hp1 <= 0:
        log.append(f"WINNER: {c2['full_name']}!")
        log.append(f"{c2['full_name'].split()[0]} stands victorious.")
    elif hp2 <= 0:
        log.append(f"WINNER: {c1['full_name']}!")
        log.append(f"{c1['full_name'].split()[0]} stands victorious.")
    else:
        # Time limit reached
        if hp1 > hp2:
            log.append(f"TIME LIMIT! {c1['full_name']} wins on HP!")
        elif hp2 > hp1:
            log.append(f"TIME LIMIT! {c2['full_name']} wins on HP!")
        else:
            log.append("TIME LIMIT! It's a draw!")
    log.append(f"{'='*45}")

    return "\n". join(log)

# Hayami Fusion Battle Stats
fusion_battle_stats = {
    "Ashfall":     {"hp": 92, "attack": 88, "defense": 78, "speed": 65, "special": 82},
    "Aurora":      {"hp": 85, "attack": 75, "defense": 80, "speed": 88, "special": 97},
    "Briar":       {"hp": 88, "attack": 90, "defense": 65, "speed": 85, "special": 78},
    "Canopy":      {"hp": 87, "attack": 78, "defense": 72, "speed": 95, "special": 85},
    "Cyclar":      {"hp": 85, "attack": 80, "defense": 60, "speed": 99, "special": 92},
    "Emberstorm":  {"hp": 86, "attack": 88, "defense": 60, "speed": 97, "special": 80},
    "Flashgale":   {"hp": 84, "attack": 85, "defense": 58, "speed": 98, "special": 83},
    "FrostFire":   {"hp": 88, "attack": 87, "defense": 72, "speed": 78, "special": 88},
    "Glacier":     {"hp": 98, "attack": 88, "defense": 97, "speed": 50, "special": 85},
    "Hailstorm":   {"hp": 87, "attack": 92, "defense": 68, "speed": 95, "special": 88},
    "Ironleaf":    {"hp": 95, "attack": 88, "defense": 88, "speed": 62, "special": 95},
    "Mistveil":    {"hp": 85, "attack": 72, "defense": 76, "speed": 95, "special": 82},
    "Permaforst":  {"hp": 88, "attack": 78, "defense": 90, "speed": 72, "special": 85},
    "Rumble":      {"hp": 96, "attack": 95, "defense": 88, "speed": 60, "special": 85},
    "Scalding":    {"hp": 85, "attack": 95, "defense": 62, "speed": 97, "special": 85},
    "Solaris":     {"hp": 88, "attack": 93, "defense": 70, "speed": 90, "special": 95},
    "Sorn":        {"hp": 87, "attack": 80, "defense": 72, "speed": 88, "special": 95},
    "Stonegale":   {"hp": 95, "attack": 90, "defense": 85, "speed": 80, "special": 78},
    "Supra":       {"hp": 88, "attack": 97, "defense": 60, "speed": 99, "special": 98},
    "Thundervine": {"hp": 87, "attack": 88, "defense": 75, "speed": 88, "special": 90},
    "Verdant":     {"hp": 97, "attack": 82, "defense": 95, "speed": 55, "special": 85},
}

#fusion specific action lines
def generate_fusion_action(fusion_name, opponent_name):
    from fusion_calculator import fusion_details
    if fusion_name in fusion_details:
        moves = fusion_details[fusion_name]["moves"]
        move = random.choice(moves)
        move_name = move.split(" - ")[0]
        return f"uses {move_name}"
    return f"unleashes a powerful attack"

def simulate_fusion_battle(fusion1, fusion2):
    from fusion_calculator import fusion_details

    if fusion1 not in fusion_battle_stats or fusion2 not in fusion_battle_stats:
        return "Invalid fusion names."
    
    stats1 = dict(fusion_battle_stats[fusion1])
    stats2 = dict(fusion_battle_stats[fusion2])

    hp1 = stats1["hp"]
    hp2 = stats2["hp"]

    #Get personality flavor text
    p1_personality = ""
    p2_personality = ""
    if fusion1 in fusion_details:
        p1_personality = fusion_details[fusion1]["personality"][:80] + "..."
    if fusion2 in fusion_details:
        p2_personality = fusion_details[fusion2]["personality"][:80] + "..."

    log = []
    log.append(f"{'='*45}")
    log.append(f"  {fusion1} Hayami")
    log.append(f"  vs")
    log.append(f"  {fusion2} Hayami")
    log.append(f"{'='*45}")
    log.append(f"  Components: {fusion_details[fusion1]['components'] if fusion1 in fusion_details else '???'}")
    log.append(f"  vs {fusion_details[fusion2]['components'] if fusion2 in fusion_details else '???' }")
    log.append(f"\n  {fusion1}: {p1_personality}")
    log.append(f"\n  {fusion2}: {p2_personality}")
    log.append(f"\n  HP: {fusion1} {hp1} | {fusion2} {hp2}\n")

    round_num = 1
    max_rounds = 20

    while hp1 > 0 and hp2 > 0 and round_num <= max_rounds:
        log.append(f"--- Round {round_num} ---")

        # Speed check with variance
        speed1 = stats1["speed"] + random.randint(-10,10)
        speed2 = stats2["speed"] + random.randint(-10,10)

        if speed1 >= speed2:
            first, second = fusion1, fusion2
            first_stats, second_stats = stats1, stats2
        else:
            first, second = fusion2, fusion1
            first_stats, second_stats = stats2, stats1
        
        #First attacker
        is_special = random.random() > 0.5
        is_critical = random.random() > 0.85
        damage = calculate_damage(first_stats, second_stats, is_special)
        if is_critical:
            damage += 1.5
            damage = round(damage, 1)
        
        action = generate_fusion_action(first, second)
        crit_text = " CRITICAL HIT!" if is_critical else ""
        log.append(f"{first} Hayami {action}.{crit_text}")

        if first == fusion1:
            hp2 -= damage
            hp2 = max(0, round(hp2, 1))
            log.append(f"{second} takes {damage} damage.")
        else:
            hp1 -= damage
            hp1 = max(0, round(hp1, 1))
            log.append(f"{second} takes {damage} damage.")

        log.append(f"HP: {fusion1} {hp1} | {fusion2} {hp2}\n")

        if hp1 <= 0 or hp2 <= 0:
            break

        #Second attacker
        is_special = random.random() > 0.5
        is_critical = random.random() > 0.85
        damage = calculate_damage(second_stats, first_stats, is_special)
        if is_critical:
            damage *= 1.5
            damage = round(damage, 1)

        action = generate_fusion_action(second, first)
        crit_text = " CRITICAL HIT!" if is_critical else ""
        log.append(f"{second} Hayami {action}.{crit_text}")

        if second == fusion2:
            hp1 -= damage
            hp1 = max(0, round(hp1, 1))
            log.append(f"{first} takes {damage} damage.")
        else:
            hp2 -= damage
            hp2 = max(0, round(hp2, 1))
            log.append(f"{first} takes {damage} damage.")

        log.append(f"HP: {fusion1} {hp1} | {fusion2} {hp2}\n")

        round_num += 1
    
    #Winner
    log.append(f"{'='*45}")
    if hp1 <= 0 and hp2 <= 0:
        log.append("DRAW! Both fusions collapse simultaneously.")
    elif hp1 <= 0:
        log.append(f"WINNER: {fusion2} Hayami!")
    elif hp2 <= 0:
        log.append(f"WINNER: {fusion1} Hayami!")
    else:
        if hp1 > hp2:
            log.append(f"TIME LIMIT! {fusion1} Hayami wins on HP!")
        elif hp2 > hp1:
            log.append(f"TIME LIMIT! {fusion2} Hayami wins on HP!")
        else:
            log.append("TIME LIMIT! It's a draw!")
    log.append(f"{'='*45}")

    return "\n".join(log)

def calculate_tier_list():
    ranked = []
    for name in characters:
        stats = get_combat_stats(name)
        score = round(sum(stats.values()) / len(stats), 1)
        ranked.append((name, score, stats))
    
    # Sort by score descending
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked


def get_tier(score):
    if score >= 84:
        return "S"
    elif score >= 81:
        return "A"
    elif score >= 79:
        return "B"
    else:
        return "C"