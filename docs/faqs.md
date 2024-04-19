# FAQs

## What is SpeechToolkit?

Please refer to the [introduction](index.md) for more details.

## Are all models trained by SpeechToolkit?

No, SpeechToolkit is actually primarily composed of third-party models. SpeechToolkit provides a unified, simple Python API to access these models. However, SpeechToolkit does provide some trained models.

## Is Apple Silicon (MPS) supported?

Unfortunately, PyTorch does not yet support all operations on MPS. For simplicity, MPS support is currently disabled across all models, however it may be supported on a case-by-case basis in the future.