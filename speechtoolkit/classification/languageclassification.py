from transformers import pipeline
from speechtoolkit.data.languages import language_codes
from speechtoolkit.utils.device import device_map


class WhisperLanguageClassifierModel:
    """
    Use a Whisper-based language classification model.

    **Args**

    device (str): The device to use. Defaults to 'auto'
    model (str): The model ID to use on the Hugging Face Hub.
    **kwargs: Additional arguments to pass to package
    """

    def __init__(
        self,
        device="auto",
        model="ml-for-speech/language-classification",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        device (str): The device to use. Defaults to 'auto'
        model (str): The model ID to use on the Hugging Face Hub.
        **kwargs: Additional arguments to pass to package
        """
        self.pipe = pipeline("audio-classification", model, device=device_map(device))

    def infer_file(self, file_path):
        """
        Run inference on a single file.

        **Args**

        file_path (str): The path of the audio to classify.

        **Returns**

        str: The language ISO language code of the detected language.
        """
        result = self.pipe(file_path)[0]["label"]
        if result in language_codes.keys():
            return language_codes[result]
        else:
            return result
