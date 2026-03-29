import streamlit as st
from source.api.management.scene_manager import SceneManager
from source.api.management.sound_manager import SoundManager
import data.constants as constants
from source.api.management.options_manager import OptionsManager
import time

# Initialize game components
options = OptionsManager()  # Load options
sound_manager = SoundManager()
sound_manager.set_options(options)
sound_manager.load_music()
sound_manager.play_music()

# Initialize scene manager
scene_manager = SceneManager(None, "main_menu")  # Streamlit doesn't use a PyGame screen

st.title("🎮 Pinball Game")

# Placeholder for the game "screen"
screen_placeholder = st.empty()

# Main game loop simulation using Streamlit
if "game_running" not in st.session_state:
    st.session_state.game_running = True

def update_game():
    # Update the active scene
    scene_manager.active_scene.update(constants.DELTA_TIME, [])

    # Render scene to placeholder
    # For now, just display scene name or score (replace with actual render logic)
    screen_placeholder.text(f"Current Scene: {scene_manager.active_scene.name}")

# Game control buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Update Game"):
        update_game()

with col2:
    if st.button("Quit Game"):
        st.session_state.game_running = False
        st.success("Game stopped.")

# Auto-update every X seconds (optional)
if st.session_state.game_running:
    while st.session_state.game_running:
        update_game()
        time.sleep(1 / constants.FRAMERATE)  # simulate framerate
