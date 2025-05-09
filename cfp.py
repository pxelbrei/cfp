# Imports
import logging
import random
import pwnagotchi.plugins as plugins

# Add new phrases
CUSTOM_PHRASES = [
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
    "WPA2: Weak Protection, Amigo!",
    "Beaming packets at light speed!",
    "MAC spoofing is my love language.",
    "Your WiFi is my canvas.",
    "Deauth now, ask questions later.",
    "RSSI: Really Strong Signal Indeed!",
    "Pwning while you're sleeping.",
    "Handshake collector at work!",
    "WiFi waves? More like WiFi slaves!",
    "Breaking encryption like bad habits.",
    "I am the WiFi whisperer.",
    "Pwn or be pwned!",
    "With great WiFi comes great responsibility.",
    "Live free or WiFi hard.",
    "May the packets be ever in your favor.",
    "Pwning is just a click away.",
    "Say hello to my little friend (your WiFi)!",
    "Pwnagotchi: Ghost in the Network",
    "Pwning never tasted so good!",
    "Winter is coming... for your WiFi.",
    "Keep pwning and carry on!",
    "Today's goal: Pwn all the things!",
    "Pwning is my cardio.",
    "One handshake at a time...",
    "Not all heroes wear capes. Some deauth.",
    "Pwning since boot.",
    "Making networks sweat since 2023.",
    "Pwn now, regret never!",
    "Life's short, pwn often!",
    "Pwning: The art of digital seduction.",
]

class CFP(plugins.Plugin):
    # Credits
    __author__ = 'p.xelbrei'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = (
        'A plugin that adds custom phrases. '
        'Displays random phrases based on configurable probabilities. '
        'Perfect for giving your Pwnagotchi more personality!'
    )

    def __init__(self):
        self.options = dict()
        self.running = False

    def on_loaded(self):
        """Called when the plugin is loaded."""
        try:
            logging.info(f"[cfp] Plugin loaded (v{self.__version__})")
        except Exception as e:
            logging.error(f"[cfp] Error in on_loaded: {e}")

    def on_ui_update(self, ui):
        """Displays random phrases based on configurable probabilities."""
        try:
            # Show random phrases
            phrase_chance = int(self.options.get('phrase_chance', 10))  # Default: 10%
            if random.randint(0, 100) < phrase_chance:
                random_phrase = random.choice(CUSTOM_PHRASES)
                ui.set('status', random_phrase)
                logging.debug(f"[cfp] Displayed phrase: {random_phrase}")  # Changed to debug
        except Exception as e:
            logging.error(f"[cfp] Error in on_ui_update: {e}")

    def on_unload(self):
        """Called when the plugin is unloaded."""
        try:
            logging.info("[cfp] Plugin unloaded")
        except Exception as e:
            logging.error(f"[cfp] Error in on_unload: {e}")

def setup():
    """Creates an instance of the plugin."""
    return CFP()
