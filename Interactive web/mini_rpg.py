import random
import tkinter as tk
from tkinter import messagebox

player = {
    "nama": "",
    "level": 1,
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "weapon_level": 1,
    "exp": 0,
    "exp_next_level": 50,
    "gold": 30,
    "inventory": ["Health Potion", "Health Potion"]
}

daftar_musuh = [
    # Normal
    {"nama": "Goblin", "hp": 60, "max_hp": 60, "attack": 12, "exp_reward": 30, "gold_reward": 20},
    {"nama": "Mimic", "hp": 50, "max_hp": 50, "attack": 10, "exp_reward": 25, "gold_reward": 50},
    {"nama": "Orc Fighter", "hp": 90, "max_hp": 90, "attack": 16, "exp_reward": 45, "gold_reward": 35},
    
    # Advaced
    {"nama": "Shadow Wolf", "hp": 110, "max_hp": 110, "attack": 22, "exp_reward": 60, "gold_reward": 45},
    {"nama": "Gargoyle Stone", "hp": 150, "max_hp": 150, "attack": 18, "exp_reward": 80, "gold_reward": 60},
    {"nama": "Dark Mage", "hp": 80, "max_hp": 80, "attack": 30, "exp_reward": 90, "gold_reward": 75},
    
    # Boss
    {"nama": "DRAGON BOSS", "hp": 350, "max_hp": 350, "attack": 40, "exp_reward": 250, "gold_reward": 200}
]

musuh_aktif = None
defend_aktif = 0  

def mulai_game():
    nama = entry_nama.get().strip()
    if not nama:
        messagebox.showwarning("Peringatan", "Nama karakter tidak boleh kosong!")
        return
    
    player["nama"] = nama
    frame_input_nama.pack_forget()
    
    frame_status.pack(fill="x", padx=15, pady=5)
    frame_log.pack(fill="both", expand=True, padx=15, pady=5)
    frame_menu.pack(fill="x", padx=15, pady=5)
    frame_battle.pack(fill="x", padx=15, pady=5)
    
    update_status_gui()
    set_mode_bertarung(False)
    log_pesan(f"Halo {player['nama']}! Perjalanan windowed RPG-mu dimulai sekarang!")

def log_pesan(teks):
    txt_log.config(state=tk.NORMAL)
    txt_log.insert(tk.END, teks + "\n")
    txt_log.see(tk.END)
    txt_log.config(state=tk.DISABLED)

def update_status_gui():
    lbl_status.config(
        text=f"Hero: {player['nama']} | LV: {player['level']} (Lv.{player['weapon_level']}) | "
             f"HP: {player['hp']}/{player['max_hp']} | EXP: {player['exp']}/{player['exp_next_level']} | $ Gold: {player['gold']}"
    )

def set_mode_bertarung(sedang_bertarung):
    if sedang_bertarung:
        btn_jelajah.config(state=tk.DISABLED)
        btn_istirahat.config(state=tk.DISABLED)
        btn_inventory.config(state=tk.DISABLED)
        btn_toko.config(state=tk.DISABLED) 
        btn_attack.config(state=tk.NORMAL)
        btn_defend.config(state=tk.NORMAL)
        btn_potion.config(state=tk.NORMAL)
    else:
        btn_jelajah.config(state=tk.NORMAL)
        btn_istirahat.config(state=tk.NORMAL)
        btn_inventory.config(state=tk.NORMAL)
        btn_toko.config(state=tk.NORMAL)
        btn_attack.config(state=tk.DISABLED)
        btn_defend.config(state=tk.DISABLED)
        btn_potion.config(state=tk.DISABLED)
        lbl_musuh.config(text="Status Musuh: -")

def jelajahi_hutan():
    global musuh_aktif, defend_aktif
    defend_aktif = 0  
    musuh_tersedia = []

    #Musuh leveling
    if player["level"] <= 2:
        musuh_tersedia = [m for m in daftar_musuh if m["nama"] in ["Goblin", "Mimic", "Orc Fighter"]]
    elif player["level"] <= 4:
        musuh_tersedia = [m for m in daftar_musuh if m["nama"] in ["Goblin", "Mimic", "Orc Fighter", "Shadow Wolf", "Gargoyle Stone", "Dark Mage"]]
    else:
        musuh_tersedia = daftar_musuh
    
    musuh_aktif = random.choice(musuh_tersedia).copy()

    log_pesan(f"\n[!] Jelajah: Kamu berhadapan dengan {musuh_aktif['nama']}!")
    lbl_musuh.config(text=f"Musuh: {musuh_aktif['nama']}  |  HP: {musuh_aktif['hp']}/{musuh_aktif['max_hp']}")
    set_mode_bertarung(True)

def aksi_attack():
    if not musuh_aktif: return
    
    is_critical = random.choice([True, False, False, False, False])
    
    if is_critical:
        damage_total = player["attack"] * 2
        heal_lifesteal = int(damage_total * 0.3)
        player["hp"] = min(player["max_hp"], player["hp"] + heal_lifesteal)
        log_pesan(f"CRITICAL HIT! Kamu menebas {musuh_aktif['nama']} sebesar {damage_total} damage!!")
        log_pesan(f"LIFESTEAL! Kamu menyerap HP musuh sebesar +{heal_lifesteal}!")
    else:
        damage_total = player["attack"]
        log_pesan(f"-> Kamu menyerang {musuh_aktif['nama']} sebesar {damage_total} damage!")
    
    musuh_aktif["hp"] -= damage_total
    update_status_gui()
    
    cek_kondisi_pertarungan()
    if musuh_aktif and musuh_aktif["hp"] > 0:
        serangan_musuh()

def aksi_defend():
    global defend_aktif
    if not musuh_aktif: return
    
    defend_aktif = 3 
    log_pesan("-> Kamu bersiap menahan serangan! Damage musuh berkurang setengah untuk 3 giliran ke depan.")
    serangan_musuh()

def aksi_potion():
    if "Super Potion" in player["inventory"]:
        player["inventory"].remove("Super Potion")
        player["hp"] = min(player["max_hp"], player["hp"] + 70)
        log_pesan(f"-> Kamu meminum Super Potion! HP pulih drastis: {player['hp']}/{player['max_hp']}.")
        update_status_gui()
        if musuh_aktif and musuh_aktif["hp"] > 0: serangan_musuh()
    elif "Health Potion" in player["inventory"]:
        player["inventory"].remove("Health Potion")
        player["hp"] = min(player["max_hp"], player["hp"] + 30)
        log_pesan(f"-> Kamu minum Health Potion! HP pulih menjadi: {player['hp']}/{player['max_hp']}.")
        update_status_gui()
        if musuh_aktif and musuh_aktif["hp"] > 0:
            serangan_musuh()
    else:
        messagebox.showwarning("Inventory", "Health Potion di inventory kamu habis!")

def serangan_musuh():
    global defend_aktif
    if not musuh_aktif: return
    
    damage = musuh_aktif["attack"]
    if defend_aktif > 0:
        damage = damage // 2
        defend_aktif -= 1
        log_pesan(f"<- [DEFEND AKTIF - Sisa {defend_aktif} giliran]")
        
    player["hp"] -= damage
    log_pesan(f"<- {musuh_aktif['nama']} mencakar kamu sebesar {damage} damage!")
    update_status_gui()
    cek_kondisi_pertarungan()

def cek_kondisi_pertarungan():
    global musuh_aktif
    
    if player["hp"] <= 0:
        messagebox.showerror("GAME OVER", "Kamu kalah! Pemainan berakhir.")
        window.destroy()
        return

    if musuh_aktif and musuh_aktif["hp"] <= 0:
        log_pesan(f"\nMENANG! Kamu mengalahkan {musuh_aktif['nama']}!")
        
        # EXP & Gold rewards
        player["exp"] += musuh_aktif["exp_reward"]
        player["gold"] += musuh_aktif["gold_reward"]
        log_pesan(f"Dapat {musuh_aktif['exp_reward']} EXP dan {musuh_aktif['gold_reward']} Gold.")
        
        if random.choice([True, False]):
            player["inventory"].append("Health Potion")
            log_pesan("Item drop: Musuh menjatuhkan 1 Health Potion!")
            
        if player["exp"] >= player["exp_next_level"]:
            player["level"] += 1
            player["exp"] -= player["exp_next_level"]
            player["exp_next_level"] = int(player["exp_next_level"] * 1.5)
            player["max_hp"] += 10
            player["hp"] = player["max_hp"]
            player["attack"] += 5
            log_pesan(f"LEVEL UP! Sekarang kamu Level {player['level']}!")
            
        musuh_aktif = None
        update_status_gui()
        set_mode_bertarung(False)
    elif musuh_aktif:
        lbl_musuh.config(text=f"Musuh: {musuh_aktif['nama']}  |  HP: {musuh_aktif['hp']}/{musuh_aktif['max_hp']}")

def buka_inventory():
    isi_bag = "\n".join([f"- {item}" for item in player["inventory"]]) if player["inventory"] else "Inventory kosong."
    messagebox.showinfo("Isi Inventory", f"Isi Kantong:\n{isi_bag}\n\nTotal barang: {len(player['inventory'])}")

def istirahat_kota():
    player["hp"] = player["max_hp"]
    log_pesan("\nKamu beristirahat di inn kota. HP pulih sepenuhnya!")
    update_status_gui()

def buka_toko():
    """Membuka sub-window baru untuk berbelanja"""
    shop_window = tk.Toplevel(window)
    shop_window.title("Toko Perlengkapan Desa")
    shop_window.geometry("300x250")
    shop_window.resizable(False, False)
    
    biaya_upgrade = player["weapon_level"] * 40 
    
    lbl_toko_gold = tk.Label(shop_window, text=f"Uangmu: {player['gold']} Gold", font=("Arial", 11, "bold"))
    lbl_toko_gold.pack(pady=10)
    
    def beli_potion():
        if player["gold"] >= 20:
            player["gold"] -= 20
            player["inventory"].append("Health Potion")
            lbl_toko_gold.config(text=f"Uangmu: {player['gold']} Gold")
            log_pesan("🛒 Toko: Kamu membeli 1 Health Potion seharga 20 Gold.")
            update_status_gui()
        else:
            messagebox.showwarning("Toko", "Uangmu tidak cukup untuk membeli Potion! (Butuh 20 Gold)")

    def beli_super_potion():
        if player["gold"] >= 45:
            player["gold"] -= 45
            player["inventory"].append("Super Potion") 
            lbl_toko_gold.config(text=f"Uangmu: {player['gold']} Gold")
            log_pesan("🛒 Toko: Membeli Super Potion (HP +70) seharga 45 Gold.")
            update_status_gui()
        else:
            messagebox.showwarning("Toko", "Gold tidak cukup! (Butuh 45 Gold)")

    def upgrade_senjata():
        nonlocal biaya_upgrade
        if player["gold"] >= biaya_upgrade:
            player["gold"] -= biaya_upgrade
            player["weapon_level"] += 1
            player["attack"] += 6 
            log_pesan(f"Toko: Senjata berhasil di-upgrade ke Lv.{player['weapon_level']}! Attack +6.")
            update_status_gui()
            shop_window.destroy()
        else:
            messagebox.showwarning("Toko", f"Uangmu tidak cukup! Upgrade butuh {biaya_upgrade} Gold.")

    tk.Button(shop_window, text="Beli Health Potion (+30 HP) - 20 G", width=30, command=beli_potion, bg="#e2e3e5").pack(pady=3)
    tk.Button(shop_window, text="Beli Super Potion (+70 HP) - 45 G", width=30, command=beli_super_potion, bg="#b2d8d8").pack(pady=3)
    tk.Button(shop_window, text=f"Upgrade Senjata (+8 ATK) - {biaya_upgrade} G", width=30, command=upgrade_senjata, bg="#ffeeba").pack(pady=3)
    tk.Button(shop_window, text="Kembali Petualang", width=15, command=shop_window.destroy).pack(pady=10)


window = tk.Tk()
window.title("Mini RPG Windows Edition")
window.geometry("580x550")
window.resizable(False, False)

frame_input_nama = tk.Frame(window, pady=50)
frame_input_nama.pack()

lbl_tanya = tk.Label(frame_input_nama, text="Masukkan Nama Karakter Kamu:", font=("Arial", 12))
lbl_tanya.pack(pady=10)

entry_nama = tk.Entry(frame_input_nama, font=("Arial", 12), width=20, justify="center")
entry_nama.pack(pady=10)
entry_nama.focus_set()

btn_mulai = tk.Button(frame_input_nama, text="Mulai Petualangan", font=("Arial", 10, "bold"), command=mulai_game, bg="#d4edda")
btn_mulai.pack(pady=10)

window.bind('<Return>', lambda event: mulai_game())

# Tampilan Status
frame_status = tk.LabelFrame(window, text=" STATUS HERO ", padx=10, pady=5)
lbl_status = tk.Label(frame_status, text="", font=("Arial", 9, "bold"))
lbl_status.pack(anchor="w")
lbl_musuh = tk.Label(frame_status, text="Status Musuh: -", font=("Arial", 10), fg="red")
lbl_musuh.pack(anchor="w", pady=(5, 0))

# Kotak Log Cerita
frame_log = tk.LabelFrame(window, text=" LOG PERPETUALANGAN ", padx=10, pady=5)
txt_log = tk.Text(frame_log, wrap=tk.WORD, state=tk.DISABLED, height=12)
txt_log.pack(fill="both", expand=True)

# Menu Utama
frame_menu = tk.LabelFrame(window, text=" MENU UTAMA ", padx=10, pady=5)
btn_jelajah = tk.Button(frame_menu, text="Jelajahi Hutan", width=11, command=jelajahi_hutan, bg="#d4edda")
btn_jelajah.pack(side="left", padx=3)
btn_inventory = tk.Button(frame_menu, text="Buka Inventory", width=11, command=buka_inventory)
btn_inventory.pack(side="left", padx=3)
btn_istirahat = tk.Button(frame_menu, text="Istirahat (Kota)", width=11, command=istirahat_kota, bg="#cce5ff")
btn_istirahat.pack(side="left", padx=3)

# Toko
btn_toko = tk.Button(frame_menu, text="🛒 Masuk Toko", width=11, command=buka_toko, bg="#fff3cd")
btn_toko.pack(side="left", padx=3)

btn_exit = tk.Button(frame_menu, text="Exit Game", width=9, command=window.destroy, bg="#f8d7da")
btn_exit.pack(side="right", padx=3)

# Menu Bertarung
frame_battle = tk.LabelFrame(window, text=" AKSI BERTARUNG ", padx=10, pady=5)
btn_attack = tk.Button(frame_battle, text="ATTACK", width=13, command=aksi_attack, bg="#ffcccb")
btn_attack.pack(side="left", padx=5)
btn_defend = tk.Button(frame_battle, text="DEFEND", width=13, command=aksi_defend, bg="#ffeeba")
btn_defend.pack(side="left", padx=5)
btn_potion = tk.Button(frame_battle, text="USE POTION", width=13, command=aksi_potion, bg="#e2e3e5")
btn_potion.pack(side="left", padx=5)

window.mainloop()