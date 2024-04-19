from speechtoolkit.utils.device import device_map


class WhisperModel:
    """
    Use OpenAI Whisper for automatic speech recognition.
    """

    def __init__(
        self,
        model="base.en",
        device="auto",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        model (str): Which Whisper model to use
        device (str): The device to use. Defaults to 'auto'
        **kwargs: Additional arguments to pass to NS3VC package
        """
        import whisper

        self.model = whisper.load_model(model).to(device_map(device))

    def infer_file(self, audio_path):
        """
        Run inference on a single file.

        **Args**

        audio_path (str): The path of the original audio.

        **Returns**

        str: The transcript of the audio file.
        """
        self.model.transcribe(audio_path)
