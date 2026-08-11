import React, { useState, useEffect } from 'react';
import { Users, Zap, Heart, Swords, AlertTriangle, CheckCircle, XCircle } from 'lucide-react';

const characters = [
  {
    name: "Liam Reed",
    role: "The Explorer",
    element: "Fire",
    personality: ["Adventurous", "Curious", "Inspiring", "Impulsive", "Restless", "Spontaneous"],
    relationships: {
      bestFriends: ["Rowan", "Jae"],
      closeFriends: ["Ben", "Jae"],
      rivalries: ["Merula"],
      romanticInterest: ["Rowan", "Merula"]
    }
  },
  {
    name: "Rowan Khanna",
    role: "The Brain",
    element: "Sound",
    personality: ["Analytical", "Knowledgeable", "Dependable", "Know-It-All", "Detached", "Perfectionist"],
    relationships: {
      bestFriends: ["Liam", "Ben"],
      closeFriends: ["Ben", "Jae"],
      rivalries: ["Talbott", "Liam"],
      romanticInterest: ["Liam", "Ben"]
    }
  },
  {
    name: "Ben Copper",
    role: "The Overthinker",
    element: "Earth",
    personality: ["Insightful", "Cautious", "Reflective", "Indecisive", "Anxious", "Self-Critical"],
    relationships: {
      bestFriends: ["Rowan"],
      closeFriends: ["Liam", "Jae", "Barnaby"],
      romanticInterest: ["Rowan", "Barnaby"]
    }
  },
  {
    name: "Jae Kim",
    role: "The Comic Relief",
    element: "Wind/Air",
    personality: ["Funny", "Optimistic", "Opportunistic", "Avoidant", "Inappropriate", "Playful"],
    relationships: {
      bestFriends: ["Liam"],
      closeFriends: ["Ben", "Rowan", "Penny"],
      rivalries: ["Merula"],
      romanticInterest: ["Liam", "Merula"]
    }
  },
  {
    name: "Penny Haywood",
    role: "The Connector",
    element: "Light",
    personality: ["Outgoing", "Sociable", "Empowering", "Nosy", "FOMO-prone", "Talkative"],
    relationships: {
      bestFriends: ["Mayumi"],
      closeFriends: ["Chiara", "Jae", "Barnaby"],
      romanticInterest: ["Mayumi", "Barnaby"]
    }
  },
  {
    name: "Mayumi Sasaki",
    role: "The Shy One",
    element: "Nature",
    personality: ["Observant", "Thoughtful", "Loyal", "Withdrawn", "Self-doubting", "Soft-spoken"],
    relationships: {
      bestFriends: ["Penny", "Chiara"],
      closeFriends: ["Barnaby"],
      romanticInterest: ["Penny", "Chiara"]
    }
  },
  {
    name: "Chiara Lobosca",
    role: "The Caregiver",
    element: "Water",
    personality: ["Empathetic", "Supportive", "Patient", "Self-Sacrificing", "Overprotective", "Nurturing"],
    relationships: {
      bestFriends: ["Mayumi"],
      closeFriends: ["Penny", "Barnaby"],
      romanticInterest: ["Mayumi"]
    }
  },
  {
    name: "Tulip Karasu",
    role: "The Rebel",
    element: "Poison",
    personality: ["Confident", "Independent", "Bold", "Stubborn", "Reckless", "Blunt"],
    relationships: {
      bestFriends: ["Hayami"],
      closeFriends: ["Andre", "Talbott"],
      rivalries: ["Hayami"],
      dislikes: ["Merula"],
      romanticInterest: ["Hayami"]
    }
  },
  {
    name: "Hayami Amamiya",
    role: "The Cynic",
    element: "Lightning",
    personality: ["Realistic", "Witty", "Loyal", "Distrustful", "Pessimistic", "Blunt"],
    relationships: {
      bestFriends: ["Tulip"],
      closeFriends: ["Talbott", "Andre"],
      rivalries: ["Tulip"],
      dislikes: ["Merula"],
      romanticInterest: ["Tulip"]
    }
  },
  {
    name: "Talbott Winger",
    role: "The Observer",
    element: "Ice",
    personality: ["Perceptive", "Wise", "Nonjudgmental", "Passive", "Distant", "Quiet"],
    relationships: {
      bestFriends: ["Andre"],
      closeFriends: ["Hayami", "Tulip"],
      rivalries: ["Rowan"],
      dislikes: ["Merula"],
      romanticInterest: ["Andre"]
    }
  },
  {
    name: "Andre Egwu",
    role: "The Romantic",
    element: "Crystal",
    personality: ["Hopeful", "Compassionate", "Creative", "Idealistic", "Overemotional", "Sentimental"],
    relationships: {
      bestFriends: ["Talbott"],
      closeFriends: ["Tulip", "Hayami"],
      romanticInterest: ["Talbott"]
    }
  },
  {
    name: "Barnaby Lee",
    role: "The Mediator",
    element: "Metal",
    personality: ["Naive", "Fair-minded", "Empathetic", "Conflict-Avoidant", "Overburdened", "Peace-Seeking"],
    relationships: {
      bestFriends: ["Mayumi"],
      closeFriends: ["Ben", "Chiara", "Penny"],
      romanticInterest: ["Ben", "Penny"]
    }
  },
  {
    name: "Merula Snyde",
    role: "The Wild Card",
    element: "Shadow",
    personality: ["Unpredictable", "Prideful", "Competitive", "Antagonistic", "Unreliable", "Impulsive"],
    relationships: {
      closeFriends: ["Jae"],
      rivalries: ["Liam", "Jae", "Tulip", "Hayami", "Talbott"],
      romanticInterest: ["Liam", "Jae"]
    }
  }
];

const scenarios = [
  {
    id: 1,
    title: "Planning a Dangerous Mission",
    description: "The group needs to infiltrate an enemy stronghold. Leadership, strategy, and trust are crucial.",
    keyFactors: ["leadership", "strategy", "trust", "courage"]
  },
  {
    id: 2,
    title: "Resolving Internal Conflict",
    description: "Two group members are in a heated argument that's affecting team morale.",
    keyFactors: ["mediation", "empathy", "communication", "diplomacy"]
  },
  {
    id: 3,
    title: "Exploring Unknown Territory",
    description: "The team discovers a mysterious new realm full of dangers and wonders.",
    keyFactors: ["curiosity", "caution", "adaptability", "observation"]
  },
  {
    id: 4,
    title: "Resource Crisis",
    description: "Supplies are running low and difficult decisions need to be made about rationing.",
    keyFactors: ["fairness", "practicality", "sacrifice", "leadership"]
  },
  {
    id: 5,
    title: "Moral Dilemma",
    description: "The group faces a choice between what's easy and what's right.",
    keyFactors: ["morality", "conviction", "support", "wisdom"]
  },
  {
    id: 6,
    title: "Celebration Planning",
    description: "After a major victory, the team wants to celebrate and bond together.",
    keyFactors: ["social", "inclusion", "fun", "bonding"]
  }
];

const GroupDynamicSimulator = () => {
  const [selectedCharacters, setSelectedCharacters] = useState([]);
  const [selectedScenario, setSelectedScenario] = useState(scenarios[0]);
  const [dynamicAnalysis, setDynamicAnalysis] = useState(null);

  const toggleCharacter = (character) => {
    setSelectedCharacters(prev => {
      const isSelected = prev.some(c => c.name === character.name);
      if (isSelected) {
        return prev.filter(c => c.name !== character.name);
      } else if (prev.length < 6) {
        return [...prev, character];
      }
      return prev;
    });
  };

  const analyzeGroupDynamic = () => {
    if (selectedCharacters.length < 2) return;

    const analysis = {
      leadership: [],
      conflicts: [],
      synergies: [],
      romanticTension: [],
      overallDynamic: "",
      successLikelihood: 0,
      keyStrengths: [],
      potentialIssues: []
    };

    // Analyze leadership potential
    const leaders = selectedCharacters.filter(c => 
      c.role === "The Explorer" || c.role === "The Brain" || c.role === "The Connector"
    );
    analysis.leadership = leaders.map(c => c.name);

    // Find conflicts
    selectedCharacters.forEach(char1 => {
      selectedCharacters.forEach(char2 => {
        if (char1.name !== char2.name) {
          if (char1.relationships.rivalries?.includes(char2.name.split(' ')[0]) ||
              char1.relationships.dislikes?.includes(char2.name.split(' ')[0])) {
            analysis.conflicts.push(`${char1.name} vs ${char2.name}`);
          }
        }
      });
    });

    // Find synergies (best friends, close friends)
    selectedCharacters.forEach(char1 => {
      selectedCharacters.forEach(char2 => {
        if (char1.name !== char2.name) {
          const firstName2 = char2.name.split(' ')[0];
          if (char1.relationships.bestFriends?.includes(firstName2) ||
              char1.relationships.closeFriends?.includes(firstName2)) {
            const synergy = `${char1.name} & ${char2.name}`;
            if (!analysis.synergies.includes(synergy) && 
                !analysis.synergies.includes(`${char2.name} & ${char1.name}`)) {
              analysis.synergies.push(synergy);
            }
          }
        }
      });
    });

    // Find romantic tension
    selectedCharacters.forEach(char1 => {
      selectedCharacters.forEach(char2 => {
        if (char1.name !== char2.name) {
          const firstName2 = char2.name.split(' ')[0];
          if (char1.relationships.romanticInterest?.includes(firstName2)) {
            const tension = `${char1.name} → ${char2.name}`;
            if (!analysis.romanticTension.includes(tension)) {
              analysis.romanticTension.push(tension);
            }
          }
        }
      });
    });

    // Calculate success likelihood based on scenario
    let successScore = 50;
    const roles = selectedCharacters.map(c => c.role);
    
    // Scenario-specific bonuses
    if (selectedScenario.keyFactors.includes('leadership') && leaders.length > 0) successScore += 15;
    if (selectedScenario.keyFactors.includes('mediation') && roles.includes('The Mediator')) successScore += 20;
    if (selectedScenario.keyFactors.includes('strategy') && roles.includes('The Brain')) successScore += 15;
    if (selectedScenario.keyFactors.includes('curiosity') && roles.includes('The Explorer')) successScore += 15;
    if (selectedScenario.keyFactors.includes('empathy') && roles.includes('The Caregiver')) successScore += 15;
    
    // Penalties for conflicts
    successScore -= analysis.conflicts.length * 10;
    
    // Bonuses for synergies
    successScore += analysis.synergies.length * 5;
    
    // Romantic tension can be good or bad
    if (analysis.romanticTension.length > 0 && selectedScenario.keyFactors.includes('social')) {
      successScore += 10;
    } else if (analysis.romanticTension.length > 2) {
      successScore -= 10;
    }

    analysis.successLikelihood = Math.max(0, Math.min(100, successScore));

    // Determine overall dynamic
    if (analysis.conflicts.length > 2) {
      analysis.overallDynamic = "Chaotic - High conflict potential";
    } else if (analysis.synergies.length > 3) {
      analysis.overallDynamic = "Harmonious - Strong team cohesion";
    } else if (analysis.romanticTension.length > 1) {
      analysis.overallDynamic = "Dramatic - Emotional complexity";
    } else {
      analysis.overallDynamic = "Balanced - Moderate dynamics";
    }

    // Key strengths
    const roleCount = {};
    selectedCharacters.forEach(c => {
      roleCount[c.role] = (roleCount[c.role] || 0) + 1;
    });
    
    Object.keys(roleCount).forEach(role => {
      if (roleCount[role] > 0) {
        analysis.keyStrengths.push(role);
      }
    });

    // Potential issues
    if (analysis.conflicts.length > 0) analysis.potentialIssues.push("Internal conflicts may cause friction");
    if (leaders.length === 0) analysis.potentialIssues.push("Lack of clear leadership");
    if (leaders.length > 2) analysis.potentialIssues.push("Too many potential leaders - power struggles possible");
    if (selectedCharacters.some(c => c.name === "Merula Snyde")) analysis.potentialIssues.push("Merula's unpredictability could disrupt plans");

    setDynamicAnalysis(analysis);
  };

  useEffect(() => {
    if (selectedCharacters.length >= 2) {
      analyzeGroupDynamic();
    } else {
      setDynamicAnalysis(null);
    }
  }, [selectedCharacters, selectedScenario]);

  const getSuccessColor = (likelihood) => {
    if (likelihood >= 70) return "text-green-600";
    if (likelihood >= 40) return "text-yellow-600";
    return "text-red-600";
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-purple-50 to-blue-50 min-h-screen">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Group Dynamic Simulator</h1>
        <p className="text-gray-600">Select characters and scenarios to explore how they work together</p>
      </div>

      {/* Scenario Selection */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-2xl font-semibold mb-4 flex items-center">
          <AlertTriangle className="mr-2 text-orange-500" />
          Choose Your Scenario
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {scenarios.map(scenario => (
            <div
              key={scenario.id}
              onClick={() => setSelectedScenario(scenario)}
              className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                selectedScenario.id === scenario.id 
                  ? 'border-purple-500 bg-purple-50' 
                  : 'border-gray-200 hover:border-purple-300'
              }`}
            >
              <h3 className="font-semibold text-gray-800 mb-2">{scenario.title}</h3>
              <p className="text-sm text-gray-600">{scenario.description}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Character Selection */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-2xl font-semibold mb-4 flex items-center">
          <Users className="mr-2 text-blue-500" />
          Select Your Team (2-6 characters)
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {characters.map(character => {
            const isSelected = selectedCharacters.some(c => c.name === character.name);
            return (
              <div
                key={character.name}
                onClick={() => toggleCharacter(character)}
                className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                  isSelected 
                    ? 'border-blue-500 bg-blue-50' 
                    : 'border-gray-200 hover:border-blue-300'
                } ${selectedCharacters.length >= 6 && !isSelected ? 'opacity-50 cursor-not-allowed' : ''}`}
              >
                <div className="flex items-center justify-between mb-2">
                  <h3 className="font-semibold text-gray-800">{character.name}</h3>
                  {isSelected && <CheckCircle className="text-blue-500 w-5 h-5" />}
                </div>
                <p className="text-sm text-purple-600 mb-1">{character.role}</p>
                <p className="text-xs text-gray-500">Element: {character.element}</p>
              </div>
            );
          })}
        </div>
        <div className="mt-4 text-center text-gray-600">
          Selected: {selectedCharacters.length}/6
        </div>
      </div>

      {/* Dynamic Analysis */}
      {dynamicAnalysis && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-semibold mb-6 flex items-center">
            <Zap className="mr-2 text-yellow-500" />
            Group Dynamic Analysis
          </h2>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Left Column */}
            <div className="space-y-4">
              <div className="bg-gray-50 rounded-lg p-4">
                <h3 className="font-semibold text-gray-800 mb-2">Overall Dynamic</h3>
                <p className="text-gray-700">{dynamicAnalysis.overallDynamic}</p>
              </div>

              <div className="bg-green-50 rounded-lg p-4">
                <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                  <CheckCircle className="mr-2 text-green-500 w-4 h-4" />
                  Success Likelihood
                </h3>
                <div className="flex items-center">
                  <div className="w-full bg-gray-200 rounded-full h-3 mr-3">
                    <div 
                      className={`h-3 rounded-full ${
                        dynamicAnalysis.successLikelihood >= 70 ? 'bg-green-500' :
                        dynamicAnalysis.successLikelihood >= 40 ? 'bg-yellow-500' : 'bg-red-500'
                      }`}
                      style={{ width: `${dynamicAnalysis.successLikelihood}%` }}
                    ></div>
                  </div>
                  <span className={`font-bold ${getSuccessColor(dynamicAnalysis.successLikelihood)}`}>
                    {dynamicAnalysis.successLikelihood}%
                  </span>
                </div>
              </div>

              {dynamicAnalysis.leadership.length > 0 && (
                <div className="bg-purple-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-800 mb-2">Natural Leaders</h3>
                  <div className="flex flex-wrap gap-2">
                    {dynamicAnalysis.leadership.map(leader => (
                      <span key={leader} className="bg-purple-200 text-purple-800 px-2 py-1 rounded text-sm">
                        {leader}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {dynamicAnalysis.synergies.length > 0 && (
                <div className="bg-green-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                    <Heart className="mr-2 text-green-500 w-4 h-4" />
                    Strong Bonds
                  </h3>
                  <ul className="text-sm text-gray-700">
                    {dynamicAnalysis.synergies.map((synergy, index) => (
                      <li key={index}>• {synergy}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>

            {/* Right Column */}
            <div className="space-y-4">
              {dynamicAnalysis.conflicts.length > 0 && (
                <div className="bg-red-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                    <Swords className="mr-2 text-red-500 w-4 h-4" />
                    Potential Conflicts
                  </h3>
                  <ul className="text-sm text-gray-700">
                    {dynamicAnalysis.conflicts.map((conflict, index) => (
                      <li key={index}>• {conflict}</li>
                    ))}
                  </ul>
                </div>
              )}

              {dynamicAnalysis.romanticTension.length > 0 && (
                <div className="bg-pink-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                    <Heart className="mr-2 text-pink-500 w-4 h-4" />
                    Romantic Tension
                  </h3>
                  <ul className="text-sm text-gray-700">
                    {dynamicAnalysis.romanticTension.map((tension, index) => (
                      <li key={index}>• {tension}</li>
                    ))}
                  </ul>
                </div>
              )}

              <div className="bg-blue-50 rounded-lg p-4">
                <h3 className="font-semibold text-gray-800 mb-2">Team Strengths</h3>
                <div className="flex flex-wrap gap-2">
                  {dynamicAnalysis.keyStrengths.map(strength => (
                    <span key={strength} className="bg-blue-200 text-blue-800 px-2 py-1 rounded text-sm">
                      {strength}
                    </span>
                  ))}
                </div>
              </div>

              {dynamicAnalysis.potentialIssues.length > 0 && (
                <div className="bg-yellow-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                    <XCircle className="mr-2 text-yellow-500 w-4 h-4" />
                    Watch Out For
                  </h3>
                  <ul className="text-sm text-gray-700">
                    {dynamicAnalysis.potentialIssues.map((issue, index) => (
                      <li key={index}>• {issue}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {selectedCharacters.length < 2 && (
        <div className="bg-white rounded-lg shadow-lg p-6 text-center">
          <p className="text-gray-500">Select at least 2 characters to see their group dynamic analysis!</p>
        </div>
      )}
    </div>
  );
};

export default GroupDynamicSimulator;