# Modello Whisper «base» (sherpa-onnx, int8) per le chat di produzione

Hugging Face non è raggiungibile dalle sessioni: il modello è qui.

```bash
git fetch origin modelli-whisper-base
git worktree add /tmp/whisper origin/modelli-whisper-base   # oppure: git archive origin/modelli-whisper-base | tar -x -C /tmp/whisper
cd /tmp/whisper/whisper-base && cat base-decoder.int8.onnx.part* > base-decoder.int8.onnx && sha256sum -c SHA256SUMS
pip install sherpa-onnx --break-system-packages
```
Uso (Python):
```python
import sherpa_onnx
rec = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder="/tmp/whisper/whisper-base/base-encoder.int8.onnx",
    decoder="/tmp/whisper/whisper-base/base-decoder.int8.onnx",
    tokens="/tmp/whisper/whisper-base/base-tokens.txt", language="it", task="transcribe", num_threads=4)
```
Audio 16 kHz mono, a pezzi da ~25 s (Whisper lavora su finestre di 30 s); i tempi delle parole si ricavano dai pezzi. Per l'inglese: language="en".
