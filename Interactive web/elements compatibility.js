import React, { useState, useMemo } from 'react';
import { Flame, Volume2, Mountain, Wind, Sun, Leaf, Droplets, Skull, Zap, Snowflake, Diamond, Shield, Moon } from 'lucide-react';

const CharacterData = [
  {
    id: 1,
    name: "Liam Reed",
    element: "Fire",
    icon: Flame,
    color: "bg-red-500",
    description: "Classic and chaotic. Burn it all or warm your hands. Your choice.",
    personality: ["Adventurous", "Impulsive", "Inspiring"]
  },
  {
    id: 2,
    name: "Rowan Khanna",
    element: "Sound",
    icon: Volume2,
    color: "bg-purple-500",
    description: "Sonic booms, vibration waves, and the power to shatter eardrums and glass.",
    personality: ["Analytical", "Dependable", "Perfectionist"]
  },
  {
    id: 3,
    name: "Ben Copper",
    element: "Earth",
    icon: Mountain,
    color: "bg-amber-600",
    description: "Grounded power. Boulders, armor, and earthquakes included.",
    personality: ["Cautious", "Reflective", "Insightful"]
  },
  {
    id: 4,
    name: "Jae Kim",
    element: "Wind/Air",
    icon: Wind,
    color: "bg-cyan-400",
    description: "Slicing gusts, flight, and casually flipping tables without lifting a finger.",
    personality: ["Funny", "Optimistic", "Playful"]
  },
  {
    id: 5,
    name: "Penny Haywood",
    element: "Light",
    icon: Sun,
    color: "bg-yellow-400",
    description: "Blinding flashes, lasers, illusions, and holy judgment vibes.",
    personality: ["Outgoing", "Empowering", "Sociable"]
  },
  {
    id: 6,
    name: "Mayumi Sasaki",
    element: "Nature",
    icon: Leaf,
    color: "bg-green-500",
    description: "Vines, thorns, and plants that aren't vegan-friendly.",
    personality: ["Observant", "Thoughtful", "Loyal"]
  },
  {
    id: 7,
    name: "Chiara Lobosca",
    element: "Water",
    icon: Droplets,
    color: "bg-blue-500",
    description: "From gentle healing to crushing tidal waves. Hydration and devastation.",
    personality: ["Empathetic", "Nurturing", "Patient"]
  },
  {
    id: 8,
    name: "Tulip Karasu",
    element: "Poison",
    icon: Skull,
    color: "bg-green-700",
    description: "Venomous strikes, acidic blasts, and toxic clouds. Bad breath weaponized.",
    personality: ["Bold", "Independent", "Reckless"]
  },
  {
    id: 9,
    name: "Hayami Amamiya",
    element: "Lightning",
    icon: Zap,
    color: "bg-indigo-500",
    description: "Fast, furious, shocking, and destructive. Zeus would approve.",
    personality: ["Witty", "Realistic", "Charismatic"]
  },
  {
    id: 10,
    name: "Talbott Winger",
    element: "Ice",
    icon: Snowflake,
    color: "bg-cyan-200",
    description: "Cool under pressure. Freeze enemies, slide into battle, Elsa-style.",
    personality: ["Perceptive", "Wise", "Quiet"]
  },
  {
    id: 11,
    name: "Andre Egwu",
    element: "Crystal",
    icon: Diamond,
    color: "bg-pink-400",
    description: "Shards, prisms, armor, and reflect magic like a disco ball of doom.",
    personality: ["Hopeful", "Creative", "Romantic"]
  },
  {
    id: 12,
    name: "Barnaby Lee",
    element: "Metal",
    icon: Shield,
    color: "bg-gray-600",
    description: "Control steel, bend weapons, or just become a walking tank.",
    personality: ["Fair-minded", "Empathetic", "Peace-seeking"]
  },
  {
    id: 13,
    name: "Merula Snyde",
    element: "Shadow",
    icon: Moon,
    color: "bg-gray-800",
    description: "Cloak yourself in fear, teleport through shadows, or just brood in the corner.",
    personality: ["Unpredictable", "Competitive", "Mysterious"]
  }
];

const SynergyData = {
  "Fire-Sound": {
    type: "Amplification",
    name: "Sonic Explosion",
    description: "Sound waves carry explosive fire blasts, creating devastating sonic booms that burn and shatter simultaneously.",
    power: 9,
    compatibility: "High"
  },
  "Fire-Earth": {
    type: "Creation",
    name: "Molten Forge",
    description: "Earth manipulation creates volcanic eruptions and molten projectiles. Perfect for reshaping battlefields.",
    power: 8,
    compatibility: "High"
  },
  "Fire-Wind": {
    type: "Amplification",
    name: "Wildfire Storm",
    description: "Wind feeds flames into unstoppable infernos that can engulf entire areas in seconds.",
    power: 9,
    compatibility: "Excellent"
  },
  "Fire-Light": {
    type: "Fusion",
    name: "Solar Flare",
    description: "Blinding light combined with searing heat creates miniature suns that blind and burn.",
    power: 8,
    compatibility: "High"
  },
  "Fire-Nature": {
    type: "Conflict",
    name: "Controlled Burn",
    description: "Nature can resist fire, but together they create strategic burns that clear paths and regenerate stronger.",
    power: 6,
    compatibility: "Complex"
  },
  "Fire-Water": {
    type: "Opposition",
    name: "Steam Burst",
    description: "Classic opposites create scalding steam attacks, but require perfect timing to avoid canceling out.",
    power: 7,
    compatibility: "Challenging"
  },
  "Fire-Poison": {
    type: "Enhancement",
    name: "Toxic Inferno",
    description: "Fire spreads poisonous smoke and creates acidic flames that corrode as they burn.",
    power: 8,
    compatibility: "High"
  },
  "Fire-Lightning": {
    type: "Amplification",
    name: "Plasma Storm",
    description: "Lightning ignites the air while fire provides fuel, creating devastating plasma-like attacks.",
    power: 10,
    compatibility: "Excellent"
  },
  "Fire-Ice": {
    type: "Opposition",
    name: "Thermal Shock",
    description: "Rapid temperature changes shatter materials and create explosive steam. Timing is everything.",
    power: 7,
    compatibility: "Challenging"
  },
  "Fire-Crystal": {
    type: "Enhancement",
    name: "Prism Flame",
    description: "Crystals focus and split fire into laser-precise beams while fire enhances crystal cutting power.",
    power: 8,
    compatibility: "High"
  },
  "Fire-Metal": {
    type: "Creation",
    name: "Forge Master",
    description: "Fire shapes and strengthens metal, creating molten weapons and armor in real-time.",
    power: 8,
    compatibility: "High"
  },
  "Fire-Shadow": {
    type: "Balance",
    name: "Flame Shadow",
    description: "Fire illuminates while shadow conceals, creating disorienting attacks from unexpected angles.",
    power: 7,
    compatibility: "Moderate"
  },
  "Sound-Earth": {
    type: "Amplification",
    name: "Seismic Resonance",
    description: "Sound waves trigger earthquakes and can shatter stone with precise frequencies.",
    power: 9,
    compatibility: "Excellent"
  },
  "Sound-Wind": {
    type: "Amplification",
    name: "Sonic Hurricane",
    description: "Wind carries sound further and faster, creating area-wide sonic attacks.",
    power: 8,
    compatibility: "High"
  },
  "Sound-Light": {
    type: "Fusion",
    name: "Strobe Scream",
    description: "Pulsing lights synchronized with sound create overwhelming sensory attacks.",
    power: 7,
    compatibility: "High"
  },
  "Sound-Nature": {
    type: "Enhancement",
    name: "Nature's Call",
    description: "Sound can accelerate plant growth or cause plants to resonate and vibrate as weapons.",
    power: 6,
    compatibility: "Moderate"
  },
  "Sound-Water": {
    type: "Amplification",
    name: "Hydro Acoustics",
    description: "Water amplifies and focuses sound waves, creating underwater sonic attacks and tsunamis.",
    power: 8,
    compatibility: "High"
  },
  "Sound-Poison": {
    type: "Enhancement",
    name: "Toxic Frequency",
    description: "Sound waves spread poison gas faster and can make toxins more potent through vibration.",
    power: 7,
    compatibility: "High"
  },
  "Sound-Lightning": {
    type: "Amplification",
    name: "Thunder Strike",
    description: "Lightning creates natural thunder, and sound can guide electrical attacks with precision.",
    power: 9,
    compatibility: "Excellent"
  },
  "Sound-Ice": {
    type: "Enhancement",
    name: "Crystalline Resonance",
    description: "Sound can shatter ice strategically or make ice structures sing with deadly frequencies.",
    power: 7,
    compatibility: "High"
  },
  "Sound-Crystal": {
    type: "Amplification",
    name: "Harmonic Prism",
    description: "Crystals resonate with sound to create powerful harmonic attacks and sound-based illusions.",
    power: 9,
    compatibility: "Excellent"
  },
  "Sound-Metal": {
    type: "Enhancement",
    name: "Sonic Forge",
    description: "Sound waves can shape metal and create resonating metal weapons that amplify attacks.",
    power: 8,
    compatibility: "High"
  },
  "Sound-Shadow": {
    type: "Enhancement",
    name: "Silent Scream",
    description: "Shadows muffle sound for stealth, while sound can make shadows 'solid' through vibration.",
    power: 7,
    compatibility: "Moderate"
  },
  "Earth-Wind": {
    type: "Balance",
    name: "Dust Devil",
    description: "Wind lifts earth into blinding sandstorms and flying boulder attacks.",
    power: 7,
    compatibility: "High"
  },
  "Earth-Light": {
    type: "Enhancement",
    name: "Solar Geomancy",
    description: "Light helps plants grow from earth faster, while crystals in earth can focus light beams.",
    power: 6,
    compatibility: "Moderate"
  },
  "Earth-Nature": {
    type: "Synergy",
    name: "Living Landscape",
    description: "Perfect partnership - earth provides foundation while nature provides life and growth.",
    power: 9,
    compatibility: "Excellent"
  },
  "Earth-Water": {
    type: "Creation",
    name: "Mudslide Mastery",
    description: "Creates mud, quicksand, and can reshape landscapes. Defensive and offensive capabilities.",
    power: 8,
    compatibility: "High"
  },
  "Earth-Poison": {
    type: "Enhancement",
    name: "Toxic Terrain",
    description: "Earth can contain and spread poisons, creating contaminated zones and acidic ground.",
    power: 7,
    compatibility: "High"
  },
  "Earth-Lightning": {
    type: "Balance",
    name: "Grounding Strike",
    description: "Earth can ground lightning safely or channel it through the ground for surprise attacks.",
    power: 8,
    compatibility: "High"
  },
  "Earth-Ice": {
    type: "Enhancement",
    name: "Permafrost Power",
    description: "Frozen earth becomes incredibly hard, while ice can preserve earth structures longer.",
    power: 7,
    compatibility: "High"
  },
  "Earth-Crystal": {
    type: "Synergy",
    name: "Gemstone Garden",
    description: "Earth naturally forms crystals, creating defensive crystal armor and offensive crystal spikes.",
    power: 8,
    compatibility: "Excellent"
  },
  "Earth-Metal": {
    type: "Enhancement",
    name: "Ore Mastery",
    description: "Earth contains metals, allowing for extraction and combination of geological and metallic powers.",
    power: 8,
    compatibility: "High"
  },
  "Earth-Shadow": {
    type: "Enhancement",
    name: "Underground Network",
    description: "Shadows hide underground tunnels while earth provides secret passage networks.",
    power: 6,
    compatibility: "Moderate"
  },
  "Wind-Light": {
    type: "Enhancement",
    name: "Radiant Gale",
    description: "Wind can bend light and create prismatic attacks, while light can make wind visible and more precise.",
    power: 7,
    compatibility: "High"
  },
  "Wind-Nature": {
    type: "Synergy",
    name: "Storm Bloom",
    description: "Wind spreads seeds and pollen rapidly while nature provides guidance for wind direction.",
    power: 8,
    compatibility: "Excellent"
  },
  "Wind-Water": {
    type: "Amplification",
    name: "Hurricane Force",
    description: "Classic storm combination - wind drives water into devastating hurricanes and water spouts.",
    power: 9,
    compatibility: "Excellent"
  },
  "Wind-Poison": {
    type: "Amplification",
    name: "Toxic Cyclone",
    description: "Wind spreads poison over vast areas quickly, creating deadly gas clouds and contaminated storms.",
    power: 8,
    compatibility: "High"
  },
  "Wind-Lightning": {
    type: "Synergy",
    name: "Thunderstorm",
    description: "Natural storm powers - wind builds the storm while lightning provides the devastating strikes.",
    power: 10,
    compatibility: "Excellent"
  },
  "Wind-Ice": {
    type: "Amplification",
    name: "Blizzard Blast",
    description: "Wind carries ice and snow to create blinding blizzards and ice storms.",
    power: 8,
    compatibility: "High"
  },
  "Wind-Crystal": {
    type: "Enhancement",
    name: "Crystal Storm",
    description: "Wind launches crystal shards like bullets while crystals can channel wind into focused blasts.",
    power: 8,
    compatibility: "High"
  },
  "Wind-Metal": {
    type: "Enhancement",
    name: "Steel Tempest",
    description: "Wind launches metal projectiles and can make metal weapons fly with deadly precision.",
    power: 8,
    compatibility: "High"
  },
  "Wind-Shadow": {
    type: "Enhancement",
    name: "Shadow Gust",
    description: "Wind can carry shadows to new locations while shadows can hide wind attacks until impact.",
    power: 7,
    compatibility: "High"
  },
  "Light-Nature": {
    type: "Synergy",
    name: "Photosynthetic Burst",
    description: "Light accelerates plant growth exponentially, creating instant forests and super-charged plant attacks.",
    power: 8,
    compatibility: "Excellent"
  },
  "Light-Water": {
    type: "Enhancement",
    name: "Prismatic Waves",
    description: "Water refracts light into rainbow attacks while light can make water sparkle and disorient enemies.",
    power: 7,
    compatibility: "High"
  },
  "Light-Poison": {
    type: "Balance",
    name: "Purifying Radiance",
    description: "Light can neutralize some poisons, but poison can corrupt light into sickly, harmful radiation.",
    power: 6,
    compatibility: "Complex"
  },
  "Light-Lightning": {
    type: "Amplification",
    name: "Plasma Beam",
    description: "Light and electricity combine into devastating energy beams that can cut through almost anything.",
    power: 10,
    compatibility: "Excellent"
  },
  "Light-Ice": {
    type: "Enhancement",
    name: "Prism Freeze",
    description: "Ice can focus light into laser beams while light can make ice structures beautiful and blinding.",
    power: 7,
    compatibility: "High"
  },
  "Light-Crystal": {
    type: "Synergy",
    name: "Laser Light Show",
    description: "Perfect match - crystals focus and amplify light into precision laser attacks and dazzling displays.",
    power: 9,
    compatibility: "Excellent"
  },
  "Light-Metal": {
    type: "Enhancement",
    name: "Solar Forge",
    description: "Light can heat and shape metal while polished metal can reflect and redirect light attacks.",
    power: 7,
    compatibility: "High"
  },
  "Light-Shadow": {
    type: "Opposition",
    name: "Eclipse Balance",
    description: "Ultimate opposites that can either cancel each other out or create stunning light/dark contrasts.",
    power: 8,
    compatibility: "Challenging"
  },
  "Nature-Water": {
    type: "Synergy",
    name: "Life Stream",
    description: "Water nourishes plants while nature can purify and control water flow. Perfect life-giving combo.",
    power: 9,
    compatibility: "Excellent"
  },
  "Nature-Poison": {
    type: "Complex",
    name: "Toxic Garden",
    description: "Some plants are naturally poisonous. Nature can create deadly toxins or cure them.",
    power: 7,
    compatibility: "Complex"
  },
  "Nature-Lightning": {
    type: "Enhancement",
    name: "Charged Growth",
    description: "Lightning can stimulate plant growth rapidly, while plants can conduct electricity in surprising ways.",
    power: 7,
    compatibility: "Moderate"
  },
  "Nature-Ice": {
    type: "Balance",
    name: "Frost Garden",
    description: "Ice can preserve plants but also kill them. Together they create hardy, cold-resistant vegetation.",
    power: 6,
    compatibility: "Complex"
  },
  "Nature-Crystal": {
    type: "Enhancement",
    name: "Crystal Bloom",
    description: "Plants can grow around crystals for protection, while crystals can enhance plant-based magic.",
    power: 7,
    compatibility: "High"
  },
  "Nature-Metal": {
    type: "Balance",
    name: "Living Armor",
    description: "Plants can grow through metal for living armor, while metal can support and protect plant growth.",
    power: 7,
    compatibility: "Moderate"
  },
  "Nature-Shadow": {
    type: "Enhancement",
    name: "Dark Forest",
    description: "Shadows help plants hide and ambush, while thick plant growth creates natural shadow networks.",
    power: 7,
    compatibility: "High"
  },
  "Water-Poison": {
    type: "Enhancement",
    name: "Toxic Tide",
    description: "Water can dilute poisons or spread them rapidly. Creates contaminated water attacks.",
    power: 7,
    compatibility: "High"
  },
  "Water-Lightning": {
    type: "Amplification",
    name: "Electric Storm",
    description: "Water conducts electricity perfectly, creating electrified water attacks and chain lightning.",
    power: 9,
    compatibility: "Excellent"
  },
  "Water-Ice": {
    type: "Synergy",
    name: "Frozen Mastery",
    description: "Water becomes ice and vice versa. Complete control over all water states and temperatures.",
    power: 9,
    compatibility: "Excellent"
  },
  "Water-Crystal": {
    type: "Enhancement",
    name: "Crystal Clear",
    description: "Water can form crystal-clear ice structures while crystals can purify and focus water.",
    power: 7,
    compatibility: "High"
  },
  "Water-Metal": {
    type: "Balance",
    name: "Liquid Metal",
    description: "Water can rust metal but also cool it. Together they can create liquid metal attacks.",
    power: 6,
    compatibility: "Moderate"
  },
  "Water-Shadow": {
    type: "Enhancement",
    name: "Dark Depths",
    description: "Deep water creates natural shadows while shadows can hide underwater movements.",
    power: 6,
    compatibility: "Moderate"
  },
  "Poison-Lightning": {
    type: "Enhancement",
    name: "Toxic Shock",
    description: "Lightning can energize poisons making them more potent, while poison can corrupt electrical attacks.",
    power: 8,
    compatibility: "High"
  },
  "Poison-Ice": {
    type: "Enhancement",
    name: "Frozen Venom",
    description: "Ice can preserve poisons longer and create slow-release toxic attacks as it melts.",
    power: 7,
    compatibility: "High"
  },
  "Poison-Crystal": {
    type: "Enhancement",
    name: "Toxic Crystals",
    description: "Crystals can store and focus poison into concentrated doses or create poisonous crystal weapons.",
    power: 7,
    compatibility: "High"
  },
  "Poison-Metal": {
    type: "Enhancement",
    name: "Corroded Blades",
    description: "Poison can corrode metal, but together they create weapons that poison and cut simultaneously.",
    power: 8,
    compatibility: "High"
  },
  "Poison-Shadow": {
    type: "Synergy",
    name: "Venomous Darkness",
    description: "Both are associated with danger and stealth. Perfect for assassin-style surprise attacks.",
    power: 8,
    compatibility: "Excellent"
  },
  "Lightning-Ice": {
    type: "Balance",
    name: "Flash Freeze",
    description: "Lightning can instantly freeze water through shock cooling, while ice can store electrical charge.",
    power: 8,
    compatibility: "High"
  },
  "Lightning-Crystal": {
    type: "Enhancement",
    name: "Electric Prism",
    description: "Crystals can store and amplify electrical energy, creating devastating charged crystal attacks.",
    power: 9,
    compatibility: "Excellent"
  },
  "Lightning-Metal": {
    type: "Amplification",
    name: "Conductive Strike",
    description: "Metal conducts electricity perfectly, creating electrified weapons and chain lightning through metal.",
    power: 9,
    compatibility: "Excellent"
  },
  "Lightning-Shadow": {
    type: "Balance",
    name: "Shadow Strike",
    description: "Lightning illuminates briefly while shadow conceals. Creates surprise electrical attacks.",
    power: 7,
    compatibility: "Moderate"
  },
  "Ice-Crystal": {
    type: "Synergy",
    name: "Diamond Ice",
    description: "Ice is essentially water crystals. Together they create incredibly hard, beautiful, and deadly formations.",
    power: 8,
    compatibility: "Excellent"
  },
  "Ice-Metal": {
    type: "Enhancement",
    name: "Frozen Steel",
    description: "Cold makes metal brittle but also preserves it. Creates super-cooled metal weapons.",
    power: 7,
    compatibility: "High"
  },
  "Ice-Shadow": {
    type: "Enhancement",
    name: "Frost Shadow",
    description: "Ice creates cold mist that enhances shadows while shadows can hide ice attacks until impact.",
    power: 7,
    compatibility: "High"
  },
  "Crystal-Metal": {
    type: "Enhancement",
    name: "Crystalline Alloy",
    description: "Crystals can grow on metal and metal can be crystallized, creating incredibly strong hybrid materials.",
    power: 8,
    compatibility: "High"
  },
  "Crystal-Shadow": {
    type: "Balance",
    name: "Dark Prism",
    description: "Crystals reflect light while shadows absorb it. Creates disorienting light-bending attacks.",
    power: 7,
    compatibility: "Moderate"
  },
  "Metal-Shadow": {
    type: "Enhancement",
    name: "Shadow Blade",
    description: "Metal weapons can be hidden in shadows, while shadows can make metal weapons appear from nowhere.",
    power: 7,
    compatibility: "High"
  }
};

const ElementalSynergyExplorer = () => {
  const [selectedCharacters, setSelectedCharacters] = useState([]);
  const [hoveredCharacter, setHoveredCharacter] = useState(null);

  const toggleCharacter = (character) => {
    setSelectedCharacters(prev => {
      const isSelected = prev.some(c => c.id === character.id);
      if (isSelected) {
        return prev.filter(c => c.id !== character.id);
      } else if (prev.length < 4) {
        return [...prev, character];
      }
      return prev;
    });
  };

  const synergyResults = useMemo(() => {
    if (selectedCharacters.length < 2) return [];

    const results = [];
    for (let i = 0; i < selectedCharacters.length; i++) {
      for (let j = i + 1; j < selectedCharacters.length; j++) {
        const char1 = selectedCharacters[i];
        const char2 = selectedCharacters[j];
        const key1 = `${char1.element}-${char2.element}`;
        const key2 = `${char2.element}-${char1.element}`;
        
        const synergy = SynergyData[key1] || SynergyData[key2];
        if (synergy) {
          results.push({
            characters: [char1, char2],
            synergy,
            key: key1
          });
        }
      }
    }
    return results.sort((a, b) => b.synergy.power - a.synergy.power);
  }, [selectedCharacters]);

  const getCompatibilityColor = (compatibility) => {
    switch (compatibility) {
      case 'Excellent': return 'text-green-600 bg-green-100';
      case 'High': return 'text-blue-600 bg-blue-100';
      case 'Moderate': return 'text-yellow-600 bg-yellow-100';
      case 'Complex': return 'text-purple-600 bg-purple-100';
      case 'Challenging': return 'text-red-600 bg-red-100';
      default: return 'text-gray-600 bg-gray-100';
    }
  };

  const getPowerBars = (power) => {
    return Array.from({ length: 10 }, (_, i) => (
      <div
        key={i}
        className={`h-2 w-4 rounded-sm ${
          i < power ? 'bg-gradient-to-r from-yellow-400 to-red-500' : 'bg-gray-200'
        }`}
      />
    ));
  };

  return (
    <div className="max-w-7xl mx-auto p-6 bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 min-h-screen text-white">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent mb-2">
          Elemental Power Synergy Explorer
        </h1>
        <p className="text-gray-300 text-lg">
          Select up to 4 characters to discover how their elemental powers combine and interact
        </p>
      </div>

      {/* Character Selection Grid */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4 text-center">Choose Your Team</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
          {CharacterData.map((character) => {
            const Icon = character.icon;
            const isSelected = selectedCharacters.some(c => c.id === character.id);
            const isHovered = hoveredCharacter?.id === character.id;
            
            return (
              <div
                key={character.id}
                className={`relative cursor-pointer transition-all duration-300 transform ${
                  isSelected 
                    ? 'scale-105 ring-4 ring-purple-400 shadow-lg shadow-purple-500/50' 
                    : 'hover:scale-105 hover:shadow-lg'
                } ${
                  selectedCharacters.length >= 4 && !isSelected 
                    ? 'opacity-50 cursor-not-allowed' 
                    : ''
                }`}
                onClick={() => toggleCharacter(character)}
                onMouseEnter={() => setHoveredCharacter(character)}
                onMouseLeave={() => setHoveredCharacter(null)}
              >
                <div className={`${character.color} p-4 rounded-xl shadow-lg text-white relative overflow-hidden`}>
                  <div className="absolute inset-0 bg-gradient-to-br from-white/20 to-transparent"></div>
                  <div className="relative z-10">
                    <Icon className="w-8 h-8 mx-auto mb-2" />
                    <h3 className="font-semibold text-sm text-center mb-1">{character.name}</h3>
                    <p className="text-xs text-center opacity-90">{character.element}</p>
                  </div>
                  {isSelected && (
                    <div className="absolute top-2 right-2 bg-white text-purple-600 rounded-full w-6 h-6 flex items-center justify-center text-xs font-bold">
                      ✓
                    </div>
                  )}
                </div>
                
                {/* Hover tooltip */}
                {isHovered && (
                  <div className="absolute z-50 bottom-full left-1/2 transform -translate-x-1/2 mb-2 bg-black/90 text-white p-3 rounded-lg shadow-xl border border-gray-600 max-w-xs">
                    <p className="text-sm font-semibold mb-1">{character.element} Power</p>
                    <p className="text-xs mb-2">{character.description}</p>
                    <div className="flex flex-wrap gap-1">
                      {character.personality.slice(0, 3).map((trait, idx) => (
                        <span key={idx} className="text-xs bg-purple-600 px-2 py-1 rounded">
                          {trait}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Selected Characters Display */}
      {selectedCharacters.length > 0 && (
        <div className="mb-8">
          <h3 className="text-xl font-semibold mb-4 text-center">Selected Team</h3>
          <div className="flex justify-center gap-4 flex-wrap">
            {selectedCharacters.map((character) => {
              const Icon = character.icon;
              return (
                <div key={character.id} className="flex items-center gap-2 bg-slate-800 px-4 py-2 rounded-lg">
                  <Icon className={`w-5 h-5 ${character.color.replace('bg-', 'text-')}`} />
                  <span className="font-medium">{character.name}</span>
                  <span className="text-sm text-gray-400">({character.element})</span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Synergy Results */}
      {synergyResults.length > 0 && (
        <div className="space-y-6">
          <h2 className="text-2xl font-semibold text-center mb-6">Power Synergies</h2>
          {synergyResults.map((result, index) => {
            const [char1, char2] = result.characters;
            const Icon1 = char1.icon;
            const Icon2 = char2.icon;
            
            return (
              <div key={index} className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-xl p-6 shadow-xl">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2">
                      <div className={`${char1.color} p-2 rounded-lg`}>
                        <Icon1 className="w-6 h-6 text-white" />
                      </div>
                      <span className="font-semibold">{char1.name}</span>
                    </div>
                    <div className="text-2xl font-bold text-purple-400">+</div>
                    <div className="flex items-center gap-2">
                      <div className={`${char2.color} p-2 rounded-lg`}>
                        <Icon2 className="w-6 h-6 text-white" />
                      </div>
                      <span className="font-semibold">{char2.name}</span>
                    </div>
                  </div>
                  
                  <div className="text-right">
                    <div className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${getCompatibilityColor(result.synergy.compatibility)}`}>
                      {result.synergy.compatibility}
                    </div>
                  </div>
                </div>

                <div className="grid md:grid-cols-3 gap-6">
                  <div className="md:col-span-2">
                    <h3 className="text-xl font-bold text-purple-300 mb-2">{result.synergy.name}</h3>
                    <p className="text-gray-300 mb-3">{result.synergy.description}</p>
                    <div className="inline-block bg-gradient-to-r from-purple-600 to-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                      {result.synergy.type}
                    </div>
                  </div>
                  
                  <div className="space-y-3">
                    <div>
                      <div className="flex justify-between items-center mb-2">
                        <span className="text-sm font-medium text-gray-400">Power Level</span>
                        <span className="text-lg font-bold text-yellow-400">{result.synergy.power}/10</span>
                      </div>
                      <div className="flex gap-1">
                        {getPowerBars(result.synergy.power)}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {selectedCharacters.length === 0 && (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">⚡</div>
          <h3 className="text-xl font-semibold mb-2">Ready to Explore?</h3>
          <p className="text-gray-400">Select characters above to discover their elemental synergies!</p>
        </div>
      )}

      {selectedCharacters.length === 1 && (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">🔮</div>
          <h3 className="text-xl font-semibold mb-2">Choose Another Character</h3>
          <p className="text-gray-400">Select at least 2 characters to see how their powers combine!</p>
        </div>
      )}
    </div>
  );
};

export default ElementalSynergyExplorer;