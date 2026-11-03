# Together We Rise

A song coded entirely in Python on [EarSketch](https://earsketch.gatech.edu/), built for the 2024 **Your Voice is Power** hackathon, where it won a national grand prize (1 of 2 winners). The piece follows the journey of Indigenous and Black communities through **peace, challenges, and resilience**, using code to shape the emotional arc of the music.

**[Listen / open in EarSketch](https://earsketch.gatech.edu/earsketch2/?sharing=7k3TekUBjC9SeGF3rjdgZg)**

## About the project

Your Voice is Power is a national competition for middle and high school students, run by TakingITGlobal as part of Amazon Future Engineer Canada. Students use coding to remix songs by Indigenous and other artists while exploring computer science and social justice.

I taught myself both EarSketch and its Python API without tutorials, then built the whole composition as a script. Every musical decision, from tempo to pitch to layering, is expressed in code.

## Musical structure

| Part | Measures (approx.) | What it represents |
|------|--------------------|--------------------|
| 1. Together | 1-7 | Peace, unity and cultural heritage, with soft vocals and a heartbeat-like bass |
| 2. Challenges | 7-26 | Hardship and identity loss, with faster beats, pitch-shifted vocals and whispers |
| 3. Resilience | 25-35 | The opening theme returns after the challenges, joined by choir and a drum bridge |
| 4. Rising Together | 35-51 | A crescendo of choir, vocals and strings celebrating collective strength |

## How the code tells the story

- **Tempo as narrative:** the song starts at 100 BPM, accelerates to 120 BPM for the Challenges section to reflect escalating difficulty, then returns to 100 BPM as a moment of reflection (`setTempo`).
- **Pitch shifting for identity loss:** vocals in the Challenges section are shifted up and down with `PITCHSHIFT` to symbolize the loss of identity (`setEffect`).
- **Whispered vocals:** looped Pharrell Williams whispers represent the inner awareness of losing one's voice.
- **Reverb and volume automation:** `REVERB` and `VOLUME` gain curves create fades, swells and crescendos, and are especially important for the final Rise section.
- **Reusable functions:** each section is its own function (`introTOGETHER`, `verse1CHALLENGES`, `bridge`, `verse2RISE`). The intro function is called twice, at measures 1-7 and 25-31, to bring back the opening theme after the challenges.
- **Loops and conditionals:** `for` loops and `if` statements place beats, flute lines and bass patterns, skipping specific measures to leave space.
- **Nested helper function:** `sfxEffect` repeats a sound effect with a louder volume ramp each time it is used.
- **Rhythm strings:** `makeBeat` patterns (like `"0--0--0---------"`) define bass lines and drum rhythms.

## Concepts used

Python functions, parameters, loops, conditionals, nested functions, variables and constants; EarSketch API calls `fitMedia`, `makeBeat`, `setTempo` and `setEffect`; and audio concepts such as tempo, layering, gain automation, reverb, pitch shifting and song structure.

## Sound sources

The song is built from stems supplied through the competition's EarSketch sound library, including artists such as Dakota Bear, Twin Flames, Samian, Ciara, Khalid, Jayli Wolf and Pharrell Williams. All sounds belong to their respective artists, and I coded the arrangement, structure, effects and timing.

## How to run it

1. Open [EarSketch](https://earsketch.gatech.edu/earsketch2/) and sign in or continue as a guest.
2. Create a new Python script and paste in the contents of `together_we_rise.py`.
3. Click **Run** to render the song, then press play.

The sounds are named constants such as `SAMIAN_PEUP_BEAT_FULL`. They load from EarSketch's sound library, so the script only runs inside EarSketch.

## Author

**Harshita Jindia**
