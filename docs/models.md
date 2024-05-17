# Models

SpeechToolkit supports several different models for various tasks.

Note that the license "Same" indicates that this is 

## Text-to-Speech

Below is a list of models supported for text-to-speech:

| Name    | License | Link                                            |
| ------- | ------- | ----------------------------------------------- |
| StyleTTS 2 | MIT     | [Repository](https://github.com/yl4579/StyleTTS2) |

Note: StyleTTS 2 by default uses a GPL-licensed phonemizer but we've replaced it with the BSD-licensed [OpenPhonemizer](https://github.com/NeuralVox/OpenPhonemizer).

## Automatic Speech Recognition

Below is a list of supported models for automatic speech recognition.

| Name    | License | Link                                            |
| ------- | ------- | ----------------------------------------------- |
| Whisper | MIT     | [Repository](https://github.com/openai/whisper) |

## Speech Classification

**NOTE: Classification models are not very accurate yet.**

SpeechToolkit supports several different types of speech classification. These models are trained by ML for Speech.

| Version | Task                    | Link                                                                  |
| ------- | ----------------------- | --------------------------------------------------------------------- |
| V1      | Language Classification | [Model](https://huggingface.co/ml-for-speech/language-classification) |
| V1      | Accent Classification   | [Model](https://huggingface.co/ml-for-speech/accent-classification)   |

## Voice Conversion

Below is a list of supported models for voice conversion.

| Name   | License | Link                                                 |
| ------ | ------- | ---------------------------------------------------- |
| LVC-VC | MIT     | [Repository](https://github.com/wonjune-kang/lvc-vc) |
| NS3VC  | MIT     | [Repository](https://github.com/open-mmlab/Amphion)  |

## A Short Guide to Licenses

Note that this is not legal advice.

Please note that models may have a different license than SpeechToolkit. If this is the case, you must comply with both SpeechToolkit *and* the license of the model.

If you're wondering whether or not you can use a model commercially, you should check both the model's license and the pretrained weights' license. The MIT, Apache 2.0, and BSD licenses typically allow commercial use, unless otherwise specified by the authors. However, the BSD-4-Clause license requires you to provide attribution to the author in certain marketing materials (read the full license for details). If the license name includes "NC," it is likely a non-commercial license, which means you cannot use it commercially. Also note that some models may be trained on copyrighted content, which, depending on your jurisdiction, may influence the ability for you to use the models.

Before using models, you should carefully read their licenses.

## Disclaimer

Disclaimer for models trained by SpeechToolkit:

THE MODEL IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS MODEL INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS MODEL.
