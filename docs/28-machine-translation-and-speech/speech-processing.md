# Speech Processing

## 1. Automatic Speech Recognition (ASR)
Automatic Speech Recognition (ASR), or **Speech-to-Text (STT)**, is the task of converting an acoustic audio signal (someone talking) into written text.
- *Applications*: Siri, Alexa, YouTube closed captions, medical dictation.
- *How it works*: Classical ASR systems (like SMT) used the Noisy Channel Model. An **Acoustic Model** maps the audio waves to phonemes, and a **Language Model** figures out what words those phonemes most likely spell. Modern ASR uses End-to-End deep neural networks (like Whisper).

## 2. Text-to-Speech (TTS)
Text-to-Speech (TTS), or **Speech Synthesis**, is the exact reverse: converting written text into an acoustic audio signal.
- *Applications*: Screen readers for the visually impaired, GPS navigation voices, automated phone menus.
- *How it works*: Modern TTS systems are split into two parts. A text analysis module converts the text into phonetic representations, and a **Vocoder** (like WaveNet) generates the actual raw audio waveforms.

## 3. Speaker Identification and Verification
While ASR cares about *what* is being said, Speaker Identification cares about *who* is saying it.
- **Speaker Identification**: "Who is talking right now out of this list of 10 known people?" (e.g., Diarization: automatically labeling "Speaker 1" and "Speaker 2" in a meeting transcript).
- **Speaker Verification**: "Is the person talking actually who they claim to be?" (e.g., Voice Biometrics for banking authentication: "My voice is my password").

## 4. Phonetics and Phonemes
Speech processing requires understanding **Phonetics** (the physical production of sounds).
A **Phoneme** is the smallest unit of sound in a language that can distinguish one word from another.
- English has 26 letters, but it has about 44 phonemes.
- For example, the "c" in "cat" and the "k" in "kite" are the exact same phoneme (/k/).
- The "th" in "this" and the "th" in "thin" are completely different phonemes.

Speech models rarely map audio directly to words; they map audio to phonemes, and then use a Lexicon (a pronunciation dictionary) to map the sequence of phonemes to actual words.

## 5. Exam Preparation
### Must Memorize
- ASR (Speech-to-Text) uses an Acoustic Model and a Language Model.
- A Phoneme is the smallest distinct unit of sound.

### Likely Theory Question
**Question**: Explain the difference between Speaker Identification and Speaker Verification.
**Answer**: Speaker Identification is a 1-to-N classification task that attempts to determine which specific person from a known database is currently speaking. Speaker Verification is a 1-to-1 binary classification task that authenticates whether the speaker's voice matches the identity they are claiming to be, often used for security applications.
