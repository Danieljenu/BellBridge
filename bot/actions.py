from bot.school_bell_system import (
    ringBell,
    ring_assembly_bell,
    play_audio_blocking,
    speak_offline_local,
    speak_alloy_online,
    speak_nova_online,
    speak_onyx_online,
    get_today_assembly_config,
    NATIONAL_ANTHEM_FILE,
    EXTRA1_FILE,
    EXTRA2_FILE
)
# bot/actions.py

def action_ring_bell(schedule):
    ringBell(schedule)

def action_ring_assembly_bell():
    ring_assembly_bell(5)

def action_play_prayer():
    _, _, cfg = get_today_assembly_config()
    play_audio_blocking(cfg["prayer"])

def action_play_birthday():
    _, _, cfg = get_today_assembly_config()
    play_audio_blocking(cfg["birthday"])

def action_play_anthem():
    play_audio_blocking(NATIONAL_ANTHEM_FILE)

def action_announcement(text, mode="offline"):
    if mode == "offline":
        speak_offline_local(text)
    elif mode == "alloy":
        speak_alloy_online(text)
    elif mode == "nova":
        speak_nova_online(text)
    elif mode == "onyx":
        speak_onyx_online(text)
