import tkinter as tk
import random
from characters import characters
from file_manager import load_discovered, save_discovered, load_history, save_history
from fusion_calculator import get_fusion, fusion_details, show_details, fusion_power, fusions, valid_elements
from relationships import relationships, get_relationship
from battle_engine import simulate_battle, simulate_fusion_battle, calculate_tier_list, get_tier
from group_data import group_dynamics, cross_group_dynamics

discovered = load_discovered()
battle_history = load_history()
current_character = [None]

def clear_display():
    for widget in display.winfo_children():
        widget.destroy()

def show_fusion_panel():
    clear_display()


    #Instructions
    tk.Label(
        display,
        text="Enter two elements to find their fusion",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 10)
    ).pack(pady=(20,10))

    #Valid elements hint
    tk.Label(
        display,
        text="Valid elements: \nThunderstorm, Cyclone, Earthquake, Blaze, Ice, Thorn, Solar",
        bg="#313244",
        fg="#6c7086",
        font=("Courier", 8),
        wraplength=450,
        justify="center"
    ).pack(pady=(0, 10), padx=20)

    #Element 1 input
    tk.Label(
        display,
        text="Element 1:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).pack()

    element1_var = tk.StringVar()
    element1_entry = tk.Entry(
        display,
        textvariable=element1_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=25,
        insertbackground="#cdd6f4"        
    )
    element1_entry.pack(pady=(0,10))

    #Element 2 input
    tk.Label(
        display,
        text="Element 2:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).pack()

    element2_var = tk.StringVar()
    element2_entry = tk.Entry(
        display,
        textvariable=element2_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=25,
        insertbackground="#cdd6f4"        
    )
    element2_entry.pack(pady=(0,15))
    
    #Result display
    result_text = tk.Text(
        display,
        bg="#1e1e2e",
        fg="#cdd6f4",
        font=("Courier", 10),
        width=55,       
        height=15,
        wrap="word",
        state="disabled"
    )
    result_text.pack(pady=10, padx=20)

    #Search button
    def on_search():
        e1 = element1_var.get().strip().lower()
        e2 = element2_var.get().strip().lower()
        result = get_fusion(e1, e2)

        result_text.config(state="normal")
        result_text.delete("1.0", "end")

        if result in fusion_details:
            if result not in discovered:
                result_text.insert("end", f"★ NEW FUSION DISCOVERED: {result} Hayami! ★\n\n")
            discovered.add(result)
            save_discovered(discovered)
            d = fusion_details[result]
            result_text.insert("end", f"{result} Hayami\n")
            result_text.insert("end", "="*40 + "\n")
            result_text.insert("end", f"Components : {d['components']}\n\n")
            result_text.insert("end", f"Personality:\n{d['personality']}\n\n")
            result_text.insert("end", f"Abilities:\n{d['abilities']}\n\n")
            result_text.insert("end", "Signature Moves:\n")
            for move in d["moves"]:
                result_text.insert("end", f"  - {move}\n")
        else:
            result_text.insert("end", result)

        result_text.config(state="disabled")
    
    tk.Button(
        display,
        text="Find Fusion",
        bg="#89b4fa",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=20,
        cursor="hand2",
        command=on_search
    ).pack() 
    
def show_character_panel():
    clear_display()

    tk.Label(
        display,
        text="Character Lookup",
        bg="#313244",
        fg="#a6e3a1",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text="Select a character to view their profile",
        bg="#313244",
        fg="#f1f3fc",
        font=("Courier", 10)
    ).pack(pady=(0, 15))

    # Main layout — list on left, card on right
    main_frame = tk.Frame(display, bg="#313244")
    main_frame.pack(fill="both", expand=True, padx=15, pady=5)

    # ── LEFT: Character list (scrollable) ──
    list_outer = tk.Frame(main_frame, bg="#1e1e2e", width=180)
    list_outer.pack(side="left", fill="y", padx=(0, 10))
    list_outer.pack_propagate(False)

    list_canvas = tk.Canvas(list_outer, bg="#1e1e2e", highlightthickness=0, width=170)
    list_scrollbar = ttk.Scrollbar(list_outer, orient="vertical", command=list_canvas.yview)
    list_canvas.configure(yscrollcommand=list_scrollbar.set)
    list_scrollbar.pack(side="right", fill="y")
    list_canvas.pack(side="left", fill="both", expand=True)

    list_frame = tk.Frame(list_canvas, bg="#1e1e2e")
    list_window = list_canvas.create_window((0, 0), window=list_frame, anchor="nw")

    def on_list_configure(e):
        list_canvas.configure(scrollregion=list_canvas.bbox("all"))
    def on_list_canvas_configure(e):
        list_canvas.itemconfig(list_window, width=e.width)
    def on_list_mousewheel(e):
        list_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    list_frame.bind("<Configure>", on_list_configure)
    list_canvas.bind("<Configure>", on_list_canvas_configure)
    # Only scroll the list when the cursor is actually over it,
    # so it doesn't fight with the card panel's scroll wheel.
    list_canvas.bind("<Enter>", lambda e: list_canvas.bind_all("<MouseWheel>", on_list_mousewheel))
    list_canvas.bind("<Leave>", lambda e: list_canvas.bind_all("<MouseWheel>", on_mousewheel))

    tk.Label(
        list_frame,
        text="CHARACTERS",
        bg="#1e1e2e",
        fg="#f3f5ff",
        font=("Courier", 7, "bold")
    ).pack(pady=(10, 5))

    # Group colors for list
    group_colors = {
        "Analysts":  "#b489fa",
        "Explorers": "#ffd000",
        "Sentinels": "#20cbff",
        "Diplomats": "#12ff1e",
    }

    # Group order
    groups = ["Analysts", "Explorers", "Sentinels", "Diplomats"]
    grouped = {g: [] for g in groups}
    for name, data in characters.items():
        grouped[data["group"]].append((name, data))

    # ── RIGHT: Character card canvas ──
    card_canvas = tk.Canvas(main_frame, bg="#313244", highlightthickness=0)
    card_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=card_canvas.yview)
    card_canvas.configure(yscrollcommand=card_scrollbar.set)
    card_scrollbar.pack(side="right", fill="y")
    card_canvas.pack(side="left", fill="both", expand=True)

    card_frame = tk.Frame(card_canvas, bg="#313244")
    card_window = card_canvas.create_window((0, 0), window=card_frame, anchor="nw")

    def on_card_configure(e):
        card_canvas.configure(scrollregion=card_canvas.bbox("all"))
    def on_card_canvas_configure(e):
        card_canvas.itemconfig(card_window, width=e.width)
    def on_mousewheel(e):
        card_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    card_frame.bind("<Configure>", on_card_configure)
    card_canvas.bind("<Configure>", on_card_canvas_configure)
    card_canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Track selected button
    selected_btn = [None]

    def show_character_card(name):
        current_character[0] = name
        wrap = max(200, display.winfo_width() - 250)
        # Clear previous card
        for widget in card_frame.winfo_children():
            widget.destroy()

        c = characters[name]
        group = c["group"]
        color = group_colors.get(group, "#eef1fb")

        # Header
        header = tk.Frame(card_frame, bg=color, padx=20, pady=15)
        header.pack(fill="x", padx=5, pady=(5, 0))

        tk.Label(
            header,
            text=c["full_name"],
            bg=color,
            fg="#1e1e2e",
            font=("Courier", 16, "bold")
        ).pack(anchor="w")

        tk.Label(
            header,
            text=f"{c['pronouns']}  •  {c['mbti']}  •  {group}  •  {c['height']}",
            bg=color,
            fg="#1e1e2e",
            font=("Courier", 9),
            wraplength=wrap
        ).pack(anchor="w", pady=(3, 0))

        def make_section(title, title_color):
            section = tk.Frame(card_frame, bg="#1e1e2e", padx=15, pady=12)
            section.pack(fill="x", padx=5, pady=2)
            tk.Label(
                section,
                text=title,
                bg="#1e1e2e",
                fg=title_color,
                font=("Courier", 9, "bold")
            ).pack(anchor="w", pady=(0, 6))
            return section

        # Personality
        p_section = make_section("PERSONALITY", color)
        pos_frame = tk.Frame(p_section, bg="#1e1e2e")
        pos_frame.pack(anchor="w", pady=2, fill="x")
        tk.Label(pos_frame, text="(+)", bg="#1e1e2e", fg="#a6e3a1",
                 font=("Courier", 9, "bold")).pack(anchor="w")
        tk.Label(pos_frame, text=f"  {', '.join(c['personality']['positive'])}",
                 bg="#1e1e2e", fg="#eef1fb", font=("Courier", 9), wraplength=wrap).pack(anchor="w")

        neg_frame = tk.Frame(p_section, bg="#1e1e2e")
        neg_frame.pack(anchor="w", pady=2, fill="x")
        tk.Label(neg_frame, text="(-)", bg="#1e1e2e", fg="#f38ba8",
                 font=("Courier", 9, "bold")).pack(anchor="w")
        tk.Label(neg_frame, text=f"  {', '.join(c['personality']['negative'])}",
                 bg="#1e1e2e", fg="#eef1fb", font=("Courier", 9), wraplength=wrap).pack(anchor="w")

        # Power
        pw_section = make_section("POWER", color)
        tk.Label(
            pw_section,
            text=c["power"],
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 11, "bold")
        ).pack(anchor="w")
        tk.Label(
            pw_section,
            text=c["power_description"],
            bg="#1e1e2e",
            fg="#eef1fb",
            font=("Courier", 9),
            wraplength=wrap,
            justify="left"
        ).pack(anchor="w", pady=(4, 0))

        # Stats
        st_section = make_section("STATS", color)
        for stat_key, label in [("academic", "Academic"), ("social", "Social"), ("strategic", "Strategic")]:
            row = tk.Frame(st_section, bg="#1e1e2e")
            row.pack(anchor="w", pady=2, fill="x")
            tk.Label(
                row,
                text=f"{label:<10}",
                bg="#1e1e2e",
                fg=color,
                font=("Courier", 9, "bold")
            ).pack(anchor="w")
            tk.Label(
                row,
                text=c["stats"][stat_key],
                bg="#1e1e2e",
                fg="#eceffc",
                font=("Courier", 9),
                wraplength=wrap,
                justify="left"
            ).pack(anchor="w", padx=(10, 0))

        # Habits
        h_section = make_section("HABITS", color)
        for habit in c["habits"]:
            tk.Label(
                h_section,
                text=f"  - {habit}",
                bg="#1e1e2e",
                fg="#eef1fb",
                font=("Courier", 9),
                wraplength=wrap,
                justify="left"
            ).pack(anchor="w", pady=1)

        card_canvas.yview_moveto(0)

    # Build the character list grouped by faction
    for group in groups:
        color = group_colors[group]

        # Group label
        tk.Label(
            list_frame,
            text=group.upper(),
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 7, "bold")
        ).pack(anchor="w", padx=8, pady=(8, 2))

        for name, data in grouped[group]:
            btn = tk.Button(
                list_frame,
                text=data["full_name"].split()[0],
                bg="#1e1e2e",
                fg="#eff2fb",
                font=("Courier", 9),
                relief="flat",
                cursor="hand2",
                anchor="w",
                padx=12,
                pady=4,
                width=14,
                command=lambda n=name: [
                    show_character_card(n),
                    selected_btn[0] and selected_btn[0].config(bg="#1e1e2e", fg="#eff2fb"),
                    None
                ]
            )
            btn.pack(fill="x", padx=4, pady=1)

            def on_enter(e, b=btn, c=color):
                b.config(bg="#313244", fg=c)
            def on_leave(e, b=btn, char_name=name):
                if selected_btn[0] != b:
                    b.config(bg="#1e1e2e", fg="#f0f3ff")

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            # Update selected on click
            def on_click(e, b=btn, c=color, n=name):
                if selected_btn[0]:
                    selected_btn[0].config(bg="#1e1e2e", fg="#eef1ff")
                selected_btn[0] = b
                b.config(bg="#313244", fg=c)
                show_character_card(n)

            btn.bind("<Button-1>", on_click)
            btn.config(command=lambda: None)

    # Show first character by default
    first_name = list(characters.keys())[0]
    show_character_card(first_name)
    first_btn = list_frame.winfo_children()[3]
    first_btn.config(bg="#313244", fg=group_colors["Analysts"])
    selected_btn[0] = first_btn

def show_fusion_detail_popup(fusion_name):
    from fusion_calculator import fusion_details

    popup = tk.Toplevel(root)
    popup.title(f"{fusion_name} Hayami")
    popup.geometry("600x500")
    popup.configure(bg="#1e1e2e")

    tk.Label(
        popup,
        text=f"{fusion_name} Hayami",
        bg="#1e1e2e",
        fg="#89b4fa",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        popup,
        text=f"Power Rating: {fusion_power.get(fusion_name, '??')}",
        bg="#1e1e2e",
        fg="#a6adc8",
        font=("Courier", 10)
    ).pack(pady=(0, 10))

    frame = tk.Frame(popup, bg="#1e1e2e")
    frame.pack(fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text = tk.Text(
        frame,
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10),
        wrap="word",
        state="normal",
        yscrollcommand=scrollbar.set
    )
    text.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text.yview)

    if fusion_name in fusion_details:
        d = fusion_details[fusion_name]
        text.insert("end", f"Components : {d['components']}\n\n")
        text.insert("end", f"Personality:\n{d['personality']}\n\n")
        text.insert("end", f"Abilities:\n{d['abilities']}\n\n")
        text.insert("end", "Signature Moves:\n")
        for move in d["moves"]:
            text.insert("end", f"  - {move}\n")
    else:
        text.insert("end", "No detailed info available yet.")

    text.config(state="disabled")

    tk.Button(
        popup,
        text="Close",
        bg="#89b4fa",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=12,
        cursor="hand2",
        command=popup.destroy
    ).pack(pady=10)

def show_discovered_panel():
    clear_display()

    tk.Label(
        display,
        text="All Fusions",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    total = len(fusion_power)
    found = len(discovered)

    tk.Label(
        display,
        text=f"Discovered: {found} / {total}",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 10)
    ).pack(pady=(0, 10))

    # Scrollable canvas setup
    canvas = tk.Canvas(display, bg="#313244", highlightthickness=0)
    scrollbar = ttk.Scrollbar(display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Inner frame that holds the cards
    cards_frame = tk.Frame(canvas, bg="#313244")
    canvas_window = canvas.create_window((0, 0), window=cards_frame, anchor="nw")

    # Sort fusions by power rating
    sorted_fusions = sorted(fusion_power.items(), key=lambda x: x[1], reverse=True)

    for fusion_name, power in sorted_fusions:
        if fusion_name in discovered:
            # Discovered card
            card = tk.Frame(
                cards_frame,
                bg="#45475a",
                relief="flat",
                padx=15,
                pady=10
            )
            card.pack(fill="x", padx=15, pady=5)

            # Top row — name and power
            top_row = tk.Frame(card, bg="#45475a")
            top_row.pack(fill="x")

            tk.Label(
                top_row,
                text=f"{fusion_name} Hayami",
                bg="#45475a",
                fg="#89b4fa",
                font=("Courier", 11, "bold")
            ).pack(side="left")

            tk.Label(
                top_row,
                text=f"PWR {power}",
                bg="#45475a",
                fg="#f9e2af",
                font=("Courier", 9, "bold")
            ).pack(side="right")

            # Elements row
            elements = ""
            for (e1, e2), name in fusions.items():
                if name == fusion_name:
                    elements = f"{e1.capitalize()} + {e2.capitalize()}"
                    break

            tk.Label(
                card,
                text=elements,
                bg="#45475a",
                fg="#a6adc8",
                font=("Courier", 9)
            ).pack(anchor="w")

            # Personality preview
            if fusion_name in fusion_details:
                preview = fusion_details[fusion_name]["personality"][:90] + "..."
                tk.Label(
                    card,
                    text=preview,
                    bg="#45475a",
                    fg="#6c7086",
                    font=("Courier", 8),
                    wraplength=500,
                    justify="left"
                ).pack(anchor="w", pady=(4, 0))

            # View details button
            tk.Button(
                card,
                text="View Details",
                bg="#313244",
                fg="#89b4fa",
                font=("Courier", 8, "bold"),
                cursor="hand2",
                relief="flat",
                command=lambda fn=fusion_name: show_fusion_detail_popup(fn)
            ).pack(anchor="e", pady=(5, 0))

        else:
            # Undiscovered card
            card = tk.Frame(
                cards_frame,
                bg="#1e1e2e",
                relief="flat",
                padx=15,
                pady=10
            )
            card.pack(fill="x", padx=15, pady=5)

            top_row = tk.Frame(card, bg="#1e1e2e")
            top_row.pack(fill="x")

            tk.Label(
                top_row,
                text="???????? Hayami",
                bg="#1e1e2e",
                fg="#45475a",
                font=("Courier", 11, "bold")
            ).pack(side="left")

            tk.Label(
                top_row,
                text="PWR ??",
                bg="#1e1e2e",
                fg="#45475a",
                font=("Courier", 9, "bold")
            ).pack(side="right")

            tk.Label(
                card,
                text="? + ?",
                bg="#1e1e2e",
                fg="#313244",
                font=("Courier", 9)
            ).pack(anchor="w")

            tk.Label(
                card,
                text="Discover this fusion to unlock its details.",
                bg="#1e1e2e",
                fg="#45475a",
                font=("Courier", 8),
                justify="left"
            ).pack(anchor="w", pady=(4, 0))

    # Make canvas scrollable
    def on_frame_configure(e):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(e):
        canvas.itemconfig(canvas_window, width=e.width)

    cards_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    # Mouse wheel scrolling
    def on_mousewheel(e):
        canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

def random_fusion():
    all_combos = list(fusions.items())
    (e1,e2), name = random.choice(all_combos)

    clear_display()

    tk.Label(
        display,
        text="Random Fusion Result!",
        bg="#313244",
        fg="#fab387",
        font=("Courier", 12, "bold")
    ).pack(pady=(20, 10))

    result_text = tk.Text(
        display,
        bg="#1e1e2e",
        fg="#cdd6f4",
        font=("Courier", 10),
        width=55,
        height=18,
        wrap="word",
        state="normal"
    )
    result_text.pack(pady=10, padx=20)

    if name in fusion_details:
        if name not in discovered:
            result_text.insert("end", f"NEW FUSION DISCOVERED: {name} Hayami!\n\n")
        discovered.add(name)
        save_discovered(discovered)
        d = fusion_details[name]
        result_text.insert("end", f"{name} Hayami\n")
        result_text.insert("end", "=" * 40 + "\n")
        result_text.insert("end", f"Components : {d['components']}\n\n")
        result_text.insert("end", f"Personality:\n{d['personality']}\n\n")
        result_text.insert("end", f"Abilities:\n{d['abilities']}\n\n")
        result_text.insert("end", "Signature Moves:\n")
        for move in d["moves"]:
            result_text.insert("end", f"  - {move}\n")
    else:
        result_text.insert("end", f"{name} Hayami\n")
        result_text.insert("end", "=" * 40 + "\n")
        result_text.insert("end", f"Elements: {e1.capitalize()} + {e2.capitalize()}\n")
        result_text.insert("end", f"Power Rating: {fusion_power.get(name, 'Unknown')}\n\n")
        result_text.insert("end", "Detailed info not yet added for this fusion.")

    result_text.config(state="disabled")

    tk.Button(
        display,
        text="Roll Again!",
        bg="#fab387",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=20,
        cursor="hand2",
        command=random_fusion
    ).pack(pady=10)

def show_relationship_panel():
    clear_display()

    tk.Label(
        display,
        text="Enter two character names to see their dynamic",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 10)        
    ).pack(pady=(20,10))

    #Character 1 input
    tk.Label(
        display,
        text="Character 1:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).pack()        
    
    char1_var = tk.StringVar()
    tk.Entry(
        display,
        textvariable=char1_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=25,
        insertbackground="#cdd6f4"
    ).pack(pady=(0,10))

    #Character 2 input
    tk.Label(
        display,
        text="Character 2:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).pack() 

    char2_var = tk.StringVar()
    tk.Entry(
        display,
        textvariable=char2_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=25,
        insertbackground="#cdd6f4"
    ).pack(pady=(0,15))

    result_text = tk.Text(
        display,
        bg="#1e1e2e",
        fg="#cdd6f4",
        font=("Courier", 10),
        width=55,       
        height=15,
        wrap="word",
        state="disabled"
    )
    result_text.pack(pady=10, padx=20)

    def on_search():
        c1 = char1_var.get().strip().lower()
        c2 = char2_var.get().strip().lower()

        result_text.config(state="normal")
        result_text.delete("1.0", "end")

        if c1 not in characters:
            result_text.insert("end", f"'{c1}' is not a valid character name.")
        elif c2 not in characters:
            result_text.insert("end", f"'{c2}' is not a valid character name.")
        elif c1 == c2:
            result_text.insert("end", "Enter two different characters!")
        else:
            #Sort alphabetically
            result = get_relationship(c1,c2)

            if result:
                c1_full = characters[c1]["full_name"]
                c2_full = characters[c2]["full_name"]
                c1_mbti = characters[c1]["mbti"]
                c2_mbti = characters[c2]["mbti"]

                result_text.insert("end", f"{c1_full} x {c2_full}\n")
                result_text.insert("end", "="*40 + "\n")
                result_text.insert("end", f"{c1_mbti}\n")
                result_text.insert("end", f"{c2_mbti}\n\n")
                result_text.insert("end", f"Dynamic:\n{result}\n")
            else:
                result_text.insert("end", "No relationship data found for this pair.")
        
        result_text.config(state="disabled")

    tk.Button(
        display,
        text="Lookup dynamic",
        bg="#cba6f7",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=20,
        cursor="hand2",
        command=on_search 
    ).pack()

def show_battle_panel():
    clear_display()

    tk.Label(
        display,
        text="Character Battle Simulator",
        bg="#313244",
        fg="#f38ba8",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text="Enter two character names to simulate a battle",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 10)
    ).pack(pady=(0, 15))

    #Input row
    input_frame = tk.Frame(display, bg="#313244")
    input_frame.pack()

    tk.Label(
        input_frame,
        text="Fighter 1:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).grid(row=0, column=0, padx=10)

    tk.Label(
        input_frame,
        text="Fighter 2:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).grid(row=0, column=1, padx=10)

    fighter1_var = tk.StringVar()    
    fighter2_var = tk.StringVar()    

    tk.Entry(
        input_frame,
        textvariable=fighter1_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=18,
        insertbackground="#cdd6f4"
    ).grid(row=1, column=0, padx=10, pady=5)

    tk.Entry(
        input_frame,
        textvariable=fighter2_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=18,
        insertbackground="#cdd6f4"
    ).grid(row=1, column=1, padx=10, pady=5)

    #Scrollable battle log
    frame = tk.Frame(display, bg="#313244")
    frame.pack(fill="both", padx=20, pady=10)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    battle_log = tk.Text(
        frame,
        bg="#1e1e2e",
        fg="#cdd6f4",
        font=("Courier", 10),
        wrap="word",
        state="disabled",
        yscrollcommand=scrollbar.set,
        height=18
    )
    battle_log.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=battle_log.yview)

    def on_battle():
        f1 = fighter1_var.get().strip().lower()
        f2 = fighter2_var.get().strip().lower()

        battle_log.config(state="normal")
        battle_log.delete("1.0", "end")

        if f1 not in characters:
            battle_log.insert("end", f"'{f1}' is not a valid character name.")
        elif f2 not in characters:
            battle_log.insert("end", f"'{f2}' is not a valid character name.")
        elif f1 == f2:
            battle_log.insert("end", "Enter two different characters!")
        else:
            result = simulate_battle(f1,f2)
            battle_log.insert("end", result)

            # Save to history
            lines = result.split("\n")
            winner = "Draw"
            for line in lines:
                if "WINNER:" in line:
                    winner = line.replace("WINNER:", "").replace("!", "").strip()
                    break

            import datetime
            entry = {
                "type": "character",
                "fighter1": characters[f1]["full_name"],
                "fighter2": characters[f2]["full_name"],
                "winner": winner,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "log": result
            }
            battle_history.append(entry)
            save_history(battle_history)

        battle_log.config(state="disabled")
        battle_log.see("1.0")

    #Buttom row
    btn_frame = tk.Frame(display, bg="#313244")
    btn_frame.pack(pady=5)

    tk.Button(
        btn_frame,
        text="Start Battle!",
        bg="#f38ba8",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=16,
        cursor="hand2",
        command=on_battle
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="Rematch!",
        bg="#fab387",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=16,
        cursor="hand2",
        command=on_battle
    ).grid(row=0, column=1, padx=10)

def show_fusion_battle_panel():
    clear_display()

    tk.Label(
        display,
        text="Hayami Fusion Battle!",
        bg="#313244",
        fg="#89dceb",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text="Enter two fusion names to simulate a battle",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 10)
    ).pack(pady=(0, 5))

    tk.Label(
        display,
        text="e.g. Supra, Glacier, FrostFire, Rumble...",
        bg="#313244",
        fg="#6c7086",
        font=("Courier", 9)
    ).pack(pady=(0, 15))

    #Input row
    input_frame = tk.Frame(display, bg= "#313244")
    input_frame.pack()

    tk.Label(
        input_frame,
        text="Fusion 1:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).grid(row=0, column=0, padx=10)

    tk.Label(
        input_frame,
        text="Fusion 2:",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).grid(row=0, column=1, padx=10)

    fusion1_var = tk.StringVar()    
    fusion2_var = tk.StringVar()    

    tk.Entry(
        input_frame,
        textvariable=fusion1_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=18,
        insertbackground="#cdd6f4"
    ).grid(row=1, column=0, padx=10, pady=5)

    tk.Entry(
        input_frame,
        textvariable=fusion2_var,
        bg="#45475a",
        fg="#cdd6f4",
        font=("Courier", 11),
        width=18,
        insertbackground="#cdd6f4"
    ).grid(row=1, column=1, padx=10, pady=5)

    #Scrollable battle log
    frame = tk.Frame(display, bg="#313244")
    frame.pack(fill="both", padx=20, pady=10)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    battle_log = tk.Text(
        frame,
        bg="#1e1e2e",
        fg="#cdd6f4",
        font=("Courier", 10),
        wrap="word",
        state="disabled",
        yscrollcommand=scrollbar.set,
        height=18
    )
    battle_log.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=battle_log.yview)

    def on_battle():
        f1 = fusion1_var.get().strip().title()
        f2 = fusion2_var.get().strip().title()

        battle_log.config(state="normal")
        battle_log.delete("1.0", "end")

        from battle_engine import fusion_battle_stats
        if f1 not in fusion_battle_stats:
            battle_log.insert("end", f"'{f1}' is not a valid fusion name.\nTry: Supra, Glacier, FrostFire, Rumble, Cyclar...")
        elif f2 not in fusion_battle_stats:
            battle_log.insert("end", f"'{f2}' is not a valid fusion name.\nTry: Supra, Glacier, FrostFire, Rumble, Cyclar...")
        elif f1 not in discovered:
            battle_log.insert("end", f"{f1} Hayami has not been discovered yet!\nFind this fusion in the Fusion Calculator first.")
        elif f2 not in discovered:
            battle_log.insert("end", f"{f2} Hayami has not been discovered yet!\nFind this fusion in the Fusion Calculator first.")
        elif f1 == f2:
            battle_log.insert("end", "Enter two different fusions!")
        else:
            result = simulate_fusion_battle(f1, f2)
            battle_log.insert("end", result)

            # Save to history
            lines = result.split("\n")
            winner = "Draw"
            for line in lines:
                if "WINNER:" in line:
                    winner = line.replace("WINNER:", "").replace("!", "").strip()
                    break

            import datetime
            entry = {
                "type": "fusion",
                "fighter1": f"{f1} Hayami",
                "fighter2": f"{f2} Hayami",
                "winner": winner,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "log": result
            }
            battle_history.append(entry)
            save_history(battle_history)

        battle_log.config(state="disabled")
        battle_log.see("1.0")
    
    #Button row
    btn_frame = tk.Frame(display, bg="#313244")
    btn_frame.pack(pady=5)

    tk.Button(
        btn_frame,
        text="Start Battle!",
        bg="#89dceb",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=16,
        cursor="hand2",
        command=on_battle
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="Rematch!",
        bg="#74c7ec",
        fg="#1e1e2e",
        font=("Courier", 10, "bold"),
        width=16,
        cursor="hand2",
        command=on_battle
    ).grid(row=0, column=1, padx=10)    

def show_tierlist_panel():
    clear_display()

    tk.Label(
        display,
        text="Character Tier List",
        bg="#313244",
        fg="#f9e2af",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text="Ranked by overall combat power (avg of all stats)",
        bg="#313244",
        fg="#a6adc8",
        font=("Courier", 9)
    ).pack(pady=(0, 10))

    ranked = calculate_tier_list()

    # Scrollable canvas
    canvas = tk.Canvas(display, bg="#313244", highlightthickness=0)
    scrollbar = ttk.Scrollbar(display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    content_frame = tk.Frame(canvas, bg="#313244")
    canvas_window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Tier colors
    tier_colors = {
        "S": "#f38ba8",
        "A": "#fab387",
        "B": "#f9e2af",
        "C": "#a6adc8",
    }

    tier_labels = {
        "S": "S  — Elite",
        "A": "A  — Strong",
        "B": "B  — Solid",
        "C": "C  — Developing",
    }

    # Group by tier
    tiers = {"S": [], "A": [], "B": [], "C": []}
    for name, score, stats in ranked:
        tier = get_tier(score)
        tiers[tier].append((name, score, stats))

    # ── TIER GROUPINGS ──
    tk.Label(
        content_frame,
        text="TIER GROUPINGS",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 11, "bold")
    ).pack(anchor="w", padx=15, pady=(10, 5))

    for tier in ["S", "A", "B", "C"]:
        if not tiers[tier]:
            continue

        tier_frame = tk.Frame(content_frame, bg="#1e1e2e", padx=10, pady=8)
        tier_frame.pack(fill="x", padx=15, pady=3)

        # Tier label
        tk.Label(
            tier_frame,
            text=tier_labels[tier],
            bg="#1e1e2e",
            fg=tier_colors[tier],
            font=("Courier", 11, "bold"),
            width=16,
            anchor="w"
        ).pack(side="left")

        # Character names in this tier
        names_frame = tk.Frame(tier_frame, bg="#1e1e2e")
        names_frame.pack(side="left", fill="x", expand=True)

        for name, score, stats in tiers[tier]:
            c = characters[name]
            chip = tk.Frame(names_frame, bg="#313244", padx=8, pady=3)
            chip.pack(side="left", padx=4)

            tk.Label(
                chip,
                text=f"{c['full_name'].split()[0]}",
                bg="#313244",
                fg=tier_colors[tier],
                font=("Courier", 9, "bold")
            ).pack()

            tk.Label(
                chip,
                text=f"{score}",
                bg="#313244",
                fg="#a6adc8",
                font=("Courier", 8)
            ).pack()

    # Divider
    tk.Frame(content_frame, bg="#45475a", height=2).pack(fill="x", padx=15, pady=15)

    # ── RANKED LIST ──
    tk.Label(
        content_frame,
        text="FULL RANKING",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 11, "bold")
    ).pack(anchor="w", padx=15, pady=(0, 5))

    for i, (name, score, stats) in enumerate(ranked):
        c = characters[name]
        tier = get_tier(score)
        color = tier_colors[tier]

        row = tk.Frame(content_frame, bg="#1e1e2e", padx=12, pady=8)
        row.pack(fill="x", padx=15, pady=2)

        # Rank number
        tk.Label(
            row,
            text=f"#{i+1}",
            bg="#1e1e2e",
            fg="#6c7086",
            font=("Courier", 10, "bold"),
            width=3,
            anchor="w"
        ).pack(side="left")

        # Tier badge
        tk.Label(
            row,
            text=f"[{tier}]",
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 10, "bold"),
            width=4
        ).pack(side="left")

        # Name and MBTI
        tk.Label(
            row,
            text=f"{c['full_name']:<20} {c['mbti'].split()[0]}",
            bg="#1e1e2e",
            fg="#cdd6f4",
            font=("Courier", 10),
            anchor="w"
        ).pack(side="left", expand=True, fill="x")

        # Score
        tk.Label(
            row,
            text=f"{score}",
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 10, "bold"),
            width=6,
            anchor="e"
        ).pack(side="right")

        # Stat breakdown on hover — show as small label
        stat_text = f"HP:{stats['hp']} ATK:{stats['attack']} DEF:{stats['defense']} SPD:{stats['speed']} SPC:{stats['special']}"
        tk.Label(
            row,
            text=stat_text,
            bg="#1e1e2e",
            fg="#d5d5d5",
            font=("Courier", 8),
            anchor="w"
        ).pack(side="bottom", anchor="w")

    # Scrolling setup
    def on_frame_configure(e):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(e):
        canvas.itemconfig(canvas_window, width=e.width)

    content_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    def on_mousewheel(e):
        canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mousewheel)

def show_group_panel():
    clear_display()

    tk.Label(
        display,
        text="Group Dynamics",
        bg="#313244",
        fg="#89dceb",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text="The four groups and how they interact",
        bg="#313244",
        fg="#e4e4e4",
        font=("Courier", 10)
    ).pack(pady=(0, 10))

    # Scrollable canvas
    canvas = tk.Canvas(display, bg="#313244", highlightthickness=0)
    scrollbar = ttk.Scrollbar(display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    content = tk.Frame(canvas, bg="#313244")
    canvas_window = canvas.create_window((0, 0), window=content, anchor="nw")

    def on_frame_configure(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
    def on_canvas_configure(e):
        canvas.itemconfig(canvas_window, width=e.width)
    def on_mousewheel(e):
        canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    content.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Group cards
    for group_name, data in group_dynamics.items():
        color = data["color"]

        # Header
        header = tk.Frame(content, bg=color, padx=15, pady=12)
        header.pack(fill="x", padx=15, pady=(10, 0))

        header_left = tk.Frame(header, bg=color)
        header_left.pack(side="left")

        tk.Label(
            header_left,
            text=f"{data['icon']} {group_name}",
            bg=color,
            fg="#1e1e2e",
            font=("Courier", 13, "bold")
        ).pack(anchor="w")

        tk.Label(
            header_left,
            text=f"  {' • '.join(data['mbti_types'])}",
            bg=color,
            fg="#1e1e2e",
            font=("Courier", 8)
        ).pack(anchor="w")

        tk.Label(
            header,
            text=data["chaos_rating"],
            bg=color,
            fg="#1e1e2e",
            font=("Courier", 8, "bold")
        ).pack(side="right", anchor="n")

        # Body
        body = tk.Frame(content, bg="#1e1e2e", padx=15, pady=12)
        body.pack(fill="x", padx=15, pady=(0, 2))

        # Tagline
        tk.Label(
            body,
            text=f'"{data["tagline"]}"',
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 9, "italic"),
            wraplength=550,
            justify="left"
        ).pack(anchor="w", pady=(0, 8))

        # Members
        members_frame = tk.Frame(body, bg="#1e1e2e")
        members_frame.pack(anchor="w", pady=(0, 8))

        tk.Label(
            members_frame,
            text="Members: ",
            bg="#1e1e2e",
            fg="#dbdbdc",
            font=("Courier", 8, "bold")
        ).pack(side="left")

        for member in data["members"]:
            chip = tk.Frame(members_frame, bg="#313244", padx=6, pady=2)
            chip.pack(side="left", padx=3)
            tk.Label(
                chip,
                text=member.split()[0],
                bg="#313244",
                fg=color,
                font=("Courier", 8)
            ).pack()

        # Facts
        tk.Label(
            body,
            text="GROUP FACTS",
            bg="#1e1e2e",
            fg="#d9d9d9",
            font=("Courier", 7, "bold")
        ).pack(anchor="w", pady=(0, 4))

        for fact in data["facts"]:
            tk.Label(
                body,
                text=f"  - {fact}",
                bg="#1e1e2e",
                fg="#dbdbdb",
                font=("Courier", 8),
                wraplength=550,
                justify="left"
            ).pack(anchor="w", pady=1)

        # Strengths and weaknesses
        sw_frame = tk.Frame(body, bg="#1e1e2e")
        sw_frame.pack(anchor="w", pady=(8, 0), fill="x")

        left = tk.Frame(sw_frame, bg="#1e1e2e")
        left.pack(side="left", fill="x", expand=True)

        tk.Label(left, text="STRENGTH", bg="#1e1e2e", fg="#dddddd",
                 font=("Courier", 7, "bold")).pack(anchor="w")
        tk.Label(left, text=data["strengths"], bg="#1e1e2e", fg="#a6e3a1",
                 font=("Courier", 8), wraplength=260, justify="left").pack(anchor="w")

        right = tk.Frame(sw_frame, bg="#1e1e2e")
        right.pack(side="left", fill="x", expand=True)

        tk.Label(right, text="WEAKNESS", bg="#1e1e2e", fg="#dddddd",
                 font=("Courier", 7, "bold")).pack(anchor="w")
        tk.Label(right, text=data["weakness"], bg="#1e1e2e", fg="#f38ba8",
                 font=("Courier", 8), wraplength=260, justify="left").pack(anchor="w")

    # Cross group dynamics
    tk.Frame(content, bg="#45475a", height=1).pack(fill="x", padx=15, pady=15)

    tk.Label(
        content,
        text="CROSS-GROUP DYNAMICS",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 10, "bold")
    ).pack(anchor="w", padx=15, pady=(0, 8))

    for label, color, desc in cross_group_dynamics:
        row = tk.Frame(content, bg="#1e1e2e", padx=15, pady=10)
        row.pack(fill="x", padx=15, pady=3)

        tk.Label(
            row,
            text=label,
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 9, "bold")
        ).pack(anchor="w")

        tk.Label(
            row,
            text=desc,
            bg="#1e1e2e",
            fg="#d6d9e5",
            font=("Courier", 8),
            wraplength=580,
            justify="left"
        ).pack(anchor="w", pady=(3, 0))

def show_history_panel():
    clear_display()

    tk.Label(
        display,
        text="Battle History",
        bg="#313244",
        fg="#f9e2af",
        font=("Courier", 14, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        display,
        text=f"{len(battle_history)} battles recorded",
        bg="#313244",
        fg="#e8ebf9",
        font=("Courier", 10)
    ).pack(pady=(0, 10))

    if not battle_history:
        tk.Label(
            display,
            text="No battles recorded yet!\nGo fight someone.",
            bg="#313244",
            fg="#f1f3fe",
            font=("Courier", 11),
            justify="center"
        ).pack(expand=True)
        return

    # Scrollable canvas
    canvas = tk.Canvas(display, bg="#313244", highlightthickness=0)
    scrollbar = ttk.Scrollbar(display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    content = tk.Frame(canvas, bg="#313244")
    canvas_window = canvas.create_window((0, 0), window=content, anchor="nw")

    def on_frame_configure(e):
        canvas.configure(scrollregion=canvas.bbox("all"))
    def on_canvas_configure(e):
        canvas.itemconfig(canvas_window, width=e.width)
    def on_mousewheel(e):
        canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

    content.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Show most recent first
    for i, entry in enumerate(reversed(battle_history)):
        is_fusion = entry["type"] == "fusion"
        color = "#89dceb" if is_fusion else "#f38ba8"
        label = "FUSION" if is_fusion else "CHARACTER"

        card = tk.Frame(content, bg="#1e1e2e", padx=15, pady=10)
        card.pack(fill="x", padx=15, pady=4)

        # Top row
        top = tk.Frame(card, bg="#1e1e2e")
        top.pack(fill="x")

        tk.Label(
            top,
            text=f"[{label}]",
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 8, "bold")
        ).pack(side="left")

        tk.Label(
            top,
            text=entry["date"],
            bg="#1e1e2e",
            fg="#ebeefe",
            font=("Courier", 8)
        ).pack(side="right")

        # Matchup
        tk.Label(
            card,
            text=f"{entry['fighter1']}  vs  {entry['fighter2']}",
            bg="#1e1e2e",
            fg="#edf0fa",
            font=("Courier", 10, "bold")
        ).pack(anchor="w", pady=(4, 2))

        # Winner
        tk.Label(
            card,
            text=f"Winner: {entry['winner']}",
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 9)
        ).pack(anchor="w")

        # View log button
        def view_log(log=entry["log"], f1=entry["fighter1"], f2=entry["fighter2"]):
            popup = tk.Toplevel(root)
            popup.title(f"{f1} vs {f2}")
            popup.geometry("650x500")
            popup.configure(bg="#1e1e2e")

            frame = tk.Frame(popup, bg="#1e1e2e")
            frame.pack(fill="both", expand=True, padx=15, pady=15)

            sb = ttk.Scrollbar(frame)
            sb.pack(side="right", fill="y")

            text = tk.Text(
                frame,
                bg="#313244",
                fg="#e8ecfa",
                font=("Courier", 10),
                wrap="word",
                state="normal",
                yscrollcommand=sb.set
            )
            text.pack(side="left", fill="both", expand=True)
            sb.config(command=text.yview)
            text.insert("end", log)
            text.config(state="disabled")

            tk.Button(
                popup,
                text="Close",
                bg="#f9e2af",
                fg="#1e1e2e",
                font=("Courier", 9, "bold"),
                relief="flat",
                cursor="hand2",
                command=popup.destroy
            ).pack(pady=10)

        tk.Button(
            card,
            text="View Full Log",
            bg="#313244",
            fg=color,
            font=("Courier", 8),
            relief="flat",
            cursor="hand2",
            command=view_log
        ).pack(anchor="e", pady=(5, 0))

    # Clear history button
    def clear_history():
        battle_history.clear()
        save_history(battle_history)
        show_history_panel()

    tk.Button(
        content,
        text="Clear All History",
        bg="#1e1e2e",
        fg="#f38ba8",
        font=("Courier", 9),
        relief="flat",
        cursor="hand2",
        command=clear_history
    ).pack(pady=15)

#Main window setup
root = tk.Tk()
root.title("Character Compendium")
root.geometry("900x600")
root.configure(bg="#1e1e2e")

# Slim scrollbar style
import tkinter.ttk as ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("Vertical.TScrollbar", 
    gripcount=0, background="#45475a", 
    darkcolor="#1e1e2e", lightcolor="#1e1e2e",
    troughcolor="#1e1e2e", bordercolor="#1e1e2e",
    arrowcolor="#6c7086", width=8)
style.configure("Horizontal.TScrollbar",
    gripcount=0, background="#45475a",
    darkcolor="#1e1e2e", lightcolor="#1e1e2e", 
    troughcolor="#1e1e2e", bordercolor="#1e1e2e",
    arrowcolor="#6c7086", width=8)

# Title bar frame
title_frame = tk.Frame(root, bg="#1e1e2e")
title_frame.pack(fill="x", pady=(15, 5))

tk.Label(
    title_frame,
    text="✦",
    bg="#1e1e2e",
    fg="#89b4fa",
    font=("Courier", 12)
).pack(side="left", padx=(20, 5))

tk.Label(
    title_frame,
    text="Character Compendium",
    bg="#1e1e2e",
    fg="#cdd6f4",
    font=("Courier", 18, "bold")
).pack(side="left")

tk.Label(
    title_frame,
    text="✦",
    bg="#1e1e2e",
    fg="#89b4fa",
    font=("Courier", 12)
).pack(side="left", padx=(5, 0))

# Home button on the right
tk.Button(
    title_frame,
    text="⌂  Home",
    bg="#1e1e2e",
    fg="#e7e7e9",
    font=("Courier", 9),
    relief="flat",
    cursor="hand2",
    command=lambda: show_home_screen()
).pack(side="right", padx=20)

# Thin accent line under title
tk.Frame(root, bg="#45475a", height=1).pack(fill="x")

#Main container
container = tk.Frame(root, bg="#1e1e2e")
container.pack(fill="both", expand=True, padx=20, pady=20)

#Sidebar
sidebar_outer = tk.Frame(container, bg="#313244", width=255)
sidebar_outer.pack(side="left", fill="y", padx=(0, 20))
sidebar_outer.pack_propagate(False)

sidebar_canvas = tk.Canvas(sidebar_outer, bg="#313244", highlightthickness=0, width=210)
sidebar_scroll = ttk.Scrollbar(sidebar_outer, orient="vertical", command=sidebar_canvas.yview)
sidebar_canvas.configure(yscrollcommand=sidebar_scroll.set)

sidebar_scroll.pack(side="right", fill="y")
sidebar_canvas.pack(side="left", fill="both", expand=True)

sidebar = tk.Frame(sidebar_canvas, bg="#313244")
sidebar_canvas.create_window((0, 0), window=sidebar, anchor="nw")

def on_sidebar_configure(e):
    sidebar_canvas.configure(scrollregion=sidebar_canvas.bbox("all"))

sidebar.bind("<Configure>", on_sidebar_configure)

def sidebar_mousewheel(e):
    sidebar_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

sidebar_canvas.bind("<MouseWheel>", sidebar_mousewheel)
sidebar.bind("<MouseWheel>", sidebar_mousewheel)

# Sidebar inner padding
sidebar_inner = tk.Frame(sidebar, bg="#313244")
sidebar_inner.pack(fill="both", expand=True, padx=8, pady=10)

# App logo/title in sidebar
tk.Label(
    sidebar_inner,
    text="✦ MENU ✦",
    bg="#313244",
    fg="#cdd6f4",
    font=("Courier", 11, "bold")
).pack(pady=(10, 15))

# Helper to create section dividers
def section_label(text):
    tk.Label(
        sidebar_inner,
        text=text,
        bg="#313244",
        fg="#e8e8e8",
        font=("Courier", 7, "bold")
    ).pack(anchor="w", padx=5, pady=(10, 2))
    tk.Frame(
        sidebar_inner,
        bg="#45475a",
        height=1
    ).pack(fill="x", padx=5, pady=(0, 5))

# Helper to create styled buttons with hover effects
def make_button(text, color, command):
    btn = tk.Button(
        sidebar_inner,
        text=text,
        bg="#1e1e2e",
        fg=color,
        font=("Courier", 9, "bold"),
        width=30,
        cursor="hand2",
        relief="flat",
        pady=6,
        command=command
    )
    btn.pack(pady=2)

    def on_enter(e):
        btn.config(bg=color, fg="#1e1e2e")

    def on_leave(e):
        btn.config(bg="#1e1e2e", fg=color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# ── CHARACTER SECTION ──
section_label("CHARACTER")
make_button("👤  Character Lookup", "#a6e3a1", show_character_panel)
make_button("📊  Tier List", "#f9e2af", show_tierlist_panel)
make_button("💞  Relationship", "#cba6f7", show_relationship_panel)
make_button("👥  Group Dynamics", "#89dceb", show_group_panel)

# ── FUSION SECTION ──
section_label("FUSIONS")
make_button("⚗️   Fusion Calculator", "#89b4fa", show_fusion_panel)
make_button("✨  Discovered", "#f38ba8", show_discovered_panel)
make_button("🎲  Random Fusion", "#fab387", random_fusion)

# ── BATTLE SECTION ──
section_label("BATTLE")
make_button("⚔️   Character Battle", "#f38ba8", show_battle_panel)
make_button("💥  Fusion Battle", "#89dceb", show_fusion_battle_panel)
make_button("📜  Battle History", "#f9e2af", show_history_panel)

#Display panel
display = tk.Frame(container, bg="#313244")
display.pack(side="left", fill="both", expand=True)

def show_home_screen():
    clear_display()

    # Scrollable canvas for home
    canvas = tk.Canvas(display, bg="#313244", highlightthickness=0)
    h_scroll = ttk.Scrollbar(display, orient="horizontal", command=canvas.xview)
    v_scroll = ttk.Scrollbar(display, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

    h_scroll.pack(side="bottom", fill="x")
    v_scroll.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    welcome_frame = tk.Frame(canvas, bg="#313244")
    canvas_window = canvas.create_window((0, 0), window=welcome_frame, anchor="nw")

    def on_frame_configure(e):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(e):
        canvas.itemconfig(canvas_window, width=max(e.width, 800))

    welcome_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    def on_mousewheel(e):
        canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    tk.Label(
        welcome_frame,
        text="✦",
        bg="#313244",
        fg="#89b4fa",
        font=("Courier", 32)
    ).pack(pady=(40, 5))

    tk.Label(
        welcome_frame,
        text="Character Compendium",
        bg="#313244",
        fg="#cdd6f4",
        font=("Courier", 20, "bold")
    ).pack()

    tk.Label(
        welcome_frame,
        text="A complete reference for Hayami's world",
        bg="#313244",
        fg="#6c7086",
        font=("Courier", 10)
    ).pack(pady=(5, 30))

    # Stats row
    stats_frame = tk.Frame(welcome_frame, bg="#313244")
    stats_frame.pack(pady=10)

    stats = [
        ("16", "Characters"),
        ("21", "Fusions"),
        ("120", "Relationships"),
        (f"{len(discovered)}", "Discovered"),
    ]

    for value, label in stats:
        stat_box = tk.Frame(stats_frame, bg="#1e1e2e", padx=20, pady=15)
        stat_box.pack(side="left", padx=10)

        tk.Label(
            stat_box,
            text=value,
            bg="#1e1e2e",
            fg="#89b4fa",
            font=("Courier", 20, "bold")
        ).pack()

        tk.Label(
            stat_box,
            text=label,
            bg="#1e1e2e",
            fg="#6c7086",
            font=("Courier", 9)
        ).pack()

    # Divider
    tk.Frame(welcome_frame, bg="#45475a", height=1).pack(fill="x", padx=40, pady=30)

    # Quick start buttons
    tk.Label(
        welcome_frame,
        text="QUICK START",
        bg="#313244",
        fg="#6c7086",
        font=("Courier", 8, "bold")
    ).pack(pady=(0, 10))

    quick_frame = tk.Frame(welcome_frame, bg="#313244")
    quick_frame.pack()

    quick_buttons = [
        ("⚗️  Fusion Calculator", "#89b4fa", show_fusion_panel),
        ("👤  Character Lookup", "#a6e3a1", show_character_panel),
        ("⚔️  Battle!", "#f38ba8", show_battle_panel),
        ("✨  Discovered", "#fab387", show_discovered_panel),
    ]

    for text, color, cmd in quick_buttons:
        btn = tk.Button(
            quick_frame,
            text=text,
            bg="#1e1e2e",
            fg=color,
            font=("Courier", 9, "bold"),
            width=24,
            cursor="hand2",
            relief="flat",
            pady=8,
            command=cmd
        )
        btn.pack(side="left", padx=8)

        def on_enter(e, b=btn, c=color):
            b.config(bg=color, fg="#1e1e2e")
        def on_leave(e, b=btn, c=color):
            b.config(bg="#1e1e2e", fg=c)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Recent discovery
    if discovered:
        tk.Frame(welcome_frame, bg="#45475a", height=1).pack(fill="x", padx=40, pady=30)

        tk.Label(
            welcome_frame,
            text="LATEST DISCOVERY",
            bg="#313244",
            fg="#6c7086",
            font=("Courier", 8, "bold")
        ).pack(pady=(0, 8))

        last = list(discovered)[-1]
        tk.Label(
            welcome_frame,
            text=f"✦ {last} Hayami",
            bg="#313244",
            fg="#f9e2af",
            font=("Courier", 12, "bold")
        ).pack()

        if last in fusion_details:
            preview = fusion_details[last]["personality"][:100] + "..."
            tk.Label(
                welcome_frame,
                text=preview,
                bg="#313244",
                fg="#6c7086",
                font=("Courier", 9),
                wraplength=500,
                justify="center"
            ).pack(pady=(5, 0))
            
    # Bottom padding
    tk.Frame(welcome_frame, bg="#313244", height=40).pack()

show_home_screen()

current_character = [None]

def on_window_resize(e):
    if e.widget == root:
        if current_character[0]:
            try:
                show_character_card(current_character[0])
            except:
                pass

root.bind("<Configure>", on_window_resize)

root.mainloop()