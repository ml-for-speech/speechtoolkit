# Examples

## Text-to-Speech

Coming soon

## Automatic Speech Recognition

## Voice Cloning

```python
from speechtoolkit.vc import LVC

vc = LVC(device='auto')

vc.infer_file(
    'original.wav',
    'sample.wav',
    'out.wav'
)
```

## Language Classification

```python
from speechtoolkit.classification.languageclassification import WhisperLanguageClassifier

lc = WhisperLanguageClassifier()

lc.infer_file('audio.wav') # 'en'
```