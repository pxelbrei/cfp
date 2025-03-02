import logging
import random

# Add new faces
CUSTOM_FACES = {
    # Existing faces
    'cool': '(⌐■_■)',
    'happy': 'ʘ‿ʘ',
    'angry': 'ಠ益ಠ',
    'bored': '(－‸ლ)',
    'excited': 'ヽ(°〇°)ﾉ',
    'smart': '(｀・ω・´)',
    'friend': '(ᵔᴥᵔ)',
    'shocked': '(⊙_☉)',
    'thinking': '(・・?)',
    'sleepy': '(－ω－) zzZ',

    # New faces
    'evil': 'ψ(｀∇´)ψ',
    'confused': '(◎_◎;)',
    'surprised': '(°ロ°) !',
    'laughing': '(≧▽≦)',
    'crying': '(╥﹏╥)',
    'determined': '(ง •̀_•́)ง',
    'sneaky': '(¬‿¬)',
    'love': '(❤ω❤)',
    'nerd': '(⌒▽⌒)☆',
    'hero': '(ಠ_ಠ)━☆ﾟ.*･｡ﾟ',
    'pirate': '(☠‿☠)',
    'robot': '[¬º-°]¬',
    'ghost': '(ړײ)',
    'alien': '👽',
    'ninja': '(ᗒᗣᗕ)՞',
    'king': '♚',
    'queen': '♛',
    'joker': '🃏',
    'zombie': '(☠◡☠)',
    'monster': '༼ ༎ຶ ෴ ༎ຶ༽',
}

# Add new phrases
CUSTOM_PHRASES = [
    # Existing phrases
    "Hack the planet!",
    "WiFi? More like Why-Fi!",
    "Pwning all the things...",
    "Just another day in the neighborhood.",
    "Stay curious, stay pwnagotchi.",
    "RSSI level: Over 9000!",
    "I see dead packets...",
    "Keep calm and pwn on.",
    "No WiFi is safe!",
    "Pwnagotchi is watching you.",

    # New phrases
    "Packet sniffer activated!",
    "Deauth storm incoming!",
    "Handshakes for breakfast!",
    "Scanning... scanning... found you!",
    "Signal strength: MAXIMUM!",
    "Encryption? More like suggestion!",
    "Your WiFi is my WiFi now.",
    "Pwning since 2023.",
    "I speak fluent WPA2.",
    "Access points? More like access toys!",
    "Rogue AP deployed!",
    "Your network is my playground.",
    "Pwning with style!",
    "I see you, hidden SSID!",
    "MAC address? More like MAC snack!",
    "Pwning is my superpower.",
    "Your handshake is mine!",
    "Pwning like a pro!",
    "No AP left behind!",
    "Pwning is a lifestyle.",
]

class CFP(plugins.Plugin):
    __author__ = 'p.xelbrei'
    __version__ = '1.0.2'
    __license__ = 'GPL3'
    __description__ = (
        'A plugin that adds custom faces and phrases. '
        'Displays random faces and phrases based on configurable probabilities. '
        'Perfect for giving your Pwnagotchi more personality!'
    )

    def __init__(self):
        self.options = dict()
        self.running = False

    def on_loaded(self):
        """Called when the plugin is loaded."""
        logging.info(f"[cfp] Plugin loaded (v{self.__version__})")

    def on_ui_setup(self, ui):
        """Adds custom faces to the UI."""
        for face_name, face_char in CUSTOM_FACES.items():
            ui.set_face(face_name.upper(), face_char)
        logging.info("[cfp] Custom faces added to UI")

    def on_ui_update(self, ui):
        """Displays random phrases and faces based on configurable probabilities."""
        # Show random phrases
        phrase_chance = int(self.options.get('phrase_chance', 10))  # Default: 10%
        if random.randint(0, 100) < phrase_chance:
            random_phrase = random.choice(CUSTOM_PHRASES)
            ui.set('status', random_phrase)
            logging.info(f"[cfp] Displayed phrase: {random_phrase}")

        # Show random faces
        face_chance = int(self.options.get('face_chance', 5))  # Default: 5%
        if random.randint(0, 100) < face_chance:
            random_face = random.choice(list(CUSTOM_FACES.keys()))
            ui.set_face(random_face.upper())
            logging.info(f"[cfp] Displayed random face: {random_face}")

    def on_unload(self):
        """Called when the plugin is unloaded."""
        logging.info("[cfp] Plugin unloaded")

def setup():
    """Creates an instance of the plugin."""
    return CFP()