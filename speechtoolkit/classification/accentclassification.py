from transformers import pipeline
from speechtoolkit.data.languages import language_codes
from speechtoolkit.utils.device import device_map


class EdAccAccentClassifierModel:
    """
    Use a Whisper-based accent classification model trained on the EdAcc dataset. It currently only supports English.

    **Args**

    device (str): The device to use. Defaults to 'auto'
    model (str): The model ID to use on the Hugging Face Hub.
    **kwargs: Additional arguments to pass to NS3VC package
    """

    def __init__(
        self,
        device="auto",
        model="ml-for-speech/accent-classification",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        device (str): The device to use. Defaults to 'auto'
        model (str): The model ID to use on the Hugging Face Hub.
        **kwargs: Additional arguments to pass to NS3VC package
        """
        self.pipe = pipeline("audio-classification", model, device=device_map(device))

    def infer_file(self, file_path):
        """
        Run inference on a single file.

        **Args**

        file_path (str): The path of the audio to classify.

        **Returns**

        str: The detected accent.
        """
        result = self.pipe(file_path)[0]["label"]
        if result in language_codes.keys():
            return language_codes[result]
        else:
            return result
