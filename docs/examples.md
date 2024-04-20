# Examples

## Text-to-Speech

Coming soon

## Automatic Speech Recognition

```python
from speechtoolkit.asr import WhisperModel

model = WhisperModel()

model.infer_file('audio.wav')
```

**With a larger model:**

```python
from speechtoolkit.asr import WhisperModel

model = WhisperModel('medium')

model.infer_file('audio.wav')
```

**With DistilWhisper:**

```python
from speechtoolkit.asr import DistilWhisperModel

model = DistilWhisperModel()

model.infer_file('audio.wav')
```

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
from speechtoolkit.classification.languageclassification import WhisperLanguageClassifierModel

lc = WhisperLanguageClassifierModel()

lc.infer_file('audio.wav') # 'en'
```

## Accent Classification

```python
from speechtoolkit.classification.accentclassification import EdAccAccentClassifierModel

ac = EdAccAccentClassifierModel()

ac.infer_file('audio.wav') # 'Mainstream US English'
```